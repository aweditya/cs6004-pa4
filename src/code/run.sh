#!/bin/sh

# Compile testcases to get the class file
/usr/lib/jvm/java-8-openjdk-amd64/bin/javac $1/*.java

/usr/lib/jvm/java-8-openjdk-amd64/bin/javac -cp ../sootclasses-trunk-jar-with-dependencies.jar PA4.java AnalysisTransformer.java
/usr/lib/jvm/java-8-openjdk-amd64/bin/java -cp ../sootclasses-trunk-jar-with-dependencies.jar:. PA4 $1

