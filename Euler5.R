#Project Euler Problem 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Checks if some number, num1, is evenly divisible by some other number, num2
is.divisible <- function(num1, num2){
	if (num1 %% num2 == 0){
		return(TRUE)
	}
	return(FALSE)
}

#check multiples of 2520, the LCM

mult.20 <- c(1*2520:100000*2520)


#Takes num1 and some list of numbers, returns TRUE if num1 is evenly divisible by all 
#of the numbers in listnum
is.divisible.list <- function(num1, listnum){
	for (i in listnum){
		if(is.divisible(num1, i) == FALSE){
			return(FALSE)
		}
	}
	return(TRUE)
	
}


for (i in mult.20){
	if(is.divisible.list(i, c(1:20))==TRUE){
		cat("IT IS:", i)
		break
	}
}
#the number is 232792560
