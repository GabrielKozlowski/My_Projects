from tkinter import *
from datetime import datetime


root = Tk()
root.title('TIME SINCE BIRTH')
root.configure(bg='#66CDAA')

def getBirthDate():
    birthDate = '1000-10-10 10:10:10'
    #Save input in to variable
    birthDate = inputBirthDate.get()
    #Save label in to variable
    errorLabel = Label(root,bg='#CD3333',fg='#000000', text='ONLY (YYYY-MM-DD H:M:S) value!')  
    #Check if is good valiue input
    try:
        birth = datetime.strptime(birthDate, '%Y-%m-%d %H:%M:%S')
    #Create errorlabel with error text
    except ValueError: 
        errorLabel.grid(row=3,column=1)  
          
    else:
        #Change errorlabel text 
        errorLabel.config(bg='#66CDAA',fg='#030303',text="    You enter a correct value :D:D    ")
        errorLabel.grid(row=3,column=1)
        #Clean input value
        inputBirthDate.delete(0, END)
        #Convert input value to datatime and save to variable
        birth = datetime.strptime(birthDate, '%Y-%m-%d %H:%M:%S')
        #Create variables of def with value
        minutes = whatTime('minutes')
        hours = whatTime('hours')
        days = whatTime('days') 
        #Create variable with date today
        dateNow = datetime.now()

        #Create label with added birth date
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
            #Calculates two dates  
            score = dateNow - birthDate
            #Convert value to seconds and next to minutes
            result = int(score.total_seconds() / 60)
            #Create minutes value label
            myLabel = Label(root,bg='#66CDAA',fg='#0000EE', text='          You exist {0:5d} minuts          '.format(result))           
            return myLabel.grid(row=4,column=1)
        return minutes

    elif chose == 'hours':
        def hours(inputBirthDate,dateNow):
            #Calculates two dates 
            score = dateNow - inputBirthDate
            #Convert value to seconds and next hours
            result = int(score.total_seconds() /60 /60)
            #Create minutes value label
            myLabel= Label(root,bg='#66CDAA',fg='#0000EE', text='          You exist {0:4d} hours          '.format(result))
            return myLabel.grid(row=5,column=1)
        return hours

    elif chose == 'days':
        def days(inputBirthDate,dateNow):
            #Calculates two dates
            score = dateNow - inputBirthDate
            #Convert value to seconds and next days
            result = int(score.total_seconds() /60 /60 / 24)
            #Create minutes value label
            myLabel= Label(root,bg='#66CDAA',fg='#0000EE', text='          You exist {0:4d} days          '.format(result))
            return myLabel.grid(row=6,column=1)
        return days

# Creating a label widget
nameApp = Label(root,bg='#66CDAA', text="Check how long you exist in the world")
nameApp.grid(row=0,column=1)

 # Info for input
inputInfo = Label(root,bg='#66CDAA', text="Enter you'r date of birth (YYYY-MM-DD H:M:S)")
inputInfo.grid(row=1, column=0)

# Create input
inputBirthDate = Entry(root,bg='#66CDAA', width=25, borderwidth=5)
inputBirthDate.grid(row=1,column=1)

# Create button adding date
dateBatton = Button(root, text='Add date',bg='#76EEC6',fg='#0000EE', width=20, command=lambda: getBirthDate())
dateBatton.grid(row=1,column=2)

# Showing it onto the screen
root.mainloop()

