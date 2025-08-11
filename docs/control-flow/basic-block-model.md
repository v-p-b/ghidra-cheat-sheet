Basic Block Model
=================

In Ghidra you can get information about the control-flow between basic blocks using the `BasicBlockModel`.

```python
from ghidra.program.model.block import BasicBlockModel
from ghidra.util.task import ConsoleTaskMonitor


blockModel = BasicBlockModel(currentProgram)
monitor = ConsoleTaskMonitor()

# ...

blocks = blockModel.getCodeBlocksContaining(func.getBody(), monitor)

while blocks.hasNext():
    bb = blocks.next()
    # ...
```

* Basic blocks are represented by `CodeBlock` objects
* Edges are represented by `CodeBlockReference` objects that include information about the `FlowType` and destinations

A more complete example can be found in [ghidra-graph-export](https://github.com/v-p-b/ghidra-graph-export)

