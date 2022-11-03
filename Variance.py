import statistics
import math
A1= {12,20,30,40,50} #Enter data in A1
A2 = {34,45,35,64,23,43} #Enter data in A2
n=0
m=0
z=0
y=0
sum1=0
sum2=0
for chr in A1 :
    n=n+1
    sum1=sum1+chr
for chr1 in A2 :
    m=m+1
    sum2=sum2+chr1
X1=(sum1)/n
X2=(sum2)/m
CM=((X1*n)+(X2*m))/(n+m)
print("Combined mean is",CM)
print("Standard deviation of A1 is :",statistics.stdev(A1))
print("Standard deviation of A2 is :",statistics.stdev(A2))
std1=statistics.stdev(A1)
std2=statistics.stdev(A2)
d1_square=((X1-CM) *(X1-CM))
d2_square=((X2-CM) *(X2-CM))

comb_var = (n*(std1 +d1_square)+m*(std2 + d2_square))/n+m
coeff_var1=X1/std1
coeff_var2=X2/std2
print("Combined variance is :",comb_var)
print("Coefficient of Variance of A1 ",coeff_var1)
print("Coefficient of Variance of A2",coeff_var2)