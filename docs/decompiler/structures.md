Structures
==========

## Field Access

LLM's tend to suggest that structure field access can be checked by matching Pcode operations with the expected field offset. This is really cumbersome, as pointer increments can happen in multiple ways, interleaved with "boring" operations. 

A much more straightforward way is to use `ClangFieldToken` like so:

```python
cfunc = res.getCCodeMarkup()

for token in cfunc.tokenIterator(True):
    if isinstance(token, ClangFieldToken):
        print("{} ({}) ClangNode:\n\t{}".format(token, token.getDataType().getDisplayName(), token.Parent()))
```
