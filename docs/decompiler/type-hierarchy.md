# Decompiler Type Hierarchy

This is a simplified version of the hierachy of classes and methods commonly used when using the decompiler API.

```mermaid
classDiagram
  class DecompileResults {
    +getCCodeMarkup() ClangTokenGroup
    +getDecompiledFunction() DecompiledFunction
  }
  class DecompInterface {
    +decompileFunction() DecompileResults
  }
  class DecompiledFunction {
    + getC() String
    + getSignature() String
  }
```


```mermaid
classDiagram
  class ClangNode {
    +getMinAddress() Address
    +getMaxAddress() Address
    +Parent() ClangNode
    +Child() ClangNode
  }
  <<Interface>> ClangNode
  class ClangToken {
    +getVarnode() Varnode
  }
  class ClangTokenGroup
  ClangNode <|-- ClangToken
  ClangToken *-- ClangTokenGroup
```
