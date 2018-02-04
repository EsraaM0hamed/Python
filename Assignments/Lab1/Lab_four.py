

def calcArea(shape):
    if shape=="r":
        w=float(input("Enter width: "));
        h=float(input("Enter Height: "));
        area=w*h;
        print(area);
        
       
    elif shape=="c":
        r=float(input("enter Radius: "));
       
        area=2*r*r;
        print(area);

    elif shape=="t":
       b=float(input("Enter Base: "));
       h=float(input("Enter Height: "));
       area=.5*b*h;
       print(area);

       
    else:
        w=float(input("Enter width: "));
        h=float(input("Enter Height: "));
        area=(h+w)*2;
        print(area);

shape=input("Enter Shape: ");
calcArea(shape);        
          


