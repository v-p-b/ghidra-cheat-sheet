

## Tips&Tricks

### Variable from HighVariable

`HighVariable`s represent a _view_ on the underlying `Variable`. The real, modifiable `Variable` object can _sometimes_ (TODO this needs investigation) be accessed by:

1. Retrieving the _representative_ varnode of the `HighVariable`.
2. Then match the address (`.getAddress().equals(...)`) with the minimum addresses of the variables known by the current function (`currentFunction.getVariables(null)`). This should handle stack/register address spaces too. 

### Get the Type of ClangVariableToken 

Say you end up at a variable in the decompiled C code - how do you programatically get the `DataType` of that variable?

`ClangVariableToken` corresponds to a `Varnode` that is - due to the SSA representation used at high-level - can't be easily associated with a data type. 

I found it easiest to use `HighlevelFunction.getSymbolTable()` to get all defined symbols in the function and match these by name with the language token. 


## Documentation

* [Decompiler Concepts](https://scrapco.de/ghidra_docs/Features/Decompiler/DecompilePlugin/DecompilerConcepts.html)
* [P-Code Reference](https://scrapco.de/ghidra_docs/GhidraDocs/languages/html/pcoderef.html)
