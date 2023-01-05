import matplotlib.pyplot as plt  # Import war an falscher stelle

def merge_sort(sort_list):   #Zu langer Variablen Name + Funktionen in Snake Case und lowercase
    if (len(sort_list) > 1): # Selbe spezifizierungen
        mid = len(sort_list) // 2
        left = sort_list[:mid]
        right = sort_list[mid:]

        merge_sort(left)
        merge_sort(right)

        l = r = i = 0 # Einfachere Definition

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                sort_list[i] = left[l]     # Assignment Funktion war überflüssig
                l += 1
            else:
                sort_list[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            sort_list[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            sort_list[i] = right[r]
            r += 1
            i += 1

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.bar(x, my_list)
ax1.set_xticks(x)
ax1.set_xlabel("Index")
ax1.set_ylabel("Wert")
ax1.set_title("Unsortierte Liste")

merge_sort(my_list)

ax2.bar(x, my_list)
ax2.set_xticks(x)
ax2.set_xlabel("Index")
ax2.set_ylabel("Wert")
ax2.set_title("Sortierte Liste")
fig.tight_layout()
plt.show()