
import unittest;
word=input("Please Enter Word: ");
letter=input("PLease Enter Letter: ")



def lab_two(word,letter):
    res=[];
    for w,char in enumerate(word):
        
        if char==letter:
           
            res.append(w);
     
    return res;   

print(lab_two(word,letter))  

                  
           


        
       