import math
def mapWB(layernum,rp,rap):
	#sMTJ=(math.pi)*lMTJ*wMTJ/4
	#rp=RA/sMTJ
	#rap=(1+(TMR/100))*rp
	for i in range(layernum-1):
		j=i+1
		f=open("W"+str(j)+".txt","r")
		wp=open("posweight"+str(j)+".txt", "w")
		wn=open("negweight"+str(j)+".txt", "w")
		for l in f:
			if (float(l)==1):
				wp.write("%f\n"%rp)
				wn.write("%f\n"%rap)

			if (float(l)==-1):
				wp.write("%f\n"%rap)
				wn.write("%f\n"%rp)
			if (float(l)==0):
				wp.write("%f\n"%rp)
				wn.write("%f\n"%rp)
				#wp.write("%f\n"%0)
				#wn.write("%f\n"%0)
		
		f.close()
		g=open("B"+str(j)+".txt","r")
		bp=open("posbias"+str(j)+".txt", "w")
		bn=open("negbias"+str(j)+".txt", "w")
		for l in g:
			if (float(l)==1):
				bp.write("%f\n"%rp)
				bn.write("%f\n"%rap)

			if (float(l)==-1):
				bp.write("%f\n"%rap)
				bn.write("%f\n"%rp)
			if (float(l)==0):
				bp.write("%f\n"%rp)
				bn.write("%f\n"%rp)
				#bp.write("%f\n"%0)
				#bn.write("%f\n"%0)
		
		g.close()


				
	
