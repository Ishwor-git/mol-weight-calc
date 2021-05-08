class Molecules:
    Elements = {'H':1.00797,'He':4.00260,
                'Li':6.941,'Be':9.0122,'B':10.810,'C':12.001,'N':14.008,'O':15.999,'F':18.998,'Ne':20.179,
                'Na':22.990,'Mg':24.305,'Al':26.981,'Si':28.086,'P':30.974,'S':32.060,'Cl':35.453,'Ar':39.948,
                'K':39.098,'Ca':40.080,'Sc':44.956,'V':50.942,'Cr':51.996,'Mn':54.938,'Fe':55.847,'Ni':58.700,'Co':58.933,'zn':65.380,'Ga':69.720,'Ge':72.590,'As':74.922,'Se':78.96,'Br':79.904,'Kr':83.800,
                'Rb':85.468,'Sr':87.620,'Y':88.906,'Zr':91.220,'Nb':92.906,'Mo':95.940,'Tc':98,'Ru':101.07,'Pd':106.4,'Ag':107.868,'Cd':112.41,'In':114.82,'Sn':118.69,'I':126.905,'Te':127.60,'Xe':131.30,
                'Cs':132.905,'Ba':137.33,'La':138.906,'Hf':178.49,'Ta':180.948,'W':183.85,'Re':186.207,'Os':190.2,'Ir':192.22,'Pt':195.09,'Au':196.967,'Hg':200.59,'Tl':204.37,'Pb':207.2,'Bi':208.980,'Po':209,'At':210,'Rn':222,
                'Fr':223,'Ra':226.025,'Ac':227.028,'Rf':261,'Bh':262,'Db':262,'Sg':263,
                'Ce':140.12,'Pr':140.908,'Nd':144.24,'Pm':145,'Sm':150.4,'Eu':151.96,'Gd':157.25,'Tb':158.925,'Dy':162.50,'Ho':164.930,'Er':167.26,'Tm':168.934,'Yb':173.04,'Lu':174.967,
                'Pa':231.036,'Th':232.038,'Np':237.048,'U':238.029,'Pu':242,'Am':243,'Bk':247,'Cm':247,'No':250,'Cf':251,'Es':252,'Hs':255,'Mt':256,'Fm':257,'Md':258,'Lr':260
                }

    def __init__(self,formula):
        self.mol_f = formula

    def list_mol(self):
        molecules = []
        x = ''
        for i in self.mol_f:
            if i.isupper():
                x = ''
                x = i
                molecules.append(x+'1')

            elif i.islower():
                del molecules[-1]
                x += i
                molecules.append(x+'1')

            elif i.isdigit():
                x += i
                del molecules[-1]
                molecules.append(x)
        return molecules

    def dict_mol(self):
        lst = Molecules.list_mol(self)
        dict = {}
        y = 0
        x = ''
        for i in lst:
            y = 0
            x = ''
            for j in i:
                if j.isdigit():
                    y = y*10 + int(j)
                else:
                    x += j
            dict[x] = y
        return dict

    def lst(self):
        elem = set()
        for i in Molecules.dict_mol(self):
            elem.add(i)
        return elem

    def weight(self):
        sum = 0
        for i in Molecules.lst(self):
            sum += Molecules.Elements[i] * Molecules.dict_mol(self)[i]
        return round(sum,3)

ch = 'C'
print('''........................................
.....          Greetings !         .....
........................................

This program is made to calculate molecular
weight of compounds.
How to use ?

1) Enter molecular formula of compounds in simple
language. ie. H2O, HNO3, H2SO4, CuSO4, CO2, C6H6 etc. 

2) Molecular Formula should be in most condensed form as possible.
ie. C2H4O2 will give more accurate results compared to CH3COOH

2) Take notice of Uppercase and lowercase.
ie. CO2 and Co2 are different molecules

3) This program is unable to compute weight of compounds
that contain () and might cause errors ie. Ca(OH)2, Zn(NO3)2 etc.

please send suggestions at raishwor2@gmail.com 

THANK YOU !!!''')
while ch.upper() == 'C':
    print()
    a = Molecules(input('Molecular Formula :: '))
    print('Molecular Weight :: {0}'.format(a.weight()))
    print()
    ch = input('Continue or exit (C/E) ?? ' )