Decompiler Setup
================

### Java

```java
import ghidra.app.decompiler.*;
import ghidra.app.decompiler.component.DecompilerUtils;

private DecompInterface setUpDecompiler(Program program) {

		DecompileOptions options = DecompilerUtils.getDecompileOptions(state.getTool(), program);

		DecompInterface decomplib = new DecompInterface();

		decomplib.setOptions(options);

		decomplib.toggleCCode(true);
		decomplib.toggleSyntaxTree(true);
		decomplib.setSimplificationStyle("decompile");

		return decomplib;
}
```

### Python

```python
from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# ...

options = DecompileOptions()
monitor = ConsoleTaskMonitor()
ifc = DecompInterface()
ifc.setOptions(options)
ifc.openProgram(program)
res = ifc.decompileFunction(func, 60, monitor)
```
