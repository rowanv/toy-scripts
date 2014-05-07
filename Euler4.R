#Project Euler Problem 4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers


#Reverses a number
num.reverse <- function(string1){
	string1 <- as.character(string1)
	string1<-strsplit(string1, "")[[1]]
	string1<-rev(string1)
	return(as.numeric(paste(string1, collapse="")))
}



#tests if a number is a palindrome, returns TRUE or FALSE
is.palindrome <- function(num){
	flipnum <- num.reverse(num)
	return(grepl(num, flipnum))

}


digit.3.nums <- c(900:999)

#Create the list of multiples that we will be testing

multiples <- vector()
for(i in digit.3.nums){
	for (j in digit.3.nums){
		multiples<-append(multiples, i*j)
	}
}


#Reorder multiples from greatest to least
multiples<-sort(multiples, decreasing=TRUE)


#Actually testing the multiples to see if they are palindromes
for (i in multiples){
	#cat("Original number", i, "Is it a palindrome?", is.palindrome(i))

	if (is.palindrome(i)==TRUE){
		print(i)
	}	

}
#the answer is 906609
