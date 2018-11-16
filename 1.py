def MaxSub(lists):
	sum=lists[0];
	temp=0;
	for i in lists:
		if temp<0:
			temp=i
		else:
			temp +=i
		if temp>sum:
			sum=temp
	return sum

def main():
	Lists=[6,-2,4,9,-8,-3,6,-1,2]
	print (MaxSub(Lists))

if __name__ == "__main__":
	main()