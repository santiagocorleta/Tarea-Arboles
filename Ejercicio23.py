from binary_tree import BinaryTree

criaturas = [
    {"name": "Ceto", "derrotado_por": None},
    {"name": "Tifón", "derrotado_por": "Zeus"},
    {"name": "Ortro", "derrotado_por": "Heracles"},
    {"name": "Toro de Creta", "derrotado_por": "Teseo"},
    {"name": "Medusa", "derrotado_por": "Perseo"},
    {"name": "Hidra de Lerna", "derrotado_por": "Heracles"},
    {"name": "Esfinge", "derrotado_por": "Edipo"},
    {"name": "Ladón", "derrotado_por": "Heracles"},
    {"name": "Talos", "derrotado_por": "Medea"},
    {"name": "Cerbero", "derrotado_por": None},
    {"name": "Basilisco", "derrotado_por": None},
    {"name": "Sirenas", "derrotado_por": None},
]

arbol = BinaryTree()

for c in criaturas:
    arbol.insert(c["name"], c)


# a) Listado inorden
print("\n(a) Listado inorden de criaturas y sus vencedores:")
arbol.in_order()

# c) Mostrar info de Talos
print("\n(c) Mostrar información de 'Talos':")
pos = arbol.search("Talos")
if pos:
    print(pos.value, pos.other_values)
else:
    print("No se encontró 'Talos'")

# d) Determinar los 3 héroes que más criaturas derrotaron
print("\n(d) Top 3 héroes con más derrotas:")
ranking_result = {}
arbol.ranking(ranking_result)
top3 = sorted(ranking_result.items(), key=lambda x: x[1], reverse=True)[:3]
for h, n in top3:
    print(h, ":", n)

# e) Listar criaturas derrotadas por Heracles
print("\n(e) Criaturas derrotadas por Heracles:")
def defeated_by_heracles(root):
    if root is not None:
        defeated_by_heracles(root.left)
        if root.other_values["derrotado_por"] == "Heracles":
            print(root.value)
        defeated_by_heracles(root.right)

if arbol.root:
    defeated_by_heracles(arbol.root)

# f) Criaturas no derrotadas
print("\n(f) Criaturas no derrotadas:")
def undefeated(root):
    if root is not None:
        undefeated(root.left)
        if root.other_values["derrotado_por"] is None:
            print(root.value)
        undefeated(root.right)

if arbol.root:
    undefeated(arbol.root)

# j) Eliminar Basilisco y Sirenas
print("\n(j) Eliminar Basilisco y Sirenas:")
for name in ["Basilisco", "Sirenas"]:
    value, data = arbol.delete(name)
    if value:
        print("Eliminada:", value)
    else:
        print(name, "no encontrada")

# k) Modificar Aves del Estínfalo 
pos = arbol.search("Aves del Estínfalo")
if pos:
    pos.other_values["derrotado_por"] = "Heracles"
    print("Aves del Estínfalo derrotadas por Heracles")

# l) Cambiar 'Ladón' por 'Dragón Ladón'
print("\n(l) Renombrar 'Ladón' → 'Dragón Ladón'")
value, other = arbol.delete("Ladón")
if value:
    other["name"] = "Dragón Ladón"
    arbol.insert(other["name"], other)
    print("Renombrado correctamente.")

# m) Barrido por nivel
print("\n(m) Listado por nivel:")
arbol.by_level()

# n) Mostrar criaturas capturadas o derrotadas por Heracles
print("\n(n) Criaturas derrotadas por Heracles:")
def heracles_creatures(root):
    if root is not None:
        heracles_creatures(root.left)
        if root.other_values["derrotado_por"] == "Heracles":
            print(root.value)
        heracles_creatures(root.right)

if arbol.root:
    heracles_creatures(arbol.root)
