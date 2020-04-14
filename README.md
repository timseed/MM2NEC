# MM2NEC

Why do this ??

For many years I have used MMAMANA-Gal on Windows, it is a nice and simple way of modelling antennas. However I now find myself wanting to try other systems. 99% of which are using some form of NEC.

## Does MMANA not have NEC ?

I do not know - there is an option to look at the definition of the antenna - this produces a file like this...

```text
40m Dipole
*
14.15
***Wires***
1
-10.16, 0.0,    0.0,    10.16,  0.0,    0.0,    8.000e-04,      -1
***Source***
1,      0
w1c,    0.0,    1.0
***Load***
0,      0
***Segmentation***
800,    80,     2.0,    2
***G/H/M/R/AzEl/X***
2,      15.0,   1,      50.0,   120,    60,     0.0
```

This is a simple Dipole for 40m. For the moment I want to convert the "WIRES"  section only.