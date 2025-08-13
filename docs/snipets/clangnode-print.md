Print ClangNode Tree
====================

```python
def print_clangnode(node, depth = 0):
    print("%s '%s' (%s)" % (">"*(depth+1), node, type(node)))
    for i in range(node.numChildren()):
        child = node.Child(i)
        print_clangnode(child, depth+1)
```

