def primes(given):
    #Basic parameters to be used
    listOfPrimes = []
    end = given
    allNums = {}


    
    #Makes a dict with all the nums in it
    counter = 1
    
    while counter <=end:
        allNums[counter] = False
        counter = counter +1


        
    #Checks the numbers by the base formula    
    i = 1

    while i*i < end:
        j = 1

        while j*j < end:
            iSquare = i*i
            jSquare = j*j


            worker = (4*iSquare) + (jSquare)
            if (worker % 12 == 1 or worker % 12 == 5) and worker <=end:
                allNums[worker] ^= True


            worker = (3*iSquare) + (jSquare)
            if worker % 12 == 7 and worker <=end:
                allNums[worker] ^= True


            worker = (3*iSquare) - (jSquare)
            if i > j and worker % 12 == 11 and worker <= end:
                allNums[worker] ^= True

            j = j+1
        i = i+1


        
    #Re-checks all multiples of 5
    i = 5

    while i*i < end:
        if allNums[i] == True:
            timeSaver = i*i

            j = timeSaver
            while j < end:
                allNums[j] = False
                j = j + timeSaver
        i = i+1


                
    #Hard adds 2 and 3 to listOfPrimes
    listOfPrimes.append(2)
    listOfPrimes.append(3)



    #Adds all the prime numbers to listOfPrimes
    counter = 1

    while counter <=end:
        if allNums[counter] == True:
            listOfPrimes.append(counter)

        counter = counter +1



    return listOfPrimes



print(len(primes(100000000)))
