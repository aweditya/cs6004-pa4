#!/bin/sh

# Compile testcases to get the class file
/src/openj9-openjdk-jdk8/build/linux-x86_64-normal-server-release/images/j2sdk-image/bin/javac $1/*.java >/dev/null 2>&1

/src/openj9-openjdk-jdk8/build/linux-x86_64-normal-server-release/images/j2sdk-image/bin/javac -cp ../sootclasses-trunk-jar-with-dependencies.jar PA4.java AnalysisTransformer.java 2>/dev/null
/src/openj9-openjdk-jdk8/build/linux-x86_64-normal-server-release/images/j2sdk-image/bin/java -cp ../sootclasses-trunk-jar-with-dependencies.jar:. PA4 $1 2>/dev/null 

