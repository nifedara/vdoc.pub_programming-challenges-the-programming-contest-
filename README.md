# 'vdoc.pub_programming-challenges-the-programming-contest' Interpreter-problem solution in Python-
#### Interpreter Instruction

##### PC/UVa IDs: 110106/10033, Popularity: B, Success rate: low Level: 2
A certain computer has ten registers and 1,000 words of RAM. Each register or
RAM location holds a three-digit integer between 0 and 999. Instructions are encoded
as three-digit integers and stored in RAM. 
#### The encodings are as follows:

* 1000	means halt
* 02dn	means set register d to n (between 0 and 9)
* 03dn	means add n to register d
* 04dn	means multiply register d by n
* 05ds	means set register d to the value of register s
* 06ds	means add the value of register s to register d
* 07ds	means multiply register d by the value of register s
* 08da	means set register d to the value in RAM whose address is in register a
* 09sa	means set the value in RAM whose address is in register a to the value of register s
* 00ds	means goto the location in register d unless register s contains 0
* 13dn	Means subtract n from register d
* 16ds	Subtract register s from register d

All registers initially contain 0000. The initial content of the RAM is read from standard input. The first instruction to be executed is at RAM address 0. All results are
reduced modulo 10000.

### Input
There will be a blank line between each two consecutive inputs.
Each input case consists of up to 1,000 three-digit unsigned integers, representing the
contents of consecutive RAM locations starting at 0. Unspecified RAM locations are
initialized to 000.
