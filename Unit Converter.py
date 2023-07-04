Unit = input("Enter the unit m2,cm2,in2,ft2,yd2: ")
O_unit = input("Enter the desired unit  m2,cm2,in2,ft2,yd2: ")

#m2

if Unit == "m2" and O_unit == "m2":
    m2 = float(input("Enter m2: "))
    m2=m2
    print(m2)
elif Unit == "m2" and O_unit == "cm2":
     m2 = float(input("Enter m2: "))
     cm2 = 10000*m2
     print(cm2)
elif Unit == "m2" and O_unit == "in2":
     m2 = float(input("Enter m2: "))
     in2 = 1550*m2
     print(in2)
elif Unit == "m2" and O_unit == "ft2":
    m2 = float(input("Enter m2: "))
    ft2 = 10.764*m2
    print(ft2)
elif Unit == "m2" and O_unit == "yd2":
    m2 = float(input("Enter m2: "))
    yd2 = 1.196*m2
    print(yd2)
elif Unit == "m2" and O_unit == "acre":
    m2 = float(input("Enter m2: "))
    acre = 0.000247*m2
    print(acre)
    
    # CM2
    
if Unit == "cm2" and O_unit == "cm2":
    cm2 = float(input("Enter cm2: "))
    cm2=cm2
    print(m2)
elif Unit == "cm2" and O_unit == "m2":
     cm2 = float(input("Enter cm2: "))
     m2 = 0.0001*cm2
     print(cm2)
elif Unit == "cm2" and O_unit == "in2":
     cm2 = float(input("Enter cm2: "))
     in2 = 0.155*cm2
     print(in2)
elif Unit == "cm2" and O_unit == "ft2":
    cm2 = float(input("Enter cm2: "))
    ft2 = 0.001076*cm2
    print(ft2)
elif Unit == "cm2" and O_unit == "yd2":
    cm2 = float(input("Enter cm2: "))
    yd2 = 0.0001196*cm2
    print(yd2)
elif Unit == "cm2" and O_unit == "acre":
    cm2 = float(input("Enter cm2: "))
    acre = 0.0000000247*cm2
    print(acre)
    
    #in2
    
if Unit == "in2" and O_unit == "in2":
    in2 = float(input("Enter in2: "))
    in2=in2
    print(m2)
elif Unit == "in2" and O_unit == "m2":
     in2 = float(input("Enter in2: "))
     m2 = 0.000645*in2
     print(cm2)
elif Unit == "in2" and O_unit == "cm2":
     in2 = float(input("Enter in2: "))
     cm2 = 6.452*in2
     print(in2)
elif Unit == "in2" and O_unit == "ft2":
    in2 = float(input("Enter in2: "))
    ft2 = 0.006944*in2
    print(ft2)
elif Unit == "in2" and O_unit == "yd2":
    in2 = float(input("Enter in2: "))
    yd2 = 0.0007716*in2
    print(yd2)
elif Unit == "in2" and O_unit == "acre":
    in2 = float(input("Enter in2: "))
    acre = 0.000000159*in2
    print(acre)
    
    #ft2
    
if Unit == "ft2" and O_unit == "ft2":
    ft2 = float(input("Enter ft2: "))
    ft2=ft2
    print(m2)
elif Unit == "in2" and O_unit == "m2":
     ft2 = float(input("Enter ft2: "))
     m2 = 0.0929*ft2
     print(cm2)
elif Unit == "ft2" and O_unit == "cm2":
     ft2 = float(input("Enter ft2: "))
     cm2 = 929.03*ft2
     print(in2)
elif Unit == "ft2" and O_unit == "in2":
    ft2 = float(input("Enter ft2: "))
    in2 = 144*ft2
    print(ft2)
elif Unit == "ft2" and O_unit == "yd2":
    ft2 = float(input("Enter ft2: "))
    yd2 = 0.1111*ft2
    print(yd2)
elif Unit == "ft2" and O_unit == "acre":
    ft2 = float(input("Enter ft2: "))
    acre = 0.00002296*ft2
    print(acre)