Services
========

Some functionality, like code viewer actions can be accessed via global [Services](https://scrapco.de/ghidra_docs/javadoc/ghidra/app/services/package-summary.html). The process of getting a service instance differs in plugins and scripts.

## Plugins

```java
CodeViewerService codeViewer = getTool().getService(CodeViewerService.class);
```

Here `getTool()` is a protected method of the `Plugin` ancestor class.

## Scripts

```python
code_viewer = state.getTool().getService(CodeViewerService)
```

Here `state` is a predefined variable in the scripting context. 

