import numpy as np
# RGB = XYZ2RGB * XYZ
XYZ2RGB = np.linalg.inv([[0.49,0.31,0.2],[0.177,0.813,0.01],[0,0.01,0.99]])

# to find true white object representation in rgb
# Now find XYZ

# X = sum(C(lambda)*x(lambda))
# Y = sum(C(lambda)*y(lambda))
# Z = sum(C(lambda)*z(lambda))

# Need to get C and tristimulus values
#  

with open('CA1_Data.csv') as file:
    lines = file.read().splitlines()
    data = [[float(val) for val in line.split(',')] for line in lines]
l, x, y, z, i_p, i_s, i_u = data

## Task A
# Reflatance p = 1 for all l


def XYZ_to_RGB(X, Y, Z):
    return [sum([a*b for a,b in zip(XYZ2RGB[i],[X,Y,Z])])*255 for i in range(len(XYZ2RGB[0]))]

def get_XYZ(I,x,y,z,l):
    X = sum([a*b for a,b,c in zip(I,x,l)])
    Y = sum([a*b for a,b,c in zip(I,y,l)])
    Z = sum([a*b for a,b,c in zip(I,z,l)])
    return X,Y,Z


# For illuminant phillips
X_p, Y_p, Z_p = get_XYZ(i_p,x,y,z,l)
R_p, G_p, B_p = XYZ_to_RGB(X_p,Y_p,Z_p)
print("X_p, Y_p, Z_p\t:\t",X_p, Y_p, Z_p)
print("R_p, G_p, B_p\t:\t",R_p, G_p, B_p)
# For illuminant silvania 
X_s, Y_s, Z_s = get_XYZ(i_s,x,y,z,l)
R_s, G_s, B_s = XYZ_to_RGB(X_s,Y_s,Z_s)
print("X_s, Y_s, Z_s\t:\t",X_s, Y_s, Z_s)
print("R_s, G_s, B_s\t:\t",R_s, G_s, B_s)
# For illuminant uniform
X_u, Y_u, Z_u = get_XYZ(i_u,x,y,z,l)
R_u, G_u, B_u = XYZ_to_RGB(X_u,Y_u,Z_u)
print("X_u, Y_u, Z_u\t:\t",X_u, Y_u, Z_u)
print("R_u, G_u, B_u\t:\t",R_u, G_u, B_u)


#### Task B
# Uniform Illumination spectra
# reflectance p(l) = w(l)/max(w(l))

def get_reflectance(w):
    max_w = max(w)
    return [val_w/max_w for val_w in w]

# for p(x)

px = get_reflectance(x)
X,Y,Z = get_XYZ(px,x,y,z,l)
R,G,B = XYZ_to_RGB(X,Y,Z)
print("X,Y,Z\t:\t",X,Y,Z)
print("R,G,B\t:\t",R,G,B)

# for p(y)

py = get_reflectance(y)
X,Y,Z = get_XYZ(py,x,y,z,l)
R,G,B = XYZ_to_RGB(X,Y,Z)
print("X,Y,Z\t:\t",X,Y,Z)
print("R,G,B\t:\t",R,G,B)

# for p(z)

pz = get_reflectance(z)
X,Y,Z = get_XYZ(pz,x,y,z,l)
R,G,B = XYZ_to_RGB(X,Y,Z)
print("X,Y,Z\t:\t",X,Y,Z)
print("R,G,B\t:\t",R,G,B)