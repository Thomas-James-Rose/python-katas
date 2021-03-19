# InfiniTick 2.0

## Task

Make an interpreter for an extended version of the esolang InfiniTick. InfiniTick has 8 possible commands that will need to be parsed. It also runs infinitely, stopping the program only when an error occurs.

## Syntax/Info

InfiniTick runs in an infinite loop. It has an infinite memory of bytes and an infinite output amount and the program only stops when an error is reached. The program is also supposed to ignore non-commands.

## Commands

```
>: Move data selector right.

<: Move data selector left.

+: Increment amount of memory cell. Truncate overflow: 255+1=0.

-: Decrement amount of memory cell. Truncate overflow: 0-1=255.

*: Output the ascii value of memory cell.

&: Raise an error and stop the program execution.

[: Jump past the matching ] if the memory cell value is zero.

]: Jump past the matching [ if the memory cell value is non-zero.
```

## Examples

Use the examples in `/programs` to test your interpreter.
