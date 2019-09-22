import random
import math
import numpy


def exp_rand_num_generator(length_, array_, lambda__):
    for k in range(length_):
        arg_ = 1 - random.random()
        log_value = math.log(arg_)
        array_.append(-1 * (1 / lambda__) * log_value)


print("START *****************************************")
lambda_ = 75
numberOfEvents = 1000
eventTypeArray = []
eventTimeArray = []


print("ARRIVAL *****************************************")
# Generating random numbers for arrivalTimes
arrivalTimeDelta = []
exp_rand_num_generator(numberOfEvents, arrivalTimeDelta, lambda_)
print("arrivalTimeDelta: ", arrivalTimeDelta)

mean = numpy.mean(arrivalTimeDelta)
print("arrivalTime mean: ", mean)

variance = numpy.var(arrivalTimeDelta)
print("arrivalTime variance: ", variance)

# used this to check:
# https://www.probabilitycourse.com/chapter4/4_2_2_exponential.php

timeOfArrival = []
arrivalTimeCounter = 0
# event = []

for i in range(numberOfEvents):
    arrivalTimeCounter = arrivalTimeCounter + arrivalTimeDelta[i]
    timeOfArrival.append(arrivalTimeCounter)
    eventTypeArray.append('Arrival')
    eventTimeArray.append(arrivalTimeCounter)

print("timeOfArrival: ", timeOfArrival)

print("PACKET LENGTH *****************************************")
packetBitLength = []
avgPacketLength = 2000
exp_rand_num_generator(numberOfEvents, packetBitLength, 1 / avgPacketLength)
print("packetLength", packetBitLength)

mean2 = numpy.mean(packetBitLength)
print("packetLength mean: ", mean2)

variance2 = numpy.var(packetBitLength)
print("packetLength variance: ", variance2)

print("SERVICING *****************************************")
servicingTime = []
C = 1000000
for i in range(numberOfEvents):
    servicingTime.append(packetBitLength[i]/C)  # since servicingTime = L/C
print("servicingTime", servicingTime)

mean2 = numpy.mean(servicingTime)
print("sample mean: ", mean2)

variance2 = numpy.var(servicingTime)
print("sample variance: ", variance2)


print("DEPARTURE *****************************************")
departureTime = []
departureTimeCounter = 0
for i in range(numberOfEvents):
    currentDepartureTime = 0.0
    if i == 1:
        currentDepartureTime = timeOfArrival[i] + servicingTime[i]
        departureTime.append(currentDepartureTime)
        eventTypeArray.append('Departure')
        eventTimeArray.append(currentDepartureTime)
        departureTimeCounter = currentDepartureTime

    else:
        if timeOfArrival[i] > departureTimeCounter:
            departureTimeCounter = timeOfArrival[i]
        currentDepartureTime = departureTimeCounter + servicingTime[i]
        departureTime.append(currentDepartureTime)
        eventTypeArray.append('Departure')
        eventTimeArray.append(currentDepartureTime)
        departureTimeCounter = currentDepartureTime

print("departureTime: ", departureTime)

print("OBSERVER *****************************************")
observerTime = []
exp_rand_num_generator(numberOfEvents, observerTime, lambda_*5)

print("observerTime: ", observerTime)
for i in range(numberOfEvents):
    eventTypeArray.append('Observer')
    eventTimeArray.append(observerTime[i])


# FILE WRITE ******************************
a = numpy.asarray(numpy.transpose([timeOfArrival, departureTime, observerTime]))
numpy.savetxt("foo.csv", a, delimiter=",")
print(a)
print("***********")
# eventTypeArray.append(event.event_type)
# eventTimeArray.append(event.event_time)

# print(eventTypeArray)
# print(eventTimeArray)
b = numpy.asarray(numpy.transpose([eventTypeArray, eventTimeArray]))
print(b)
numpy.savetxt("foo2.csv", b, fmt='%s', delimiter=",")

