# Imports eventuels
#import numpy as np
# Déclaration des classes et fonctions
class Vector :
#constructeur
    def __init__(self, coeffs): 
        self.list_coeffs = coeffs; 
        #print('Vector instance');
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
        #return np.shape(self.list_coeffs);
        return len(self.list_coeffs); 
    def get(self, i):
        if i > (len(self.list_coeffs)-1):
            print('i too big');
        else: 
            return self.list_coeffs[i];
    def calculate_sum(self, vec2):
           if self.dimension() == vec2.dimension():
               sum_vec = self.list_coeffs;
               for i in range(0,len(self.list_coeffs)):
                   sum_vec[i] =  self.get(i) + vec2.get(i);
               vec_sum = Vector(sum_vec);
               return vec_sum; 
           else:
               raise Exception("Different dimensions!")
            
class Polynomial(Vector) :
    def __int__(self,list_coeffs):
        super().__init__(list_coeffs)
    def __str__(self):
        sentence = "";
        for i in range(0,len(self.list_coeffs)):
                       if i == (len(self.list_coeffs)-1) :
                           sentence += str(self.list_coeffs[i])+"x^" + str(i);
                       else:
                           sentence += str(self.list_coeffs[i])+ "x^" + str(i) + " +"; 
        return sentence;
    def degree(self):
        return self.dimension()-1;
    def evaluate(self, x):
        mult_vec = self.list_coeffs;
        for i in range(0,len(self.list_coeffs)):
            mult_vec[i] =  self.get(i)*x;
        pol_mult = Polynomial(mult_vec);
        return pol_mult;
    

# Programme principal
v1 = Vector([[10, 20],[10,20]]);
v2 = Vector((5, -2, 1.5));
v3 = Vector(range(4,8));

# tester __str__(): affiche sentence
print(v1)
print(v2)
print(v3)

print(v2.get(2));
print(v3.dimension());

v4 = Vector(range(15, 16));
#print(v1.calculate_sum(v4));

pol1 = Polynomial([5,2]);
print(pol1)
print(pol1.evaluate(2)); 

