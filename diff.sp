*Differential Amplifier with Gain=50
.SUBCKT diff in+ in- out
R1 in- n1 1k
R2 in+ n2 1k
E1 out 0 OPAMP n2 n1

R3 n1 out 15.0k
R4 n2 0 15.0k
.ENDS diff

