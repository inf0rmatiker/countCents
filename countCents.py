import sys

def main():
	
	if (len(sys.argv) < 2):
		print("Usage: python countCents.py <amount>")
		exit()
	counts = [0, 0]
	countCents(int(sys.argv[1]), counts)
	print("Amount of 5 cent stamps: " + str(counts[0]))	
	print("Amount of 3 cent stamps: " + str(counts[1]))
	print("Total min stamps required: " + str(counts[0] + counts[1]))


def countCents(amount, counts):
	# counts[0] is 5c, counts[1] is 3c
	if (amount <= 8):
		if (amount == 8):
			counts[0] = 1
			counts[1] = 1
			return counts
		elif (amount == 0):
			return counts
		elif (amount == 3):
			counts[1] += 1
			return counts
		elif (amount == 5):
			counts[0] += 1
			return counts
		elif (amount == 6):
			counts[1] += 2
			return counts
		else:
			print("Cent amount must be representable with 3 and/or 5 cent stamps!")
			exit()
	else:
		countCents(amount-1, counts)

	if (counts[1] >= 3):
		counts[1] -= 3
		counts[0] += 2
	elif (counts[0] >= 1):
		counts[0] -= 1
		counts[1] += 2
	

	return counts;


if __name__ == "__main__":
	main()