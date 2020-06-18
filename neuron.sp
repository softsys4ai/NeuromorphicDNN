.SUBCKT neuron in out vsup+ vsup-

X1 out input vsup- vsup- nfet nfin=10
X2 out input vsup+ vsup+ pfet nfin=10
Rlow in2 input 4244.13181578
vin in in2 -0.4
Rhigh input out 16976.5272631

.ENDS neuron
