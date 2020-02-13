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
import mapLayer
def mapFC(nodes,length,weight_var):
	f=open("classifier.sp", "w")
	f.write("*Fully-connected Classifier\n")
	f.write(".lib './models' ptm14hp\n")    #the transistor library can be changed here (of course in this current format the weighted array does not use a transistor)
	f.write(".include 'diff.sp'\n")
	f.write(".include 'diff2.sp'\n")
	#f.write(".include 'diff3.sp'\n")
	f.write(".include 'neuron.sp'\n")
	f.write(".option post\n")
	f.write(".op\n")
	f.write(".PARAM VddVal=0.8\n")
	f.write(".PARAM VssVal=-0.8\n")
	f.write(".PARAM tsampling=1n\n")
	for i in range(len(nodes)-1):
		f.write(".include 'layer"+ str(i+1)+".sp'\n")
	for i in range(len(nodes)-1):
		mapLayer.mapLayer(nodes[i],nodes[i+1],i+1,length,weight_var)
		f.write("Xlayer"+ str(i+1)+" vdd vss ")
		for i2 in range(nodes[i]):			
			if (i==0):
				f.write("in%d "%i2)
			else:
				f.write("out%d_%d "%(i,i2))
		for i3 in range(nodes[i+1]):
			if (i==len(nodes)-2):
				f.write("output%d "%i3)
			else:
				f.write("out%d_%d "%(i+1,i3))
		f.write("layer"+ str(i+1)+"\n\n\n")


	f.write("\n\n**********Input Test****************\n\n")
	c=open("singletestinput1.txt", "r")
	m=0
	for l in c:	
		f.write("v%d in%d 0 DC %f\n"% (m,m,float(l)))
		m+=1;
	c.close()
	
	f.write("\n\n\nvss vss 0 DC VssVal\n")
	f.write("\n\n\nvdd vdd 0 DC VddVal\n")
	f.write(".TRAN 0.1n tsampling\n")
	f.write(".MEASURE TRAN pwr AVG 'i(vdd)*VddVal' FROM=0n TO=tsampling\n")
	f.write(".MEASURE TRAN powr AVG POWER FROM=0n TO=tsampling\n")
	for iii in range(nodes[len(nodes)-1]):
		#f.write(".MEASURE TRAN VXIN%d AVG v(out%d) FROM=0n TO=tsampling\n"%(iii,iii))
		f.write(".MEAS TRAN VOUT%d FIND v(output%d) AT=tsampling\n"%(iii,iii))
	f.close() 



			
			
	
