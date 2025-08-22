omelet=0
ägg_per_omelet=2
egg_destroyed=0

omelet=int(input("hur många omeleter vi du ha "))
ägg_per_omelet=int(input("hur många egg per omelet "))

for i in range(0,omelet):
    egg_destroyed+=ägg_per_omelet
    omelet+=1

print (f"du förstöde",[egg_destroyed]," för att få",[omelet])

   


    





 