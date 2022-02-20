# copy your dat. file from Airfoil Tools
import pandas as pd # you need to install openpyxl
af = pd.read_excel("C:/Users/???/Desktop/yourexcelname.xlsx", sheet_name = "Sheet1", header = None) # use your path
r = af.shape[0] # number of rows
f = open("C:/Users/???/Desktop/yourtxtname.txt", "w") # your txt file to write
for i in range(r):
    f.write("Point(" + str(i+1) + ") = {" + str(af[0][i]) + ", " + str(af[1][i]) + ", 0, 1};\n") # write yout points in Gmsh format

# if you want to connect the points with lines
for n in range(r-1):
    f.write("Curve(" + str(n+1) + ") = {" + str(n+1) + ", " + str(n+2) + "};\n")
f.write("Curve(" + str(n+2) + ") = {" + str(n+2) + ", 1};")

# if you want toconnect the points with a spline
f.write("Spline(1) = {" + ", ".join(str(n) for n in list(range(1,102))) + "};")
