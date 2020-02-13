import os

class TuneParam:
    def __init__(self, testnum, RA, 
                 TMR, gain1, gain2):
        print ("[STATUS]: initializing TuneParam class")
        
        self.update_testFC (RA,TMR,testnum)
        self.update_diff (gain1)
        self.update_diff2 (gain2)
        os.system('python testFC.py')
  
    def update_testFC(self, RA,TMR,
                      testnum):
	ff=open("testFC.py","r+")
	i=0
	data= ff.readlines()
	for line in data:
		i+=1
		if  'RA=' in line:
			data[i-1]='RA=' + str(RA) +'\n'
		if  'TMR=' in line:
			data[i-1]='TMR=' + str(TMR) +'\n'
		if  'testnum=' in line:
			data[i-1]='testnum=' + str(testnum) +'\n'
      
	ff.seek(0)
	ff.truncate()
	ff.writelines(data)
	ff.close()

    def update_diff (self, gain1):
	ff=open("diff.sp", "r+")
	i=0
	data= ff.readlines()
	for line in data:
		i+=1
		if  'R3' in line:
			data[i-1]='R3 n1 out ' + str(gain1) +'k\n'
		if  'R4' in line:
			data[i-1]='R4 n2 0 ' + str(gain1) +'k\n'

	ff.seek(0)
	ff.truncate()
	ff.writelines(data)
	ff.close()

    def update_diff2 (self, gain2):
	ff=open("diff2.sp", "r+")
	i=0
	data= ff.readlines()
	for line in data:
		i+=1
		if  'R3' in line:
			data[i-1]='R3 n1 out ' + str(gain2) +'k\n'
		if  'R4' in line:
			data[i-1]='R4 n2 0 ' + str(gain2) +'k\n'

	ff.seek(0)
	ff.truncate()
	ff.writelines(data)
	ff.close()


    
