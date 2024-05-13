import matplotlib.pyplot as plt
import subprocess
import np

# execute main_shell.exe to get value of pi for n
N=[]
PI=[]
for n in [i for i in range(2, 25)]:
    n = int(n)
    cli = "main_shell.exe " + str(2**n)
    pi = subprocess.check_output(cli, shell=True)
    pi = float(pi)
    # print(pi)
    N.append(n)
    PI.append(pi)
    # line plot of pi vs n
plt.plot(N, PI,'o-')
plt.xlabel("no of samples in log scale")
plt.ylabel("estimated pi")
plt.title("estimated pi vs no of samples in log scale")
plt.savefig("plots.pdf")
# plt.show()
