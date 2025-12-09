
nums = input("Enter numbers separated by space: ").split()
nums = [int(x) for x in nums]
largest = nums[0]
for num in nums:
  if num > largest:
    largest = num
print("The largest number is:", largest)
