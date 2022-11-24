# GCF

A simple Python function to take the GCF(greatest common factor) of any number of numbers. Useful as a module to plug into other programs and includes an extra function for user input of numbers that's more useful on CLI programs.

gcf.py contains two functions. The function getGCF() is useful for any number of programs as a back end function to calculate the GCF of any number of integers sent to it in the form of a list[] data type. The enterNumbers() function is more useful in CLI programs unless you can write a bot to interact with it, but with any GUI application, you might have to write your own algorithms to handle user input of numbers and convert them into a list. The numbers can be passed as strings which the getGCF() function will automatically convert into an integer. The getGCF() function will not accept floating point numbers or strings that contain periods or any non-digit symbols. enterNumbers() will allow the user to enter any number of inputs though, converting each input into a string element in a list before returning the list. A regular expression is used for the user to exit the otherwise eternal loop of number entry.

get_gcf.py makes use of both functions in gcf.py, showcasing how both functions may be used practically. It's simply a runnable application to find the GCF of any list of integers in a simple CLI or SHELL interface. Nothing too fancy, but will give you the GCF. You might prefer to use gcf.py as an extension in your own application.

fraction_simplify is a program that only takes two numbers, a numerator and denominator, and simplifies the fraction into the most basic integer format using the getGCF() function from gcf.py. Another simple application of gcf.py.
