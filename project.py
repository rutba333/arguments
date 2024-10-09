import os
shutdown=input("do you wanna shut down your computer?(yes or no):")
if shutdown=='no':
    exit()
else:
    os.system("shutdown/s/t/1")