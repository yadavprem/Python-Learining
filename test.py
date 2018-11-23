# # change this code
# mystring = "hello"
# myfloat = 10.0
# myint = 20

# # testing code
# if mystring == "hello":
    # print("String: %s" % mystring)
# if isinstance(myfloat, float) and myfloat != 20.0:
    # print("Float: %f" % myfloat)
# if isinstance(myint, int) and myint != 30:
    # print("Integer: %d" % myint)
	
	
def a_void_function():
    a = 1
    b = 2
    c = a + b

x = a_void_function()
print(x)


def improper_return_function(a):
	if (a % 2) == 0:
		return True
	else:
		return False

x = improper_return_function(2)
print(x)


if True:
	print "Answer"
	print "True"
else:
	print "Answer"
	print "False"