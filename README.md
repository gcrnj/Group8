# Group8

## _ROT13 and Polybius Cipher_

- ***Cornejo, Gio***
- ***Agregado, King Philip Denmar***
- ***Saligan, Ivhan***
- ***Cornejo, Gio B.***

### Testing
- Run `test.py`

### Main
- Run `main.py`

| **Files**                   | **Class**        | **Description**                                                                                                                                                                  |
|-----------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `main.py`                   | `Group8`         | This is where the main function is located.                                                                                                                                      |
| `constants.py`              |                  | Contains all the strings and Enums to prevent hardcoded values.                                                                                                                  |
| `models/base_encryption.py` | `BaseEncryption` | The Abstract class that all the Encryption classes should extend to.<br/>It also has the callable function that will display the encrypted nad decrypted values that extends it. |
| `models/polybius.py`        | `Polybius`       | The class that holds the process of encryption and decryption of ***Polybius***.                                                                                                 |
| `models/rot13.py`           | `ROT13`          | The class that holds the process of encryption and decryption of **ROT13**.                                                                                                      |

## ROT13

    A  B  C  D  E  F  G  H  I  J   K   L   M   N
    1  2  3  4  5  6  7  8  9  10  11  12  13  14

    O   P   Q   R   S   T   U   V   W   X   Y   Z
    15  16  17  18  19  20  21  22  23  24  25  26

## Polybius

            1   2   3    4    5 

     1      A   B   C    D    E
     2      F   G   H   I/J   K
     3      L   M   N    O    P
     4      Q   R   S    T    U
     5      V   W   X    Y    Z