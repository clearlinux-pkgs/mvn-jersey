PKG_NAME := mvn-jersey
URL = https://github.com/jersey/jersey/archive/2.22.2.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2/jersey-guava-2.22.2.jar : https://repo1.maven.org/maven2/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2/jersey-guava-2.22.2.pom : https://repo1.maven.org/maven2/org/glassfish/jersey/bundles/repackaged/project/2.22.2/project-2.22.2.pom : 

include ../common/Makefile.common
