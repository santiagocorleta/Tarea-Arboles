from binary_tree import BinaryTree 

superheroes = [
    {"name": "Iron Man", "is_villain": False},
    {"name": "Thanos", "is_villain": True},
    {"name": "Captain America", "is_villain": False},
    {"name": "Loki", "is_villain": True},
    {"name": "Black Widow", "is_villain": False},
    {"name": "Ultron", "is_villain": True},
    {"name": "Doctor Strange", "is_villain": False},
    {"name": "Dr Strange", "is_villain": False},  # mal cargado
    {"name": "Wanda Maximoff", "is_villain": False},
    {"name": "Mysterio", "is_villain": True},
    {"name": "Captain Marvel", "is_villain": False},
    {"name": "Red Skull", "is_villain": True},
    {"name": "Hela", "is_villain": True},
]


arbol = BinaryTree()

for s in superheroes:
    arbol.insert(s["name"], s)


# b) Listado de villanos en orden alfabético
print("\n(b) Villanos ordenados alfabéticamente:")
arbol.villain_in_order()

# c) Superhéroes que comienzan con C
print("\n(c) Superhéroes que comienzan con 'C':")
arbol.proximity_search("C")

# d) Contar superhéroes
print("\n(d) Cantidad de superhéroes:")
print(arbol.count_heroes())

# e) Buscar y corregir Doctor Strange mal cargado
print("\n(e) Buscar por proximidad 'Dr' y corregir nombre:")
arbol.proximity_search("Dr")

value, other_value = arbol.delete("Dr Strange")
if value is not None:
    print("Corrigiendo nombre a 'Doctor Strange'")
    other_value["name"] = "Doctor Strange"
    arbol.insert(other_value["name"], other_value)

print("\nVerificación tras corrección:")
arbol.proximity_search("Doctor")

# f) Superhéroes ordenados descendente
print("\n(f) Superhéroes ordenados descendente:")
heroes_desc = []

def collect_heroes_desc(root):
    if root is not None:
        collect_heroes_desc(root.right)
        if root.other_values["is_villain"] is False:
            heroes_desc.append(root.value)
        collect_heroes_desc(root.left)

if arbol.root:
    collect_heroes_desc(arbol.root)

for h in heroes_desc:
    print(h)

# g) Dividir el árbol en héroes y villanos (bosque)
print("\n(g) Bosque: héroes y villanos separados")
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

arbol.divide_tree(arbol_heroes, arbol_villanos)

print("\nHéroes:")
arbol_heroes.in_order()

print("\nVillanos:")
arbol_villanos.in_order()

print("\nTotal héroes:", arbol_heroes.count_heroes())
print("Total villanos:", arbol_villanos.count_heroes())
