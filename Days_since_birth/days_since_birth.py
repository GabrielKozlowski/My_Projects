from tkinter import *
from datetime import datetime


root = Tk()
root.title('TIME SINCE BIRTH')

def getBirthDate(birth):

    minutes = whatTime('minutes')
    hours = whatTime('hours')
    days = whatTime('days')

    birth = birth
    dateNow = datetime.now().date()


    # Create minutes button
    minutesBatton = Button(root, text='Show in minutes', width=40, command=lambda: minutes(birth,dateNow))
    minutesBatton.grid(row=3,column=0)
    

    # Create hours botton
    hoursBatton = Button(root, text='Show in hours', width=40,  command=lambda: hours(birth,dateNow))
    hoursBatton.grid(row=4,column=0)

    # Create days botton
    daysBatton = Button(root, text='Show in days', width=40,  command=lambda: days(birth,dateNow))
    daysBatton.grid(row=5,column=0)
    
    
def whatTime(chose = 'days'):
    if chose == 'minutes':
        def minutes(birthDate,dateNow):  
            score = dateNow - birthDate
            result = int(score.total_seconds() / 60)
            myLabel = Label(root, text='You exist {0:5d} minuts'.format(result))
            myLabel.grid(row=3,column=1)
            return myLabel
        return minutes

    elif chose == 'hours':
        def hours(inputBirthDate,dateNow):
            score = dateNow - inputBirthDate
            result = int(score.total_seconds() /60 /60)
            myLabel= Label(root, text='You exist {0:4d} hours'.format(result))
            return myLabel.grid(row=4,column=1)
        return hours

    elif chose == 'days':
        def days(inputBirthDate,dateNow):
            score = dateNow - inputBirthDate
            result = int(score.total_seconds() /60 /60 / 24)
            myLabel= Label(root, text='You exist {0:4d} days'.format(result))
            return myLabel.grid(row=5,column=1)
        return days


# Creating a label widget
nameApp = Label(root, text="Check how long you exist in the world")
nameApp.grid(row=0,column=1)

 # Info for input
inputInfo = Label(root, text="Enter you'r date of birth (YYYY-MM-DD)")
inputInfo.grid(row=1, column=0)

# Create input
inputBirthDate = Entry(root, width=25, borderwidth=5)
inputBirthDate.grid(row=1,column=1)


birthDate = inputBirthDate.get()

birthDate = '1989-1-30'
birth = datetime.strptime(birthDate, '%Y-%m-%d').date()

dateBatton = Button(root, text='Add date', width=20, command=lambda: getBirthDate(birth))
dateBatton.grid(row=1,column=2)



# Showing it onto the screen
root.mainloop()

git pull --rebase
# #-----------------------------------------------------

# minutes = whatTime('minutes')
# hours = whatTime('hours')
# days = whatTime('days')

# inputBirthDate = datetime(2022,10,28)
# dateNow = datetime(2022,11,29)


# print(minutes(datetime(2022,10,28),datetime(2022,11,29)))
# print(hours(inputBirthDate,dateNow))
# print(days(inputBirthDate,dateNow))


# print(days(datetime(1989,1,30),datetime.now()))
# print(days(datetime(1990,8,26),datetime(2023,7,4)))

# #-----------------------------------------------------