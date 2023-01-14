import tkinter as tk

root = tk.Tk()  # Create a Tk object called root

root.title('My Diary')      #Set the name on the root frame
root.geometry('800x600')    #Set the size of the window

root.columnconfigure(1,weight=1)                #This make sure the second column (list box) only uses one row of space, else multiple rows used to show all options
root.rowconfigure(2,weight=1)

subject_label = tk.Label(root, text='Subject: ')            #This is the name of the firts field inside the window
subject_label.grid(sticky=tk.E + tk.W, padx=5,pady=5)       #Decide the location and alignment direction, start with row=0, column=0
                                                            #sticky=tk.E + tk.W means span on the right and left sides, pad 5 on the right and left side of the label

subject_inp = tk.Entry(root)                                #This is the input box next to the subject_label
subject_inp.grid(row=0,column=1, sticky=tk.E + tk.W)        #The input field is on the first row and left of the label (Subject: )

categories = ['Work','Hobbies','Health','Bills']            #This creates the list of options in the categories
cat_label = tk.Label(root, text='Category: ')               #Name of the field on teh second row
cat_label.grid(row=1,column=0, sticky=tk.E + tk.W, padx=5, pady=5)

cat_inp = tk.Listbox(root, height=1)                                #The grid on the right of the label (Categories: ), this is a Listbox, not tk.Entry like previous
                                                                    #height=1 show one row at a time
cat_inp.grid(row=1,column=1, sticky=tk.E + tk.W, padx=5,pady=5)     #The list box is left of the label (Categories: )

for category in categories:                                 #Create a loop to run through the options within the categories list.
    cat_inp.insert(tk.END, category)                        #Use the dpwn arrow key to loop through

message_inp = tk.Text(root)                                 #Input the text in the main box here
message_inp.grid(row=2,column=0,columnspan=2, sticky='nesw')  # sticky on four sides

save_btn = tk.Button(root, text='Save')                         #Create a save button with tk.Button
save_btn.grid(row=3,column=1, sticky=tk.E, ipadx=5, ipady=5)    #sticky=tk.E means put this on the right side

status_bar=tk.Label(root, text='')
status_bar.grid(row=100, column=0, columnspan=2, ipadx=5, ipady=5)

def save():
    subject = subject_inp.get()
    selected = cat_inp.curselection()
    if not selected:
        category = 'Misc'
    else:
        category = categories[selected[0]]

    message = message_inp.get('1.0',tk.END)

    filename = f'{category}-{subject}.txt'
    with open(filename,'w') as fh:
        fh.write(message)

    status_bar.configure(text='File saved')

save_btn.configure(command=save)

root.mainloop()  #This is always the last line that triggers an event



