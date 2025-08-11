IDEA Run Configuration for Ghidra
=================================

```xml
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="RunGhidra" type="Application" factoryName="Application">
    <envs>
      <!-- TODO Set the `GHIDRA_INSTALL_DIR` Path Variable under `File/Settings/Path Variables` -->
      <env name="GHIDRA_INSTALL_DIR" value="$GHIDRA_INSTALL_DIR$" />
    </envs>
    <option name="MAIN_CLASS_NAME" value="ghidra.Ghidra" />
    <module name="YourProject.main" /> <!-- TODO Update project/module name -->
    <option name="PROGRAM_PARAMETERS" value="ghidra.GhidraRun" />
    <option name="VM_PARAMETERS" value="-Dghidra.external.modules=$PROJECT_DIR$ -Djava.system.class.loader=ghidra.GhidraClassLoader -Dfile.encoding=UTF8 -Duser.country=US -Duser.language=en -Duser.variant= -Dsun.java2d.opengl=false -Djdk.tls.client.protocols=TLSv1.2,TLSv1.3 -Dcpu.core.limit= -Dcpu.core.override= -Dfont.size.override= -Dpython.console.encoding=UTF-8 -Xshare:off -Dsun.java2d.pmoffscreen=false -Dsun.java2d.xrender=true -Dsun.java2d.uiScale=1 -Dawt.useSystemAAFontSettings=on" />
    <method v="2">
      <option name="Make" enabled="true" />
    </method>
  </configuration>
</component>
```
