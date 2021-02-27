import time, os

os.system ("cls") 

#print("===========================================================")
#msg = "Hello World"
#print(msg)
#for x in range(2):
#    print(msg)



def countdown(t,cad): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        #print(timer, end="\r") 
        print(cad + timer, end="\r") 
        time.sleep(1) 
        t -= 1

#print("===========================================================")
print("  ")

v_file = 'c:\\celf\\cl_python\\vocabulary.txt'

with open(v_file, 'r') as v_obj:
    v_lineas = v_obj.readline()
    
    while v_lineas:
        v_ind =1 
        v_vec_words=v_lineas.split(';')
        for i in v_vec_words :
            #print(i+input('>'))
            #print(i)
           
            if v_ind==1:
              countdown(5, i+ ' ')
              previo=i
            else:
               print(previo+' =='+i)
            v_ind = 2  
        v_lineas = v_obj.readline()
                
#print("===========================================================")

print("  ")
print("  ")
print("  ")
