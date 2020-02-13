.SUBCKT neuron in out vsup+ vsup-

X1 out input vsup- vsup- nfet nfin=10
X2 out input vsup+ vsup+ pfet nfin=10
Rlow in2 input 2.12206590789e+16
vin in in2 -0.4
Rhigh input out 2.22816920329e+16

.ENDS neuron
