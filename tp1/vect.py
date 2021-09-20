# Imports éventuels
import numpy as np
# Déclaration des classes et fonctions
class Vector :
    #constructeur
    def __init__(self, coeffs): 
        self.list_coeffs = coeffs; 
        print('Vector instance');
    def __str__(self):
        sentence = "[";
        for i in range(0,len(self.list_coeffs)):
                       if i == (len(self.list_coeffs)-1) :
                           sentence += str(self.list_coeffs[i]);
                       else:
                           sentence += str(self.list_coeffs[i])+ "; ";
        sentence = sentence + "]";
        return sentence;
    def dimension(self):
        return np.shape(self.list_coeffs);
    def get(self, i):
        if i > (len(self.list_coeffs)-1):
            print('i too big');
        else: 
            return self.list_coeffs[i];
    def calculate_sum(self, vec2):
        try:
           for i in range(0,len(self.list_coeffs)-1):
               sum[i] = self.get(i) + vec2.get(i);
           vec_sum = Vector(sum);
           return vec_sum; 
        except ValueError:
            print("Different dimension!"); 
            
    

# Programme principal
v1 = Vector([[10, 20],[10, 20]]);
v2 = Vector((5, -2, 1.5));
v3 = Vector(range(4,8));

# tester __str__(): affiche sentence
print(v1)
print(v2)
print(v3)

print(v2.get(1)); 

#v1.dimension()

