import scipy

import math
import statsmodels

'''make "car prompt" to ask to put in data, even beforehand like data to then convert to mean etc
Input data to variables and booleans to keep track of which variables are used
then once finished, using if depending on false conditions, run test'''

print('''Welcome to the Statistical Inference Doer (SID).
Sid will automatically choose and compute the appropriate
statistical inference test.

All you need to do is input the data:
such as population mean, population SD
sample mean, sample SD, sample size

Type any of the phrases above to enter its data
and when done, enter "done"
''')

data = ""
pm = False
psd = False
sm = False
ssd = False
ss = False

while data != "done":
    data = input("> ").lower()
    if data == "population mean":
        population_mean = float(input("Population Mean: "))
        pm = True
    elif data == "population sd":
        population_sd = float(input("Population SD: "))
        psd = True
    elif data == "sample mean":
        sample_mean = float(input("Sample Mean: "))
        sm = True
    elif data == "sample sd":
        sample_sd = float(input("Sample SD: "))
        ssd = True
    elif data == "sample size":
        sample_size = float(input("Sample Size: "))
        ss = True
    elif data == "done":
        break

'''how to make loop to print all values if true
if pm:
    print(population_mean)'''



#making scenarios depending on unused variables
#can make modules to later import

#1 Sample Z; sample SD not used
if ssd == False:
    print("Performing 1 Sample Z Test...")
    Z = (sample_mean - population_mean) / (population_sd / math.sqrt(sample_size))
    if abs(Z) >= 1.96:
        print(f"""The Z is {Z}, which is outside the Z score bounds of +-1.96
therefore, we reject the null hypothesis""")
    elif abs(Z) < 1.96:
        print(f"""The Z is {Z} which lies inside the Z score bounds of +-1.96;
therefore, we accept the null hypothesis""")
#1 Sample T; pop SD not used
elif psd == False:
    print("Performing 1 Sample T Test...")
    degrees_of_freedom = sample_size - 1
    #"t table" -> critical value
    critical_value = scipy.stats.t.ppf(q=.975, df = degrees_of_freedom)
    print(f"Critical Value = {critical_value}")
    #t value
    t_value = (sample_mean - population_mean) / (sample_sd / math.sqrt(sample_size))
    print(f"T Value = {t_value}")
    if abs(t_value) >= critical_value:
        print(f"""The data's t-value of {t_value}
is outside the bounds of the critical value of {critical_value} and {-critical_value}.
Therefore, there IS EVIDENCE the experiment had a statistically significant affect.""")
    elif abs(t_value) < critical_value:
        print(f"""The data's t-value of {t_value}
is inside the bounds of the critical value of {critical_value} and {-critical_value}.
Therefore, there is NO EVIDENCE the experiment had a statistically significant affect.""")


#make setting to choose alpha level
#also exception if input does not match set wording