class Student:
    #we are using the default __init__

    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    
    def raise_hand(self):
        print("Pick me!")



#Student is super class (parent class)
#ChattyStudent has access to all of parent's methods/attributes
#including hello() and raise_hand()
class ChattyStudent(Student):
    
    #we are using the default __init__

    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    def raise_hand(self):
        #run this 10 times
        for i in range(10):
            super().raise_hand()