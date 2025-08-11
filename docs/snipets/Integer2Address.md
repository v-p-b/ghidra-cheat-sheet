Integer to Address
==================

```java
import ghidra.program.model.address.AddressFactory;
import ghidra.program.model.address.Address;

// ...

AddressFactory addressFactory = flatProgramApi.getAddressFactory();
Address a = addressFactory.getAddress(0x1337);
```

