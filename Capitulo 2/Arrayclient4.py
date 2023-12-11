import Array3
maxSize = 10 
arr = Array3.Array(maxSize) 
arr.insert(77) 
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)
print("Array containing", len(arr), "items")
arr.traverse()
print("Search for 12 returns", arr.search(12))
print("Search for 12.34 returns", arr.search(12.34))
print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))
print("Setting item at index 3 to 33")
arr.set(3, 33)
print("Array after deletions has", len(arr), "items")
arr.traverse()
max_num = arr.getMaxNum()
print("Maximo numero del array:", max_num)
print("Array containing", len(arr), "items")
arr.traverse()
max_num = arr.deleteMaxNum()
if max_num is not None:
    print("Maximo numero eliminado despues del array:", max_num)

print("Matriz después de eliminar el número máximo tiene", len(arr), "items")
arr.traverse()

for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if isinstance(arr.get(j), (int, float)) and isinstance(arr.get(min_idx), (int, float)):
            if arr.get(j) < arr.get(min_idx):
                min_idx = j
    if min_idx != i:
        arr.set(i, arr.get(min_idx))
        arr.set(min_idx, arr.get(i))

print("Matriz orden acendente ")
arr.traverse()


print("Matriz original que contiene", len(arr), "items")
arr.traverse()


arr.removeDupes()

print("La matriz después de eliminar duplicados tiene", len(arr), "items")
arr.traverse()
