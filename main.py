def count_even_number(numbers):
    result=0
    for i in numbers:
        if i%2==0:
            result+=1
    return result

print(count_even_number([1,2]))
print(count_even_number([1,3,5,7,9]))
