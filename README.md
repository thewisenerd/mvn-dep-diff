# mvn-dep-diff
--------------

a stupid tool that copies [@JakeWharton/dependency-tree-diff](https://github.com/JakeWharton/dependency-tree-diff) that
is for gradle for maven


### use-case
------------

- you want to add a dependency to your project
- you do not know what dependent versions need to be updated (pre-dependency-addition)
- you do not know what dependent versions have not yet been updated (and maven still is picking up older versions) (post-dependency-addition)
- maven provides `dependency:tree` but parsing it line-by-line maybe difficult

### demo

```diff
--- /base
+++ /dependency
 |     |  +- org.glassfish.jersey.bundles.repackaged:jersey-guava:jar:2.25.1:compile
 |     |  \- org.glassfish.hk2:osgi-resource-locator:jar:1.0.1:compile
 |     \- org.jvnet.mimepull:mimepull:jar:1.9.6:compile
 +- io.dropwizard:dropwizard-auth:jar:1.3.9:compile
-+- com.fasterxml.jackson.core:jackson-core:jar:2.9.8:compile
++- com.fasterxml.jackson.core:jackson-core:jar:2.12.4:compile
 +- com.auth0:java-jwt:jar:3.2.0:compile
 |  +- commons-codec:commons-codec:jar:1.11:compile
 |  \- org.bouncycastle:bcprov-jdk15on:jar:1.55:compile
 +- org.jetbrains.kotlin:kotlin-stdlib:jar:1.3.21:compile
 |  +- org.jetbrains.kotlin:kotlin-stdlib-common:jar:1.3.21:compile
 |  \- org.jetbrains:annotations:jar:13.0:compile
-+- org.slf4j:slf4j-api:jar:1.7.26:compile
++- org.slf4j:slf4j-api:jar:1.7.32:compile
 +- junit:junit:jar:4.12:test
 |  \- org.hamcrest:hamcrest-core:jar:1.3:test
 +- org.jetbrains.kotlin:kotlin-test-junit:jar:1.3.21:test
 |  +- org.jetbrains.kotlin:kotlin-test-annotations-common:jar:1.3.21:test
 |  \- org.jetbrains.kotlin:kotlin-test:jar:1.3.21:test
 |     \- org.jetbrains.kotlin:kotlin-test-common:jar:1.3.21:test
```

### todo
--------

- code clean up
- any downgrades in scope (eg., from `compile` to `test`) can likely be outright ignored


### goals
---------

- web interface? the core logic is simple enough
- change language; write in kotlin-native so i can kang this onto a web interface
- web interface
