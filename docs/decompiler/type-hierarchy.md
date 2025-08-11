# Decompiler Type Hierarchy

This is a simplified version of the hierachy of classes and methods commonly used when using the decompiler API.

## Decompiler Engine 

```mermaid
classDiagram
  class DecompileResults {
    +getCCodeMarkup() ClangTokenGroup
    +getDecompiledFunction() DecompiledFunction
    +getHighFunction() HighFunction
  }
  class DecompInterface {
    +decompileFunction() DecompileResults
  }
  class DecompiledFunction {
    + getC() String
    + getSignature() String
  }
  DecompileResults <-- DecompInterface
  ClangTokenGroup <-- DecompileResults
  DecompiledFunction <-- DecompileResults
  HighFunction <-- DecompileResults
```

## C Language Representation

### Nodes and Tokens

**Not all `Clang*Token` classes are inherited from `ClangToken` (e.g. `ClangVariableToken`)!**

```mermaid
classDiagram
  class ClangNode {
    +getMinAddress() Address
    +getMaxAddress() Address
    +Parent() ClangNode
    +Child() ClangNode
  }
  <<Interface>> ClangNode
  note for ClangNode "Needs recursive traversal"
  class ClangToken {
    +getVarnode() Varnode
  }
  class ClangStatement {
    +getPcodeOp() PcodeOp
  }
  class ClangTokenGroup
  note for ClangTokenGroup "Somewhat arbitrary grouping, doesn't necessarily follow syntax!"
  ClangNode <|.. ClangToken
  ClangNode <|.. ClangStatement
  ClangToken --* ClangTokenGroup
  PcodeOp <-- ClangStatement
  ClangTokenGroup <|-- ClangStatement
```

## High-Level Representation

### Symbols, Variables, Varnodes

```mermaid
classDiagram
  class Varnode {
    +getAddress() Address
    +getOffset() long
  }
  class HighSymbol {
    +getSymbol() Symbol
  }
  class HighVariable{
    +getSymbol() HighSymbol
    +getRepresentative() Varnode
  }
  Varnode <-- HighVariable
  HighSymbol <-- HighVariable
  Symbol <-- HighSymbol
  Address <-- Varnode
  class Function{
    +getVariables() Variable[]
  }
  class Variable{
    getMinAddress() Address
  }
  Address <-- Variable
  Variable <-- Function


```

`HighVariable`s represent a _view_ on the underlying variable. The real, modifiable `Variable` object can be accessed by:

1. Retrieving the _representative_ varnode of the `HighVariable`.
2. Then match the address (`.getAddress().equals(...)`) with the minimum addresses of the variables known by the current function (`currentFunction.getVariables(null)`). This should handle stack/register address spaces too. 

