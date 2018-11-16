### 题目：

- 输入一个整形数组，数组里有正数也有负数。
  数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。
  求所有子数组的和的最大值。要求时间复杂度为O(n)。

**分析：这是动态规划问题。**

**代码：**

```
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
```

