Import Existing Ghidra Project to Eclipse
==========================================

**⚠️ Since Ghidra 11.1 the GhidraDev plugin has an Import feature, you can just use that!**

Prerequisites
-------------

- Working Eclipse installation
- Installed GhidraDev extension in Eclipse  
  - You can find the `GhidraDev.zip` file in your Ghidra distribution package, no need to [build from source](https://voidstarsec.com/blog/ghidra-dev-environment)
  - Extensions targeting different Ghidra major versions may need different GhidraDev versions
- Working Ghidra
  - Ghidra was executed at least once
  - Ghidra doesn't have the module under development (or one with the same name) installed
- The appropriate Ghidra installation and JDK is configured in GhidraDev 
  - Eclipse `GhidraDev` menu -> `Link Ghidra...`

Import
------

### Create Project

- Create a new `Ghidra Module` project in Eclipse (`File -> New -> Project`)
- Choose the appropriate name and location, click `Next` in the wizard
  - Leave `Create run configuration` enabled 
- Deselect all Module templates, click `Next`
- Select appropriate Ghidra installation, click `Next`
- Leave Jython unconfigured (we're doing Java now)
- Click `Finish`

A new project is created, you can find it in the Project Explorer, usually on the left.

### Import Files

- Right click the new Ghidra project, select `Import...`
- Select `File system`
- Click `Browse...` and select the root directory of the project to be imported
- Open the root folder in the left pane and select the following directories:
  - `src/`
  - `data/`
- With the root folder selected on the left, select the following files on the right:
  - `build.gradle`
  - `extension.properties`
  - `Module.manifest`
- Select any other files/folders specifically needed by the original project
- Enable the `Overwrite existing resources without warning` option
- **Under `Advanced >>`, enable the `Create links in workspace` option** - 
  This way the files in the original location will be edited instead of copies, 
  so you can use the existing Git repo to track changes. 
  Locations will be linked via the `.project` file created by Eclipse - 
  this is specific to your installation, don't track these in Git. 
- Click `Finish`

You can now run/debug the project with the Run Configuration that was automatically created during project creation. 

License
-------

This file is licenced under CC0, please add it to your projects so people will strugle less with Eclipse!

If you feel anything is missing/inaccurate, please leave a comment or reach out to any available channel!