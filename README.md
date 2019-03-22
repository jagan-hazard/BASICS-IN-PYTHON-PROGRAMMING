#BASICS-IN-PYTHON-PROGRAMMING
------------------------------

  1. An Introduction
  -------------------
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991.
Python has a design philosophy that emphasizes code readability, notably using significant whitespace.
It provides constructs that enable clear programming on both small and large scales.
It is open source software, well documented and vast community to support you. Python is well used in the following fields,
		
	Machine Learning and AI,
	Developing GUI apps,
	Games and 3D graphics,
	Scientific and Numerics,
	Used as scripting language and go on.

It has vast libraries and packages that will help you in anywhere, few notable libraries in python are,

	Data Science - Numpy,NLTK,Matplotlib,scipy,pandas, etc,
	Web Scrapping - Scrapy, Beautiful soup, etc,
	GUI Development -PyQT,Kivy, etc.
	
  2. Basic Elements in Python
  -----------------------------
    2.1. Variables, Identifiers and Keywords
    ----------------------------------------
  		2.1.1. Variables:
  		-----------------
  		   - Variables are reserved locations in a computer memory to store values.
  		   - we can store data type such as integer,strings,list, etc in a variable.
  		   - variables are stored in stack and their values are stored in heap.
  		   - It does have value,scope,type,scope, etc.
  		   - Python supports Dynamic Typing i.e. Dynamic memory allocation.(Hope you know about stack and heap)

  		    e.g:
  		    		a=10;
  		    		list1=[4,5,3,2,1]
  		    		dic1={1:'jagan',2:'nathan'}
  		    	Here, a,list1,dic1 are variables which holds some values.

  		2.1.2. Identifiers:
  		-------------------
  			- Identifier is the name given to entities like variables,functions,objects etc.
  			- The name of the variable is an identifier.
  			- It doesn't have value,scope,type,scope, etc.

  			Rules for identifier

  				- Case sensitive,
  				- Only Number,letters and underscore is allowed rest of the keywords are not allowed.
  		
  		2.1.3. Keywords:
  		----------------
  			- Keywords are predefined names used as syntax for certain function, loops.
  			- Keywords can't be used in any other ways, otherwise it's a error.

  			e.g:
  					function a:
  						...
  						if ():
  							...
  						...

  				function,if,else,while,for class int,list,tuple,in are some of the keywords in python.

  	2.2. Data Types and Data Structure
  	-----------------------------------
  		The data types in python is given in the below picture. Since python supports dynamic typing, we don't have to
  		initialize any variable. Based on the type of object assigned to the variable, python itself declare the object.

![Screenshot](data_type.png)
		
		Further, based on the mutablility, data types are further classified as following.
			- The Object are able to modify even after the creation, such object is said to be mutable object.
			- The Object are not able to modify once it's created, such object is said to be immutable object.

![Screenshot](adv_data_types.png)

		2.1. Numeric Data types:
		------------------------
			- In python, based on the value of number python will assign the varible and allocate the memory for various numeric data type such as int, float and complex.

			e.g:

					a=4
					b=34244.53423478
					c=4+5j

				Here a is a int, b is a float, c is a complex numeric data types

		2.2. Strings
		-------------
			- String is a sequence of charecters. It is enclosed in single quotes ('') or double quotes("").
			- Python allows Indexing for the srings. Indexing is the process of accessing each charecter or elemet by their index.

			e.g:

					a="earth"
					b="""earth's climate is "hotter" than the sun""" #quotes can be used inside string(when enclosed by triple quotes)
					print(a[2])  #will print letter "r" in variable a

			2.2.1. String manipulation:
			--------------------------
			2.2.1.1. string concordination(+):
			----------------------------------
				- It is the process of adding one string to another.
				-  '+' is used for concordination.

				e.g:
					a="jagan"
					b="nathan"
					c=a+b
					print (c)  # will give "jagannathan"
			2.2.1.2. string Repetition(*):
			-------------------------------
				- It is the process of repeting the strings.
				-  '*' is used for repetition.

				e.g:
					a="jagan"
					b=a*2
					print (b)  # will give "jaganjagan"

			2.2.2. Commonly used methods in strings:
			----------------------------------------
				- Since string is immutable object, most of the methods in string returns a value without altering the original variable.
				- Some of the commonly used methods are,

					2.2.2.1. capitalize():
					----------------------
						- This method will capitalize first letter of the given string.
						-  syntax:    <string_var_name>.capitalize()

						e.g:
							a="we loves python"
							b=a.capitalize()
							print(b)  # gives "We loves python"

					2.2.2.2. upper():
					----------------------
						- This method will convert all the elements into upper case.
						-  syntax:    <string_var_name>.upper()

						e.g:
							a="we loves python"
							b=a.upper()
							print(b)  # gives "WE LOVES PYTHON"

					2.2.2.3. lower():
					----------------------
						- This method will convert all the elements into lower case.
						-  syntax:    <string_var_name>.lower()

						e.g:
							a="We Loves PYTHON"
							b=a.upper()
							print(b)  # gives "we loves python"

					2.2.2.4. title():
					----------------------
						- This method will convert given string into title case.
						-  syntax:    <string_var_name>.title()

						e.g:
							a="We loves pYTHON"
							b=a.upper()
							print(b)  # gives "We Loves Python"

					2.2.2.5. count("string",start_index,ending_index):
					--------------------------------------------------
						- This method will return the count of occurance of a string in the given string provided starting and ending index.

						-  syntax:    <string_var_name>.count("string",start_index,ending_index)

						e.g:
							a="my name is my pYTHON"
							b=a.count("my")        # b=2
							c=a.count("my",0,20)   # c=2
							d=a.count("my",5,20)   # d=1
							print(b,c,d)           # gives 2,2,1

					2.2.2.6. find("string",start_index,ending_index):
					------------------------------------------------
						- This method will return lowest index of a string in the given string provided between starting and ending index.
						- If it doesn't find the index, it will return -1.
						-  syntax:    <string_var_name>.find("string",start_index,ending_index)

						e.g:
							a="my name is my pYTHON"
							b=a.find("my")        # b=0
							c=a.find("my",0,20)   # c=0
							d=a.find("my",5,20)   # d=11
							print(b,c,d)           # gives 0,0,11

					2.2.2.7. index("string",start_index,ending_index):
					------------------------------------------------
						- This method will return lowest index of a string in the given string provided between starting and ending index.
						- If it doesn't find the index, it will throw error.
						-  syntax:    <string_var_name>.index("string",start_index,ending_index)

						e.g:
							a="my name is pYTHON"
							b=a.find("my")        # b=0
							c=a.find("my",0,20)   # c=0
							d=a.find("my",5,20)   # error
							print(b,c,d)           # gives 0,0,(error)


						 


















