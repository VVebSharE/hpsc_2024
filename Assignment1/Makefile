output.txt: monte.exe
	./monte.exe > output.txt

monte.exe: monte_carlo.f90 point_module
	gfortran -o monte.exe monte_carlo.f90 test_pi.f90 monte_carlo_pi.f90

main_shell.exe: main_shell.f90 test_pi.f90 monte_carlo_pi.f90 point_module
	gfortran main_shell.f90 test_pi.f90 monte_carlo_pi.f90 -o main_shell.exe

point_module: monte_carlo_pi.f90
	gfortran -c monte_carlo_pi.f90

plots: main_shell.exe
	python plot_python.py

.PHONEY: clean clobber help

clean:
	rm -rf *.exe *.mod *.o output.txt 

clobber: clean
	rm -rf *.pdf

help:
	@echo "The following targets are available and useful:"
	@echo -e "\n output.txt:        Run the monte_carlo program and save the output to output.txt"
	@echo -e "\n main_shell.exe:    Compile the main_shell program"
	@echo -e "\n plots:             Run the main_shell program and plot the results"
	@echo -e "\n clean:             Remove all compiled files and output.txt"
	@echo -e "\n clobber:           Remove all compiled files, output.txt, and plots"
	@echo -e "\n help:              Print this message"
