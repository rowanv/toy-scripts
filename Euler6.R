#Euler Problem No. 6

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Calculates the sum of the squares for some set of natural numbers
#Args: start.num -- a number, start of the range of the set of natural numbers
#		stop.num -- a number, end of the range of the set of natural numbers
sum.squares <- function(start.num, stop.num){
	num.list <- c(start.num:stop.num)
	sum.num <- 0
	for(i in num.list){
		sum.num <- sum.num + i**2
	}
	return(sum.num)
}


#Calculates the square of the sum for some set of natural numbers
#Args: start.num -- a number, start of the range of the set of natural numbers
#		stop.num -- a number, end of the range of the set of natural numbers

square.sum <- function(start.num, stop.num){
	num.list <- c(start.num:stop.num)
	sum.num <- 0
	sum.num <- sum(num.list)**2
	return(sum.num)
	
}


#difference of the sum of the squares and the square of the sum

result <- square.sum(1,100) - sum.squares(1,100) 
result
#answer is 25164150
