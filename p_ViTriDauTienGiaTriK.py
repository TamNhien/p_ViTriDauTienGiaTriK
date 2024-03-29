def find_first_occurrence(lst, k):
    return lst.index(k) if k in lst else -1

nums = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
k = int(input("Nhập số nguyên dương k: "))
print(f"Vị trí của phần tử đầu tiên có giá trị {k} là: {find_first_occurrence(nums, k)}")
