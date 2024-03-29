x = 3.14159
y = 4*x
print("Os valores são:")
print("{:8.2f}".format(x))
print("{:8.2f}".format(y))



x = "Teste de Nome"
y = "menor"
print("Os valores são:")
print(f"{20*'x'}")
print("{:^20}".format(x))
print("{:^20}".format(y))
print(f"{20*'x'}")

x = """
  _____   __   __  ____   U _____ u  _           
 |_ " _|  \ \ / /U|  _"\ u\| ___"|/U|"|u         
   | |     \ V / \| |_) |/ |  _|"  \| |/         
  /| |\   U_|"|_u |  __/   | |___   |_|          
 u |_|U     |_|   |_|      |_____|  (_)          
 _// \\_.-,//|(_  ||>>_    <<   >>  |||_         
(__) (__)\_) (__)(__)__)  (__) (__)(__)_)        
"""

print(x)