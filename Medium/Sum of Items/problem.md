

I have one question in my exam I want to know how I will implement this in JavaScript.

Question During the war, the enemy battalion has planted a bomb in your bunker. Your informer has sent you a message of the enemy which contains a list having N numbers and a key. The numbers are used to construct a sequence to defuse the bomb. According to your informer, the logic to extract the sequence from the whole message is by replacing each number with the sum of the next key numbers. When the value of key is negative, the number is replaced by the sum of the previous key numbers. The series of numbers is considered in a cyclic fashion for the last key numbers.


The input to the function/method consists of three arguments

size: an integer representing the size of the list (N).
key: an integer representing the key.
message: representing the list of integers.

output:
Return a list of integers representing the sequence to defuse the bomb.

input:
message= [4,2,-5,11]
size =4
key = 3

steps [2,-5,11] ==> 8
steps[-5,11,4]==>10
steps[11,4,2]==>17
steps[4,2,-5]==>1

expected output =[8,10,17,1]