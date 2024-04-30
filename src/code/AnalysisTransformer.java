import java.util.*;

import soot.*;
import soot.jimple.Jimple;
import soot.jimple.Constant;
import soot.jimple.DefinitionStmt;
import soot.jimple.NumericConstant;
import soot.jimple.toolkits.scalar.Evaluator;
import soot.toolkits.graph.*;
import soot.toolkits.scalar.SimpleLocalDefs;

public class AnalysisTransformer extends BodyTransformer {
    @Override
    protected void internalTransform(Body body, String phaseName, Map<String, String> options) {
        PatchingChain<Unit> units = body.getUnits();

        // Construct CFG for the current method's body
        BriefUnitGraph cfg = new BriefUnitGraph(body);

        // Construct local definitions analysis
        SimpleLocalDefs localDefs = new SimpleLocalDefs(cfg);

        // Iterate through CFG
        for (Unit u : cfg) {
            // Constant propagation
            for (ValueBox vb : u.getUseBoxes()) {
                Value v = vb.getValue();
                if (v instanceof Local) {
                    // Only look at local variables
                    Local vLocal = (Local) v;
                    List<Unit> vLocalDefs = localDefs.getDefsOfAt(vLocal, u);
                    if (vLocalDefs.size() == 1) {
                        if (vLocalDefs.get(0) instanceof DefinitionStmt) {
                            DefinitionStmt def = (DefinitionStmt) vLocalDefs.get(0);
                            Value leftOp = def.getLeftOp();
                            Value rightOp = def.getRightOp();

                            // Check if the RHS is a constant
                            if (rightOp instanceof NumericConstant) {
                                // If yes, check if the RHS fits inside the box
                                if (vb.canContainValue(rightOp)) {
                                    vb.setValue(rightOp);
                                }
                            }
                        }
                    }
                }                
            }

            // Evaluate all constant expressions
            for (ValueBox vb : u.getUseBoxes()) {
                Value v = vb.getValue();
                if (!(v instanceof Constant)) {
                    if (Evaluator.isValueConstantValued(v)) {
                        Value constV = Evaluator.getConstantValueOf(v);
                        if (vb.canContainValue(constV)) {
                            vb.setValue(constV);
                        }
                    }
                }
            }
        }
    }
}
