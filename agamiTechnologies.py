#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Student:
    def __init__(self,Name,RollNo,Course):
        self.Name=Name
        self.RollNo=RollNo
        self.Course=Course


# In[17]:


def insert(Name,RollNo,Course):
    ob=Student(Name,RollNo,Course)
    return ob


# In[18]:


def view(database):
    if len(database)<1:
        print("No data Found")
    else:
        print("Data Found ! Here the list of Student")
    print("****************************************************************************")
    for i in database:
        
        print("Name : ",i.Name, "RollNo : ",i.RollNo, "Course : ",i.Course)
        print("_________________________________________________________________________")
    print("*****************************************************************************")
    


# In[19]:


def delete(database,value):
  
    for i in range(len(database)):
        if database[i].RollNo == value:
            copy_delete_data = i
            break
    else:
        print("data does't exist")
    del database[copy_delete_data]
    print("data deleted")
        


# In[20]:


def edit(database,value):
    delete(database,value)
    Name= input("enter name : ")
    RollNo = int(input("Enter eoll :"))
    Course = input("enter Course")
    read=insert(Name,RollNo,Course)
    database.append(read)
    print("Updated")


# In[21]:


def template():
    print("Type insert to INSERT data : ")
    print("Type view to VIEW data : ")
    print("Type delete to DELETE data : ")
    print("Type edit to EDIT data :  ")
    print("Type exit to EXIT from STUDENT Data : ")
                        


# In[ ]:


database=[]

while True:
    template()
    
    check = input("Enter What You Want To Do ? ")
    if check == 'exit':
        
        break
    elif check == 'insert':
        Name=input("Enter Name : ")
        RollNo= int(input( " Enter RollNo  : "))
        Course = input("Enter Course : ")
        item=insert(Name,RollNo,Course)
        database.append(item)
        print("Sucessfully Enter Data")
        
    elif check == 'view':
        view(database)
    
    elif check == 'delete':
        bulk=True
        while bulk:
            view(database)
            print("Enter Exit to exit : ")
            value = input("Enter the roll no.")
            if value != 'exit' :
                value=int(value)
                delete(database,value)
            else:
                bulk=False
                
    elif check=='edit':
        view(database)
        value = int(input("Enter RollNo of student : "))
        edit(database,value)
        
        
    else:
        pass
    


# In[ ]:




