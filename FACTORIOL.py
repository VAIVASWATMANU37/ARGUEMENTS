def VIPER(SRT10):
    if SRT10  == 0 or SRT10  == 1:
        return 1
    else:
        return SRT10 * VIPER(SRT10-1)
ACR_X= int(input("ENTER THE NO.!!! "))
if ACR_X < 0:
    print("ERROR 396!!! FACTORIAL DOES WORK ON NEGETIVE NO.!!!!!!!")
else:
    print("THE FACTORIAL OF THE NO. IS",VIPER(ACR_X))