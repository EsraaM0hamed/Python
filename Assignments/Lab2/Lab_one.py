import re;

class Person:
    def __init__(self,name,salary,mood,healthRate):
        self.name=name;
        self.salary=salary;
        self.mood=('Happy','tired','Lazy');
        
        self.healthRate=healthRate;
    
   
    def buy(self,itemNum):
        if itemNum==1:

            self.salary-=25;  
           

    
    def sleep(self,hour):
        if hour==7:
            print(self.mood[0])
        elif  hour<7:
            print(self.mood[1])
        else:
            print(self.mood[2])

    def eat(self,healthRate):
        if healthRate>=75:
            print("100% htn")
        elif healthRate<=75:
            print("75% htn")
        elif healthRate<50:
        
            print("50% htn")
  
    
          
class Car:
    def __init__(self,name, disatnce,fuelRate, velocity):
        self.name=name;
        self.distance=disatnce;
        self.fuelRate=fuelRate;
        self.velocity=velocity;
    

   
        

    def run(self,velocity, distance):

        self.fuelRate =(self.fuelRate*0.1*distance/10);

        return self.velocity==velocity;
        


    def stop(self):
        
        return self.velocity==0;
        
    
        
    def refuel(self,fualRate):
        if fualRate<0:
            return self.fuelRate==0;
        if fualRate>100:
            return 100;


        
       

    
class Employee(Person):
    
    def __init__(self,name,salary,healthRate,mood,id,car,email,dtw):
        Person.__init__(self,name,salary,mood,healthRate);
        
        self.id=id;
        self.car=car;
        self.email=email;
        self.dtw=dtw;
        self.name=name

    def drive(self,distance,time):
       v=distance/time;
       car=Car();
       car.run(v,distance)

    

    def getSalary(self,salary):
        if salary<5000:
            print( "the salary should be 5000");
        elif salary<1000:
            self.salary==1000;
            return self.salary;
            
       
    @property
    def email(self):
        return self.__email;
    

    @email.setter
    def email(self,email):
       # EMAIL_REGEX = re.compile([^@]+@[^@]+\.[^@]+)
        # if not EMAIL_REGEX.match(email):
        #     print(" InValid email !!")
        
        pass;
       


class Office(Employee):
    def __init__(self,name,employee):
        self.name=name;
        self.employee=employee;
      

    def hire(self):
       
        return self.name +" Is Hired";

    def fire(self,name):
       
            return self.name+"Is Fired";
        
    
    
      
    def  get_employee(self,id):
        if id==self.id:
            return self.name;
        else:
            return 0
    
    
    def calculate_lateness(self):
        pass
    def deduct(self):
        pass
    def reward(self):
        pass



    def work(self,workHour):
        if workHour==8:
            print("Happy")
        elif workHour>8:
            print("Tired")
        else:
            print("Lazy")

    def send_mail(self):
        pass
        


p=Person("esraa",5000,"g",4);
pp=Person("engy",6000,'g',4)
x=Employee("seham",3,5000,"mood",5,"128 Fiat","seham@com",100)
e=Employee("esraa",75,5000,'mood',2,"128 Fiat","seham@com",100)
o=Office("esraa","Programmer")


print(p.sleep(7))
print(p.eat(3))
print(p.name)
print(pp.salary)
print(p.buy(1))
print(e.name,e.car)
print(e.eat(3))
print(o.hire())
print(o.fire(2))
print(x.mood[1])

