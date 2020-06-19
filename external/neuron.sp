.SUBCKT neuron in out vsup+ vsup-

X1 out input vsup- vsup- nfet nfin=10
X2 out input vsup+ vsup+ pfet nfin=10
Rlow in2 input 3183.09886184
vin in in2 -0.4
Rhigh input out 11140.8460164

.ENDS neuron
