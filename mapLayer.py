# mapRBM: get the layer number and number of nodes in the corrosponding hidden layer and generates the SPICE code of that layer
# mapRBM( layer2, layerNUM )
# Output: RBM_layer2
# Input parameters:
# layer2: number of nodes in the hidden layer
# layerNUM: the layer number

############################################################
#                                                          #
#               2018 Ramtin Zand. All rights reserved.     #
#                    ramtinmz@knights.ucf.edu              #
#                                                          #
############################################################
import random
def mapLayer(layer1,layer2, LayerNUM,length,weight_var):  
	f=open("layer"+str(LayerNUM)+".sp", "w")
	g=open("posweight"+str(LayerNUM)+".txt", "r")
	n=1;
	m=1;
	#f.write("*Ramtin Zand, January 2018\n")
	#f.write("*Resistive RBM\n")
	#f.write(".lib './models' ptm14hp\n")    #the transistor library can be changed here (of course in this current format the weighted array does not use a transistor)
	#f.write(".include 'diff.sp'\n")
	#f.write(".include 'sigmoid.sp'\n")
	#f.write(".option post\n")
	#f.write(".op\n")
	#f.write(".PARAM VddVal=0.8\n")
	#f.write(".PARAM tsampling=2n\n")
	f.write(".SUBCKT layer"+ str(LayerNUM)+" vdd vss ")

	for i in range(layer1):
		i2=i+1
		f.write("in%d "%i2)
	
	for i in range(layer2):
		i2=i+1		
		f.write("out%d "%i2)
	
	f.write("\n\n**********Non-Negative Weighted Array****************\n")
	for l in g:
		if (float(l)!=0):	
			if (m < layer2+1):
				f.write("Rwpos%d_%d in%d sp%d %f\n"% (n,m,n,m,float(l)+random.uniform(-1*weight_var,weight_var)))
				m+=1;
			else:
				n+=1;
				m=1;		
				f.write("Rwpos%d_%d in%d sp%d %f\n"% (n,m,n,m,float(l)+random.uniform(-1*weight_var,weight_var)))
				m+=1;
		else:
			m+=1;
	f.write("\n\n**********Negative Weighted Array****************\n\n")
	n=1;
	m=1;
	g.close()
	h=open("negweight"+str(LayerNUM)+".txt", "r")
	for l in h:
		if (float(l)!=0):
			if (m < layer2+1):
				f.write("Rwneg%d_%d in%d sn%d %f\n"% (n,m,n,m,float(l)+random.uniform(-1*weight_var,weight_var)))
				m+=1;
			else:
				n+=1;
				m=1;		
				f.write("Rwneg%d_%d in%d sn%d %f\n"% (n,m,n,m,float(l)+random.uniform(-1*weight_var,weight_var)))
				m+=1;
		else:
			m+=1;
			

	h.close()
	f.write("\n\n**********Positive Biases****************\n\n")
	m=1;
	a=open("posbias"+str(LayerNUM)+".txt", "r")
	for l in a:
		if (float(l)!=0):
			f.write("Rbpos%d vdd sp%d %f\n"% (m,m,float(l)+random.uniform(-1*weight_var,weight_var)))
			m+=1;
		else:
			m+=1;
	a.close()

	f.write("\n\n**********Negative Biases****************\n\n")
	m=1;
	b=open("negbias"+str(LayerNUM)+".txt", "r")
	for l in b:
		if (float(l)!=0):
			f.write("Rbneg%d vss sn%d %f\n"% (m,m,float(l)+random.uniform(-1*weight_var,weight_var)))
			m+=1;
		else:
			m+=1;
	b.close()

	f.write("\n\n**********Weight Differntial Op-AMPS****************\n\n")
	for ii in range(layer2):
		jj=ii+1;
		if (LayerNUM!=(length-1)):
			f.write("XDIFFw%d sp%d sn%d xin%d diff\n"% (jj,jj,jj,jj))
		else:
			f.write("XDIFFw%d sp%d sn%d xin%d diff%d\n"% (jj,jj,jj,jj,LayerNUM))
	
	f.write("\n\n**********neurons****************\n\n")	
	for i in range(layer2):
		j=i+1;
		f.write("Xsig%d xin%d out%d vdd 0 neuron\n"% (j,j,j))
		
	m=1;
	#f.write("Vbias vb 0 0.4\n")
	#f.write(".param vddval=0.8\n")
	#f.write("VSUP+ vsup+ 0 vddval\n")
	#f.write("VSUP- vsup- 0 0\n")
##################### Input test#################
	#f.write("\n\n**********Input Test****************\n\n")
	#c=open("singletestinput"+str(LayerNUM)+".txt", "r")
	#for l in c:	
	#	f.write("v%d n%d 0 DC %f\n"% (m,m,float(l)))
	#	m+=1;
	#c.close()

	#f.write("\n\n\nvdd vdd 0 DC VddVal\n")
	#f.write(".TRAN 0.1n tsampling\n")
	#f.write(".MEASURE TRAN pwr AVG 'i(vdd)*VddVal' FROM=0n TO=tsampling\n")
	#for iii in range(layer2):
	#	f.write(".MEASURE TRAN VXIN%d AVG v(out%d) FROM=0n TO=tsampling\n"%(iii,iii))
		#f.write(".MEAS TRAN VXIN%d FIND v(xin%d) AT=2n\n"%(iii,iii)) 
	f.write(".ENDS layer"+ str(LayerNUM))
	f.close()






			
			
	
