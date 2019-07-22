#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jersey
Version  : 2.22.2
Release  : 3
URL      : https://github.com/jersey/jersey/archive/2.22.2.tar.gz
Source0  : https://github.com/jersey/jersey/archive/2.22.2.tar.gz
Source1  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-client/1.13/jersey-client-1.13.jar
Source2  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-client/1.13/jersey-client-1.13.pom
Source3  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-client/1.19/jersey-client-1.19.jar
Source4  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-client/1.19/jersey-client-1.19.pom
Source5  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-client/1.9/jersey-client-1.9.jar
Source6  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-client/1.9/jersey-client-1.9.pom
Source7  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-core/1.13/jersey-core-1.13.jar
Source8  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-core/1.13/jersey-core-1.13.pom
Source9  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-core/1.17.1/jersey-core-1.17.1.jar
Source10  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-core/1.17.1/jersey-core-1.17.1.pom
Source11  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-core/1.19/jersey-core-1.19.jar
Source12  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-core/1.19/jersey-core-1.19.pom
Source13  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-core/1.9/jersey-core-1.9.jar
Source14  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-core/1.9/jersey-core-1.9.pom
Source15  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-project/1.13/jersey-project-1.13.pom
Source16  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-project/1.19/jersey-project-1.19.pom
Source17  : https://repo1.maven.org/maven2/com/sun/jersey/jersey-project/1.9/jersey-project-1.9.pom
Source18  : https://repo1.maven.org/maven2/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2/jersey-guava-2.22.2.jar
Source19  : https://repo1.maven.org/maven2/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2/jersey-guava-2.22.2.pom
Source20  : https://repo1.maven.org/maven2/org/glassfish/jersey/bundles/repackaged/project/2.22.2/project-2.22.2.pom
Source21  : https://repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-client/2.22.2/jersey-client-2.22.2.jar
Source22  : https://repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-client/2.22.2/jersey-client-2.22.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.0 CDDL-1.1 GPL-2.0
Requires: mvn-jersey-data = %{version}-%{release}

%description
This directory contains Jersey & JAX-RS tools - ant tasks, maven plugins, shell scripts etc.

%package data
Summary: data components for the mvn-jersey package.
Group: Data

%description data
data components for the mvn-jersey package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.13
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.13/jersey-client-1.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.13
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.13/jersey-client-1.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.19
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.19/jersey-client-1.19.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.19
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.19/jersey-client-1.19.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.9
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.9/jersey-client-1.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.9
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.9/jersey-client-1.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.13
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.13/jersey-core-1.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.13
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.13/jersey-core-1.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.17.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.17.1/jersey-core-1.17.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.17.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.17.1/jersey-core-1.17.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.19
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.19/jersey-core-1.19.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.19
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.19/jersey-core-1.19.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.9
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.9/jersey-core-1.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.9
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.9/jersey-core-1.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-project/1.13
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-project/1.13/jersey-project-1.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-project/1.19
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-project/1.19/jersey-project-1.19.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-project/1.9
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/com/sun/jersey/jersey-project/1.9/jersey-project-1.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2/jersey-guava-2.22.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2/jersey-guava-2.22.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/bundles/repackaged/project/2.22.2
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/bundles/repackaged/project/2.22.2/project-2.22.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/core/jersey-client/2.22.2
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/core/jersey-client/2.22.2/jersey-client-2.22.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/core/jersey-client/2.22.2
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/jersey/core/jersey-client/2.22.2/jersey-client-2.22.2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.13/jersey-client-1.13.jar
/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.13/jersey-client-1.13.pom
/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.19/jersey-client-1.19.jar
/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.19/jersey-client-1.19.pom
/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.9/jersey-client-1.9.jar
/usr/share/java/.m2/repository/com/sun/jersey/jersey-client/1.9/jersey-client-1.9.pom
/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.13/jersey-core-1.13.jar
/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.13/jersey-core-1.13.pom
/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.17.1/jersey-core-1.17.1.jar
/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.17.1/jersey-core-1.17.1.pom
/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.19/jersey-core-1.19.jar
/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.19/jersey-core-1.19.pom
/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.9/jersey-core-1.9.jar
/usr/share/java/.m2/repository/com/sun/jersey/jersey-core/1.9/jersey-core-1.9.pom
/usr/share/java/.m2/repository/com/sun/jersey/jersey-project/1.13/jersey-project-1.13.pom
/usr/share/java/.m2/repository/com/sun/jersey/jersey-project/1.19/jersey-project-1.19.pom
/usr/share/java/.m2/repository/com/sun/jersey/jersey-project/1.9/jersey-project-1.9.pom
/usr/share/java/.m2/repository/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2/jersey-guava-2.22.2.jar
/usr/share/java/.m2/repository/org/glassfish/jersey/bundles/repackaged/jersey-guava/2.22.2/jersey-guava-2.22.2.pom
/usr/share/java/.m2/repository/org/glassfish/jersey/bundles/repackaged/project/2.22.2/project-2.22.2.pom
/usr/share/java/.m2/repository/org/glassfish/jersey/core/jersey-client/2.22.2/jersey-client-2.22.2.jar
/usr/share/java/.m2/repository/org/glassfish/jersey/core/jersey-client/2.22.2/jersey-client-2.22.2.pom
