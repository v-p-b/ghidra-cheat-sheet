# Dump C language structures for the current function
# @author buherator
# @category Dev
# @keybinding
# @menupath
# @toolbar
# @runtime PyGhidra

from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.app.decompiler import ClangToken, ClangStatement

def print_varnode(varnode, depth):
    print("%s%s" % (" "*depth, varnode))

def print_highvar(hvar, depth):
    print("%sHighVar: %s" % (" "*depth, hvar.getName()))
    print("%sRepresentative:" % (" "*(depth+1),))
    print_varnode(hvar.getRepresentative(), depth+2)
    print("%sInstances:" % (" "*(depth+1),))
    for i in hvar.getInstances():
        print_varnode(i, depth+2)

def print_highsym(hsym, depth):
    print("%sHighSym: %s (%s)" % (" "*depth, hsym.getName(), hsym.getDataType().getDisplayName()))

def print_clangtoken_details(token, depth):
    if token.getMinAddress() is not None:
        print("%sAddress: %s - %s" % (" "*depth, token.getMinAddress(), token.getMaxAddress()))
    if isinstance(token, ClangToken):
        if token.getPcodeOp() is not None:
            print("%sPcodeOp: %s" % (" " * depth, token.getPcodeOp()))
        high_function = token.getClangFunction().getHighFunction()
        high_sym = token.getHighSymbol(high_function)
        high_var = token.getHighVariable()
        if high_var is not None:
            print_highvar(high_var, depth)
        if high_sym is not None:
            print_highsym(high_sym, depth)
    if isinstance(token, ClangStatement):
        if token.getPcodeOp() is not None:
            print("%sPcodeOp: %s" % (" " * depth, token.getPcodeOp()))

def print_clangnode(node, depth=0):
    print("%s '%s' (%s)" % (">" * (depth + 1), node, type(node)))
    print_clangtoken_details(node, depth + 2)
    for i in range(node.numChildren()):
        child = node.Child(i)
        print_clangnode(child, depth + 1)


func = getFunctionContaining(currentAddress)

options = DecompileOptions()
monitor = ConsoleTaskMonitor()
ifc = DecompInterface()
ifc.setOptions(options)
ifc.openProgram(currentProgram)
res = ifc.decompileFunction(func, 60, monitor)

root_token_group = res.getCCodeMarkup()

print_clangnode(root_token_group)
