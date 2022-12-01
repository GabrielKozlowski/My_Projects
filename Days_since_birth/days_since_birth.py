from tkinter import *
from datetime import datetime


root = Tk()
root.title('TIME SINCE BIRTH')
root.configure(bg='#66CDAA')

def getBirthDate():

    birthDate = inputBirthDate.get()
    errorLabel = Label(root,bg='#CD3333',fg='#000000', text='  ONLY (YYYY-MM-DD) value!  ')  
    try:
        birth = datetime.strptime(birthDate, '%Y-%m-%d').date()
    except ValueError: 
        errorLabel.grid(row=3,column=1)  
          
    else:
        errorLabel.config(bg='#66CDAA',fg='#030303',text="  You enter a correct value :D:D  ")
        errorLabel.grid(row=3,column=1)
        inputBirthDate.delete(0, END)
        birth = datetime.strptime(birthDate, '%Y-%m-%d').date()
        minutes = whatTime('minutes')
        hours = whatTime('hours')
        days = whatTime('days') 
        dateNow = datetime.now().date()


        birthDateLabel = Label(root,bg='#66CDAA', text="Your exact date of birth: {0}".format(birth))
        birthDateLabel.grid(row=3,column=0)

        # Create minutes button
        minutesBatton = Button(root, text='Show in minutes', width=40,bg='#76EEC6',fg='#0000EE', command=lambda: minutes(birth,dateNow))
        minutesBatton.grid(row=4,column=0)
        
        # Create hours botton
        hoursBatton = Button(root, text='Show in hours', width=40,bg='#76EEC6',fg='#0000EE',  command=lambda: hours(birth,dateNow))
        hoursBatton.grid(row=5,column=0)

        # Create days botton
        daysBatton = Button(root, text='Show in days', width=40, bg='#76EEC6',fg='#0000EE', command=lambda: days(birth,dateNow))
        daysBatton.grid(row=6,column=0)
        
# Checks witch button is pressed, and displays the corect value.
def whatTime(chose = 'days'):
    if chose == 'minutes':
        def minutes(birthDate,dateNow):  
            score = dateNow - birthDate
            result = int(score.total_seconds() / 60)
            #Create minutes value lasbel
            myLabel = Label(root,bg='#66CDAA',fg='#0000EE', text='          You exist {0:5d} minuts          '.format(result))           
            return myLabel.grid(row=4,column=1)
        return minutes

    elif chose == 'hours':
        def hours(inputBirthDate,dateNow):
            score = dateNow - inputBirthDate
            result = int(score.total_seconds() /60 /60)
            #Create minutes value lasbel
            myLabel= Label(root,bg='#66CDAA',fg='#0000EE', text='          You exist {0:4d} hours          '.format(result))
            return myLabel.grid(row=5,column=1)
        return hours

    elif chose == 'days':
        def days(inputBirthDate,dateNow):
            score = dateNow - inputBirthDate
            result = int(score.total_seconds() /60 /60 / 24)
            #Create minutes value lasbel
            myLabel= Label(root,bg='#66CDAA',fg='#0000EE', text='          You exist {0:4d} days          '.format(result))
            return myLabel.grid(row=6,column=1)
        return days


# Creating a label widget
nameApp = Label(root,bg='#66CDAA', text="Check how long you exist in the world")
nameApp.grid(row=0,column=1)

 # Info for input
inputInfo = Label(root,bg='#66CDAA', text="Enter you'r date of birth (YYYY-MM-DD)")
inputInfo.grid(row=1, column=0)

# Create input
inputBirthDate = Entry(root,bg='#66CDAA', width=25, borderwidth=5)
inputBirthDate.grid(row=1,column=1)

# Create button adding date
dateBatton = Button(root, text='Add date',bg='#76EEC6',fg='#0000EE', width=20, command=lambda: getBirthDate())
dateBatton.grid(row=1,column=2)



# Showing it onto the screen
root.mainloop()

