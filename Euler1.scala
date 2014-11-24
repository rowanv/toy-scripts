def mult3(n: Int): Boolean = {
	return (n % 3) == 0
}

def mult5(n:Int): Boolean = {
	return (n % 5) == 0
}

def mult3or5(n: Int) = {
	val list_nums = 0 until n
	for (i <- 0 until n) if (mult3(i) | mult5(i)) println(i)	
}

mult3or5(1000)
