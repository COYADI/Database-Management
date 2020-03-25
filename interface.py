import tkinter as tk

root = tk.Tk()

class frontpage(object):
	def __init__(self, master=None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.header = tk.Label(self.page, text='WeBike')
		self.header.grid()

		self.register_button = tk.Button(self.page, text = 'Register', command = self.to_register_page)
		self.register_button.grid()

		self.login_button = tk.Button(self.page, text = 'Login', command = self.to_login_page)
		self.login_button.grid()

	def to_register_page(self):
		self.page.destroy()
		mainpage(self.root)

	def to_login_page(self):
		self.page.destroy()
		loginpage(self.root)
########################################REGISTER####################################################

class mainpage(object):
    def __init__(self, master=None):
        self.root = master 
        self.page = tk.Frame(self.root) 
        self.page.pack()

        self.user_Button = tk.Button(self.page, text='Register User',command=self.to_user_page) 
        self.user_Button.grid() 

        self.bike_Button = tk.Button(self.page, text='Register Bike',command=self.to_bike_page) 
        self.bike_Button.grid() 

        self.employee_Button = tk.Button(self.page, text='Register Employee',command=self.to_employee_page) 
        self.employee_Button.grid() 

        self.return_button = tk.Button(self.page, text = 'Back', command = self.back_to_top)
        self.return_button.grid()


    def to_user_page(self):
        self.page.destroy()
        Userpage(self.root)

    def to_bike_page(self):
        self.page.destroy()
        Bikepage(self.root)

    def to_employee_page(self):
        self.page.destroy()
        Employeepage(self.root)

    def back_to_top(self):
        self.page.destroy()
        frontpage(self.root)
    
  
class Userpage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()

        self.header = tk.Label(self.page, text='Register User')
        self.header.grid(row = 0)

        self.name_frame = tk.Label(self.page, text='Name: ')
        self.name_frame.grid(row = 1, column = 0)
        self.name_entry = tk.Entry(self.page)
        self.name_entry.grid(row = 1, column = 1)

        self.id_frame = tk.Label(self.page, text='Student ID: ')
        self.id_frame.grid(row = 2, column = 0)
        self.id_entry = tk.Entry(self.page)
        self.id_entry.grid(row = 2, column = 1)

        self.register_button = tk.Button(self.page, text = 'register', command = self.get_info)
        self.register_button.grid(row = 3, column = 1)
        self.Button = tk.Button(self.page, text='Go Back',command=self.mainpage) 
        self.Button.grid(row = 3, column = 0) 

        self.output_label = tk.Label(self.page)
        self.output_label.grid(row = 4, column = 0)
        
    def mainpage(self):
        self.page.destroy()
        mainpage(self.root)

    def get_info(self):
    	if not self.id_entry.get():
    		message = 'Student ID missed!'
    		self.output_label.configure(text = message)
    	else:
	    	name = self.name_entry.get()
	    	studentid = self.id_entry.get()
	    	####user_create(name, studentid)
	    	self.name_entry.delete(0, 'end')
	    	self.id_entry.delete(0, 'end')
	    	message = 'Student ' + name + ' successfully registered!'
	    	self.output_label.configure(text = message)

#############################################################

class Bikepage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()

        self.bike_id_frame = tk.Label(self.page, text='Bike ID: ')
        self.bike_id_frame.grid(row = 1, column = 0)
        self.bike_id_entry = tk.Entry(self.page)
        self.bike_id_entry.grid(row = 1, column = 1)

        self.lock_id_frame = tk.Label(self.page, text='Lock ID: ')
        self.lock_id_frame.grid(row = 2, column = 0)
        self.lock_id_entry = tk.Entry(self.page)
        self.lock_id_entry.grid(row = 2, column = 1)

        self.lock_passwd_frame = tk.Label(self.page, text='Lock Password: ')
        self.lock_passwd_frame.grid(row = 3, column = 0)
        self.lock_passwd_entry = tk.Entry(self.page)
        self.lock_passwd_entry.grid(row = 3, column = 1)

        self.student_id_frame = tk.Label(self.page, text='Student ID: ')
        self.student_id_frame.grid(row = 4, column = 0)
        self.student_id_entry = tk.Entry(self.page)
        self.student_id_entry.grid(row = 4, column = 1)

        self.register_button = tk.Button(self.page, text = 'register', command = self.get_info)
        self.register_button.grid(row = 5, column = 1)
        self.Button = tk.Button(self.page, text='Go Back',command=self.mainpage) 
        self.Button.grid(row = 5, column = 0) 

        self.output_label = tk.Label(self.page)
        self.output_label.grid(row = 6, column = 0)

    def mainpage(self):
        self.page.destroy()
        mainpage(self.root)  

    def get_info(self):
    	if not self.student_id_entry.get():
    		message = 'Student ID missed!'
    		self.output_label.configure(text = message)
    	elif not self.bike_id_entry.get():
    		message = 'Bike ID missed!'
    		self.output_label.configure(text = message)
    	else:
	    	bike_id = self.bike_id_entry.get()
	    	lock_id = self.lock_id_entry.get()
	    	lock_passwd = self.lock_passwd_entry.get()
	    	student_id = self.student_id_entry.get()
	    	####bike_create(bike_id, lock_id, lock_passwd, student_id)
	    	self.bike_id_entry.delete(0, 'end')
	    	self.lock_id_entry.delete(0, 'end')
	    	self.lock_passwd_entry.delete(0, 'end')
	    	self.student_id_entry.delete(0, 'end')
	    	message = 'Bike ' + bike_id + ' of ' + student_id + ' successfully registered!'
	    	self.output_label.configure(text = message)

#############################################################

class Employeepage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()

        self.header = tk.Label(self.page, text='Register User')
        self.header.grid(row = 0)

        self.name_frame = tk.Label(self.page, text='Name: ')
        self.name_frame.grid(row = 1, column = 0)
        self.name_entry = tk.Entry(self.page)
        self.name_entry.grid(row = 1, column = 1)

        self.ssn_frame = tk.Label(self.page, text='SSN: ')
        self.ssn_frame.grid(row = 2, column = 0)
        self.ssn_entry = tk.Entry(self.page)
        self.ssn_entry.grid(row = 2, column = 1)

        self.register_button = tk.Button(self.page, text = 'register', command = self.get_info)
        self.register_button.grid(row = 3, column = 1)
        self.Button = tk.Button(self.page, text='Go Back',command=self.mainpage) 
        self.Button.grid(row = 3, column = 0) 

        self.output_label = tk.Label(self.page)
        self.output_label.grid(row = 4, column = 0)
        
    def mainpage(self):
        self.page.destroy()
        mainpage(self.root)   

    def get_info(self):
    	if not self.ssn_entry.get():
    		message = 'Employee SSN missed!'
    		self.output_label.configure(text = message)
    	else:
	    	name = self.name_entry.get()
	    	SSN = self.ssn_entry.get()
	    	####empolyee_create(name, SSN)
	    	self.name_entry.delete(0, 'end')
	    	self.ssn_entry.delete(0, 'end')
	    	message = 'Employee ' + name + ' successfully registered!'
	    	self.output_label.configure(text = message)  


#####################################LOGIN#########################################

class loginpage(object):
	def __init__(self, master = None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.user_login_button = tk.Button(self.page, text = 'User Login', command = self.to_login_user)
		self.user_login_button.grid()

		self.employee_login_button = tk.Button(self.page, text = 'Employee Login', command = self.to_login_employee)
		self.employee_login_button.grid()

		self.back_button = tk.Button(self.page, text = 'Go Back', command = self.go_to_top)
		self.back_button.grid()

	def to_login_user(self):
		self.page.destroy()
		userloginpage(self.root)

	def to_login_employee(self):
		self.page.destroy()
		employeeloginpage(self.root)

	def go_to_top(self):
		self.page.destroy()
		frontpage(self.root)

####################################################################################################################

class userloginpage(object):
	def __init__(self, master = None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.name_frame = tk.Label(self.page, text='Name: ')
		self.name_frame.grid(row = 1, column = 0)
		self.name_entry = tk.Entry(self.page)
		self.name_entry.grid(row = 1, column = 1)

		self.id_frame = tk.Label(self.page, text='Student ID: ')
		self.id_frame.grid(row = 2, column = 0)
		self.id_entry = tk.Entry(self.page)
		self.id_entry.grid(row = 2, column = 1)

		self.login_button = tk.Button(self.page, text = 'Login', command = self.login)
		self.login_button.grid(row = 3)

		self.back_button = tk.Button(self.page, text = 'Go Back', command = self.to_login_page)
		self.back_button.grid(row = 4)

		self.message_label = tk.Label(self.page)
		self.message_label.grid(row = 5)

	def to_login_page(self):
		self.page.destroy()
		loginpage(self.root)

	def login(self):
		if not self.id_entry.get():
			message = 'Student ID missed!'
			self.message_label.configure(text = message)
		else:
			name = self.name_entry.get()
			studentid = self.id_entry.get()
			####SEARCH FOR ID IN DATA AND LOGIN

			##if LOGIN RETURN LOGIN
			self.page.destroy()
			useroperatingpage(self.root)
			##else RETURN ERROR


####################################################################################################################

class employeeloginpage(object):
	def __init__(self, master = None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.name_frame = tk.Label(self.page, text='Name: ')
		self.name_frame.grid(row = 1, column = 0)
		self.name_entry = tk.Entry(self.page)
		self.name_entry.grid(row = 1, column = 1)

		self.SSN_frame = tk.Label(self.page, text='SSN: ')
		self.SSN_frame.grid(row = 2, column = 0)
		self.SSN_entry = tk.Entry(self.page)
		self.SSN_entry.grid(row = 2, column = 1)

		self.login_button = tk.Button(self.page, text = 'Login', command = self.login)
		self.login_button.grid(row = 3)

		self.back_button = tk.Button(self.page, text = 'Go Back', command = self.to_login_page)
		self.back_button.grid(row = 4)

		self.message_label = tk.Label(self.page)
		self.message_label.grid(row = 5)

	def to_login_page(self):
		self.page.destroy()
		loginpage(self.root)

	def login(self):
		if not self.SSN_entry.get():
			message = 'SSN missed!'
			self.message_label.configure(text = message)
		else:
			name = self.name_entry.get()
			SSN = self.SSN_entry.get()
			####SEARCH FOR SSN IN DATA AND LOGIN

			##if LOGIN RETURN LOGIN
			self.page.destroy()
			employeeoperatingpage(self.root)
			##else RETURN ERROR

######################################USER OPERATING PAGE##################################
class useroperatingpage(object):
	"""docstring for useroperatingpage"""
	def __init__(self, master = None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.lend_button = tk.Button(self.page, text = 'Lend', command = self.lendbike)
		self.lend_button.grid(row = 0)

		self.reserve_button = tk.Button(self.page, text = 'Reserve', command = self.reservebike)
		self.register_button.grid(row = 1)

		self.message_label = tk.Label(self.page)
		self.message_label.grid(row = 2)

	def lendbike(self):
		###lend a bike and return lend message###
		#message = ~~~~
		#self.message_label.configure(text = message)

	def reservebike(self):
		self.page.destroy()
		reservepage(self.root)

class reservepage(object):
	"""docstring for reservepage"""
	def __init__(self, master = None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.id_frame = tk.Label(self.page, text='Student ID: ')
		self.id_frame.grid(row = 1, column = 0)
		self.id_entry = tk.Entry(self.page)
		self.id_entry.grid(row = 1, column = 1)

		self.bike_id_frame = tk.Label(self.page, text='Bike ID: ')
		self.bike_id_frame.grid(row = 2, column = 0)
		self.bike_id_entry = tk.Entry(self.page)
		self.bike_id_entry.grid(row = 2, column = 1)

		self.time_frame = tk.Label(self.page, text='Time: ')
		self.time_frame.grid(row = 3, column = 0)
		self.time_entry = tk.Entry(self.page)
		self.time_entry.grid(row = 3, column = 1)

		self.back_button = tk.Button(self.page, text = 'Back', command = self.go_back)
		self.back_button.grid(row = 4, column = 0)

		self.reserve_button = tk.Button(self.page, text = 'Reserve', command = self.reserve)
		self.reserve_button.grid(row = 4, column = 1)

		self.message_label = tk.Label(self.page)
		self.message_label.grid(row = 5)

	def go_back(self):
		self.page.destroy()
		useroperatingpage(self.root)

	def reserve(self):
		if not id_entry.get() or not bike_id_entry.get():
			message = 'Missed IDs'
			self.message_label.configure(text = message)
		else:
			###reserve and return message
			#message = ~~~
			#self.message_label.configure(text = message)
		

#################################EMPLOYEE OPERATING PAGE######################################
class employeeoperatingpage(object):
	"""docstring for employeeoperatingpage"""
	def __init__(self, master = None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.change_data_button = tk.Button(self.page, text = 'Change Bike Data', command = self.change_data)
		self.change_data_button.grid(row = 0)

		self.add_fix_button = tk.Button(self.page, text = 'Add fix event', command = self.add_fix)
		self.add_fix_button.grid(row = 1)

		self.add_violate_button = tk.Button(self.page, text = 'Add violate event', command = self.add_violate)
		self.add_violate_button.grid(row = 2)

	def change_data(self):
		self.page.destroy()
		changedatapage(self.root)

	def add_fix(self):
		self.page.destroy()
		addfixpage(self.root)

	def add_violate(self):
		self.page.destroy()
		addviolatepage(self.root)


class changedatapage(object):
	"""docstring for changedatapage"""
	def __init__(self, master = None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.bike_id_frame = tk.Label(self.page, text='Bike ID: ')
		self.bike_id_frame.grid(row = 1, column = 0)
		self.bike_id_entry = tk.Entry(self.page)
		self.bike_id_entry.grid(row = 1, column = 1)

		self.rate_frame = tk.Label(self.page, text = 'Earning rate to change')
		self.rate_frame.grid(row = 2, column = 0)
		self.rate_entry = tk.Entry(self.page)
		self.rate_entry.grid(row = 2, column = 1)

		self.cost_frame = tk.Label(self.page, text = 'Cost to change')
		self.cost_frame.grid(row = 3, column = 0)
		self.cost_entry = tk.Entry(self.page)
		self.cost_entry.grid(row = 3, column = 1)

		self.back_button = tk.Button(self.page, text = 'Back', command = self.go_back)
		self.back_button.grid(row = 4, column = 0)

		self.change_button = tk.Button(self.page, text = 'Change', command = self.change)
		self.change_button.grid(row = 4, column = 1)

		self.message_label = tk.Label(self.page)
		self.message_label.grid(row = 5)

	def go_back(self):
		self.page.destroy()
		employeeoperatingpage(self.root)

	def change(self):
		if not self.bike_id_entry.get():
			message = 'Bike ID Missed!'
			self.message_label.configure(text = message)

		else:
			###change changed data###
			self.bike_id_entry.delete(0, 'end')
			self.cost_entry.delete(0, 'end')
			self.rate_entry.delete(0, 'end')
			message = 'Successfully Changed!'
			self.message_label.configure(text = message)


class addfixpage(object):
	def __init__(self, master = None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.bike_id_frame = tk.Label(self.page, text='Bike ID: ')
		self.bike_id_frame.grid(row = 1, column = 0)
		self.bike_id_entry = tk.Entry(self.page)
		self.bike_id_entry.grid(row = 1, column = 1)

		self.date_frame = tk.Label(self.page, text='Date: ')
		self.date_frame.grid(row = 2, column = 0)
		self.date_entry = tk.Entry(self.page)
		self.date_entry.grid(row = 2, column = 1)

		self.content_frame = tk.Label(self.page, text='Content: ')
		self.content_frame.grid(row = 3, column = 0)
		self.content_entry = tk.Entry(self.page)
		self.content_entry.grid(row = 3, column = 1)

		self.back_button = tk.Button(self.page, text = 'Back', command = self.go_back)
		self.back_button.grid(row = 4, column = 0)

		self.change_button = tk.Button(self.page, text = 'Add', command = self.add)
		self.change_button.grid(row = 4, column = 1)

		self.message_label = tk.Label(self.page)
		self.message_label.grid(row = 5)

	def go_back(self):
		self.page.destroy()
		employeeoperatingpage(self.root)

	def add(self):
		if not self.bike_id_entry.get():
			message = 'Bike ID Missed!'
			self.message_label.configure(text = message)

		else:
			###add changed data###
			self.bike_id_entry.delete(0, 'end')
			self.date_entry.delete(0, 'end')
			self.content_entry.delete(0, 'end')
			message = 'Successfully Added!'
			self.message_label.configure(text = message)


class addviolatepage(object):
	def __init__(self, master = None):
		self.root = master
		self.page = tk.Frame(self.root)
		self.page.pack()

		self.id_frame = tk.Label(self.page, text='Student ID: ')
		self.id_frame.grid(row = 1, column = 0)
		self.id_entry = tk.Entry(self.page)
		self.id_entry.grid(row = 1, column = 1)

		self.date_frame = tk.Label(self.page, text='Date: ')
		self.date_frame.grid(row = 2, column = 0)
		self.date_entry = tk.Entry(self.page)
		self.date_entry.grid(row = 2, column = 1)

		self.time_frame = tk.Label(self.page, text='Time: ')
		self.time_frame.grid(row = 3, column = 0)
		self.time_entry = tk.Entry(self.page)
		self.time_entry.grid(row = 3, column = 1)
		
		self.fine_frame = tk.Label(self.page, text='Fine: ')
		self.fine_frame.grid(row = 4, column = 0)
		self.fine_entry = tk.Entry(self.page)
		self.fine_entry.grid(row = 4, column = 1)

		self.back_button = tk.Button(self.page, text = 'Back', command = self.go_back)
		self.back_button.grid(row = 5, column = 0)

		self.change_button = tk.Button(self.page, text = 'Add', command = self.add)
		self.change_button.grid(row = 5, column = 1)

		self.message_label = tk.Label(self.page)
		self.message_label.grid(row = 6)

	def go_back(self):
		self.page.destroy()
		employeeoperatingpage(self.root)

	def add(self):
		if not self.id_entry.get():
			message = 'Student ID Missed!'
			self.message_label.configure(text = message)

		else:
			###add changed data###
			self.id_entry.delete(0, 'end')
			self.date_entry.delete(0, 'end')
			self.time_entry.delete(0, 'end')
			self.fine_entry.delete(0, 'end')
			message = 'Successfully Added!'
			self.message_label.configure(text = message)


								

        
frontpage(root)
root.mainloop()     