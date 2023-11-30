fruits = {
 'apple': 130,
 'avocado': 50,
 'lime': 20,
 'banana': 110,
 'lemon': 15,
 'grapes': 90,
 'orange': 80,
 'watermelon': 80,
 'honeydew melon': 50,
 'nectarine': 60,
 'peach': 60,
 'pineapple': 50,
 'plums': 70,
 'strawberries': 50,
 'sweet cherries': 100,
 'tangerine': 50,
 'pear' :100,
 'kiwifruit': 90
 }
fruit =input("Фрукт: ").lower()
if fruit in fruits:
 print("Калории:", fruits[fruit])
