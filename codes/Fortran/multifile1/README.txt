
See the Makefiles section of the notes for discussion of these files.

What is Use of clean: to remove all the temperaory compiled files(like .o files in this case)
Use of Clobber: clean + remove the created output also so that project goes to initial unbuild state

How to run a differnt makefile not default : make -f filename action

while runing makefile command each command is prited in the ternimal, but this functionality may not be required at echo so prefix this with @

can run all the file with specific patters with %
eg.
    %.o : %.f90
        gfortran -c $<
$< will replace by the value of % in the make command


we can define variable in makefile like
    varName = file1.ext file2.ext 
and use it as $(varName) , now varName will be replaced by file1.ext file2.ext


also consider this thing
    SOURCES = $(wildcard *.f90)  
    OBJECTS = $(subst .f90,.o,$(SOURCES))