# What is error handling?
Error handling is the process of anticipating, detecting, and responding to errors that occur while a program is running. The goal is to make sure that program can handle unexpected situations gracefully, rather than crashing or producing incorrect results.
## Why it’s important?
Programs often deal with unpredictable situations –like missing files, invalid user input, or failed network connections. Error handling helps your program stay stable and inform the user or developer about what went wrong.
## 1.Try –except block
A try –except block is a way to handle errors (also called exceptions) in many programming languages –most commonly used in python.
-	**Try** a piece of code that might cause an error.
-	**Except: ** catch and respond to the error if it happens, without crashing the program.
## 2.The finally block in error handling is used to define code that must run no matter what –whether an exception occurs or not.
It’s commonly used for cleanup tasks, like
-	Closing files
-	Releasing resources
-	Closing database connections
-	Logging final messages
## 3.Else –clause
The else clause in a try –except block is often underused but very useful for clarity and control.
-	The else block runs only if the try block does not raise an exception.
-	If an exception is raised in the try, the else block is skipped.
-	It helps separate the “risky” code from the “safe to run if all went well” code.
## 3.Raise Exception Error
You can manually raise exceptions in python using the raise statement.
This is useful when you want to signal that something went wrong-for example, when input is invalid or a condition isn’t met.

**Syntax**

			raise ExceptionType(“Error message”)
			
## 4.Custom Exceptions
A custom exception is a user –defined error type that you create by subclassing python’s built –in Exception class (or one of its subclasses). This lets you define specific, meaningful errors that make your code cleaner and easier.

**Syntax**
class MyCustomError (Exception)
					pass
raise MyCustomError(“Something went wrong”)

## 5.Common python Errors

There are many common built in python Errors.

**1. Syntax Error**
Occurs when python can’t understand your code (bad syntax).

Example: 
				If true
					Print(“Hello”)
Fix: Add the colon:

 **2.Indendation Error**
 
It happens when indentation is incorrect.

Example:
				def greet():
					print(“Hello”)
**3.NameError**

Happens when you try to use a variable that doesn’t exist.

Example:
					print(score)

**4.Type Error**

Occurs when you use a function or operation on the wrong data type.

				print(“Age “ + 25)

**5.Debugging**

Debugging is the process of finding and fixing errors(bugs) in your code. Python provides several tools and techniques for debugging, ranging from simple print statements to advanced interactive debugging.

**Common Debugging Techniques in python**

**Print statement**

Use print() to check variables values or flow of execution.

**Using pdb (python Debugger)**

Python’s built in interactive debugger. It allows you to pause execution, inspect variables, and step through code line by line.

**Using IDE Debugger**

Graphical debuggers that let you set break points, step through code, inspect variables, and more.

**Using logging Modue**

Instead of print(), use the logging for better  control over output(info, warning, error,etc.)

**Writing Unit Test**

Use unittest or pytest to test individual parts of your code and catch errors early.

**Use asserts statements**

Example:
			assert x != 0, “x should not be zero”
**Static Code Analysis Tool**
Use tools like:
Flake8, pylint: Linting for code quality and style issues.
mypy: Type checking


			




