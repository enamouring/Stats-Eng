# -*- coding: utf-8 -*-
"""Audrey_24 Lab 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ae_MJvJ_wx0MMyihJ3nu4i0MimvPAFWM
"""

import numpy as np
import matplotlib.pyplot as plt #importing mathematical libraries

numbers= np.array([1,2,2,3,3,3,4,4,4,4]) #manually create an array called 'numbers' for the following (randomized) computations

plt.hist(numbers,100); #plotting the amount of numbers in a histogram in 100 bins ie. 1 has 1 occurrence 1-[1], 2-[2],...

"""# PRNG"""

x = 0.12345          # seed value
X = np.zeros(5000,)  # initialize an array of zeros (5000 spots for data)

for i in range(X.shape[0]): #loop -> 5000 iterates
    x = 3*x % 1      # update x (assignment operator '=') and store the value in X (mod 1)
    X[i] = x

plt.plot(X, '.')     # plot the values in X

#cd=change directory
#terminal on mac
#cmdspace on windows
#equality operator '=='

plt.hist(X); #no preferred numbers; uniform distribution

def coin():
    return 2*(np.random.random() > 0.5) - 1 #simulating flipping a coin

coin() #left=-1, right=1

x = 0
x + coin()

x = 0

for i in range(3): #run the code 3 times
    x = x + coin()

x

x = 0

for i in range(100): #flipping 100 times and compliling the total result
    x = x + coin()
print(x) #added this line to showcase x after the code has ran

x

M = 10000 #simulations
N = 100 #number of flips per simulation

X = np.zeros(M,) #array storage

for j in range(M):

    x = 0

    for i in range(N):
        x = x + coin()

    X[j] = x

plt.hist(X,100); #plotting data from previous code

#mimics plinko board, normal (bell) curve

"""# Bonus: Explain Pascal's Triangle"""

P = np.zeros((12,18)) #12 by 18 zeros (row by column)

P[0,5]=1 #1,6 position equals 1

for i in range(1,P.shape[0]): #rows

    for j in range(1,P.shape[1]-1): #nested loop for colums

        P[i,j] = P[i-1,j-1]+P[i-1,j] #algorithm for Pascal's triangle (adding element above and above left to produce a new sum)

print(P[:,5:])

"""# Normal Distribution"""

# Define the parameters for the normal distribution
mean = 0  # Mean (mu) of the distribution
std_dev = 0.1  # Standard deviation (sigma) of the distribution

# Generate 100000 data points following a normal distribution with the specified mean and standard deviation
sample_size = 100000
data_points = np.random.normal(mean, std_dev, sample_size)

# Plot the histogram of the data points
bins_number = 30  # Number of bins for the histogram
hist_count, x, ignored = plt.hist(data_points, bins_number, density=True)

# Plot the probability density function of the normal distribution
normal_dist_curve = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * std_dev ** 2))
plt.plot(x, normal_dist_curve, linewidth=2, color='r')

# Set the title and labels for the plot
plt.title('Normal Distribution Visualization')
plt.xlabel('Value')
plt.ylabel('Probability Density')

# Display the plot
plt.show()

x = np.array([1,2,3,4]) #creates array

np.sum(x) #adds all array values

x.shape[0]

np.sum(x)/x.shape[0] #calculates the mean

def mean(x):
    return np.sum(x)/x.shape[0] #creates a function for the mean

mean(x)

x #recalls array

x - mean(x) #subtracts the mean from the array

(x - mean(x))**2 #squares the previous result

def var(x): #takes the mean of the previous result (variance)
    return mean((x - mean(x))**2)

def std(x): #standard deviation
    return np.sqrt(var(x))

mean(x) #calculates the mean of the original array

var(x) #calculates the variance

std(x) #calculates standard deviation



"""### Uniform Random Numbers"""

X = np.random.random(50000,)

X

plt.hist(X,100);

np.random.random()

r = np.random.random() #generates random number

r #recalls

r = np.random.randint(1,10) #integer between 1 and 9

r

np.random.randn() #generates a number from the standard normal distribution

numbers  = np.random.randn(2,4)

numbers.shape #outputs the shape (2x4)

numbers = numbers.reshape(-1) #becomes 1 less dimension (2-D->1-D)

numbers.shape

numbers= np.array([1,2,2,3,3,3,4,4,4,4]) #array called numbers

plt.hist(numbers,100); #array over 100 bins

numbers = np.random.randn(100000,) #takes new array from standard normal distribution
plt.hist(numbers,100); #plots in 100 bins

numbers = np.random.rand(1000000,) #larger data set over 100 bins
plt.hist(numbers,100);

np.random.seed(12345) #histogram, scatter plot, path, 2D
data = np.random.randn(2, 100)

plt.figure(1, figsize=(9, 9)) #creates room for multiple plots
#all 2x2, 3rd coordinate represents subplot
plt.subplot(2,2,1)
plt.hist(data[0]) #histogram

plt.subplot(2,2,2)
plt.scatter(data[0], data[1]) #scatter plot

plt.subplot(2,2,3)
plt.plot(data[0], data[1],'-') #line plot

plt.subplot(2,2,4)
plt.hist2d(data[0], data[1]) #2d histogram

plt.show() #displays all 4 plots

"""Normal Dist Data"""

x = 10*np.random.randn(10000) #normal distribution samples assigned to x, multipled by a factor of 10 (std=10)

plt.hist(x);

x = np.random.rand(1000,) #1000 samples between 0 and 1

plt.hist(x); #uniform distribution



mu = 100  # mean of distribution (center)
sigma = 15  # standard deviation of distribution (scalar)
x = mu + sigma * np.random.randn(10000) #scalars and shifts

n,bins,patches = plt.hist(x,bins=100) #plotting normal distribution

bins

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(y) #normal distribution curve

num_bins = 50
n,bins,patches = plt.hist(x, num_bins, density=1)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(bins,y) #plot together with a line to represent the normal curve (y)



x

def mean(x): #mean
    return np.sum(x)/x.shape[0]

def var(x): #variance
    return mean((x - mean(x))**2)

def std(x): #standard deviation
    return np.sqrt(var(x))

def median(x): #median
    n = len(x)
    sorted_x = np.sort(x)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_x[mid - 1] + sorted_x[mid]) / 2
    else:
        return sorted_x[mid]

def mode(x): #mode
    values, counts = np.unique(x, return_counts=True)
    max_count_index = np.argmax(counts) #value with the highest count (multiplicity)
    return values[max_count_index]

def range(x): #range
    return np.max(x) - np.min(x)

data = np.array([1, 2, 2, 3, 4, 5, 5, 5, 6]) #running all functions

# Testing the functions
mean_value = mean(data)
var_value = var(data)
std_value = std(data)
median_value = median(data)
mode_value = mode(data)
range_value = range(data)

mean_value, var_value, std_value, median_value, mode_value, range_value



"""# Homework



"""



"""# Pi from Random Numbers"""

N = 10000 #amount of points to be generated

points = -1 + 2*np.random.random((N,2)) #x and y values range from -1 to 1

plt.plot(points[:,0],points[:,1],'.') #(x,y) correspondingly

plt.gca().set_aspect(1) #aspect ratio = 1

inside_circle  = points[:,0]**2 + points[:,1]**2  <=  1 #adds up the coordinates to tell if the point lies inside r=1
outside_circle = points[:,0]**2 + points[:,1]**2  > 1 #outside the circle

plt.plot(points[inside_circle,0],points[inside_circle,1],'g.')
plt.plot(points[outside_circle,0],points[outside_circle,1],'r.')


plt.gca().set_aspect(1) #showing points inside the circle (green)/ outside the circle (red) [inside the circle pi/3, outside the circle pi/4]

np.sum(inside_circle),np.sum(outside_circle) #points inside vs. points outside

total_area = 4 #total area of the square

fraction_inside = np.sum(inside_circle)/N #what fraction of all points lie inside the circle

fraction_inside*total_area #should give an approximation of pi (accurate 2 digits)

N = 100000000 #more accurate approximation of pi due to increased points (3 digits)
points = -1 + 2*np.random.random((N,2)) #multiple times 2 because of radius
inside_circle  = points[:,0]**2 + points[:,1]**2  <=  1 #x^2, y^2 less than or equal to 1 (r=1)
fraction_inside = np.sum(inside_circle)/N
fraction_inside*4

"""# Complete Code for Estimating π using Monte Carlo Simulation"""

# Number of random points to generate
num_points = 10000

# Generating random points
x_points = np.random.uniform(-1, 1, num_points) #uniformly distributed x and y coordinates
y_points = np.random.uniform(-1, 1, num_points)

# Calculating the number of points inside the quarter circle
points_inside = np.sqrt(x_points**2 + y_points**2) <= 1 #check if the distance is less than or equal to the radius
num_inside = np.sum(points_inside) #adds up all points inside

# Estimating π
pi_estimate = 4 * num_inside / num_points #calculates the ratio and multiplies it by 4

# Plotting the points and the quarter circle
plt.figure(figsize=(6, 6))
plt.scatter(x_points[points_inside], y_points[points_inside], color='green', label='Inside')
plt.scatter(x_points[~points_inside], y_points[~points_inside], color='red', label='Outside')
circle = plt.Circle((0, 0), 1, color='blue', fill=False) #circle graph r=1
plt.gca().add_artist(circle)
plt.title('Estimating π using Monte Carlo Simulation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.axis('equal')
plt.show()

pi_estimate #writes the approximation of pi below the graph





"""# e from Random Numbers"""

X = np.random.random((1000000,10));X #dimensions of array, random numbers between 0 and 1

Y = np.cumsum(X,1);Y #cumulative sum

Z = np.argmax(Y > 1,1) + 1;Z #set Z equivalent to the first time the cumulative sum in Y is over 1 (adds 1 because array starts at 0 to relay index)

np.mean(Z) #calulates mean

np.mean(np.argmax(np.cumsum(np.random.random((10000000,10)),1) > 1,1) + 1) #larger inputs (10x)

np.exp(1) #computes estimate of e





"""# Further Reading:

### Quantum Random Numbers API

https://aws.amazon.com/marketplace/pp/prodview-246kyrfjo3bag
"""



