GUI
====

Ghidra provides a set of widgets that provide a more convenient interface and extended features compared to the underlying Swing objects.


## Dialogs

Dialogs are implemented as sublasses of [DialogComponentProvider](https://scrapco.de/ghidra_docs/javadoc/docking/DialogComponentProvider.html).

* `OptionDialog` provides static methods to display dialogs for data input, e.g.:
    * `OptionDialog.showInputSingleLineDialog()` - Input one line
    * ...
* `OkDialog` can be used to show information, e.g.:
    * `OkDialog.showInfo()`
    * `OkDialog.showError()`
    * ...
* `ListSelectionDialog` displays a list of rows to select from, while providing sorting, filtering and ordering just like standard Ghidra widgets. 
    * `DataToStringConverter.stringDataToStringConverter` provides a common implementation for the last constructor argument. 
    * `.show()` displays the instantiated dialog and blocks. `.getSelectedItem()` retrieves the selection. `.wasCancelled()` should be used to check if the user cancelled the dialog. 

Dialog widgets can also be used to let users select Ghidra objects, e.g. `DataTypeSelectionDialog`.

Parent `Component` parameters can usually be `null` for simple use-cases. 


