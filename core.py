import NSITP7 as function

data = [
    {
        'question': 'Donnez toutes les villes dont le nom commence par « pa » (sans tenir compte de la casse)',
        'answer': [
            "afficher_table(exo1(tableVilles,'PA', 1),0,10)",
            "len(exo1(tableVilles,'PA', 1))"
        ]
    },
    {
        'question': "Donnez tous les pays d'Amérique du Sud.",
        'answer': [
            "afficher_table(exo2(tablePays, 'South America', 1),0,10)",
            "len(exo2(tablePays, 'South America', 1))"
        ]
    },
    {
        'question': "Donnez toutes les villes d'Europe dont le nom commence par pa",
        'answer': [
            "afficher_table(exo3(tableVilles,tablePays),0,10)",
            "len(exo3(tableVilles,tablePays))"
        ]
    },
    {
        'question': "Donnez toutes les villes de plus de 100 000 habitants d'Europe.",
        'answer': [
            "afficher_table(exo4(tableVilles,tablePays),0,10)",
            "len(exo4(tableVilles,tablePays))"
        ]
    },
    {
        'question': "Donnez le nombre de formes de gouvernements présentes dans la base.",
        'answer': [
            "len(exo5_6(11))"
        ]
    },
    {
        'question': "Donnez le nombre de pays répertoriés dans la base.",
        'answer': [
            'len(exo5_6(1))'
        ]
    },
    {
        'question': "Donnez tous pays où l'on parle français.",
        'answer': [
            "afficher_table((exo7()), 0, 10)",
            "len(exo7())"
        ]
    },
    {
        'question': "Donnez tous les pays où le français est langue officielle.",
        'answer': [
            "afficher_table((exo8()), 0, 10)",
            "len(exo8())"
        ]
    },
    {
        'question': "Donnez toutes les villes de moins de 100 000 habitants, d'Afrique, ayant le français pour langue officielle.",
        'answer': [
            "afficher_table((exo9()), 0, 10)",
            "len(exo9())"
        ]
    },
    {
        'question': "Quels sont les pays d'Amérique du Sud de plus de 10 000 000 d'habitants ayant un régime républicain ?",
        'answer': [
            "afficher_table((exo10()), 0, 10)",
            "len(exo10())"
        ]
    },
    {
        'question': "Quelles sont les villes de plus de 100000 habitants de pays nord-américains où l'on parle espagnol ?",
        'answer': [
            "afficher_table((exo11()), 0, 10)",
            "len(exo11())"
        ]
    },
    {
        'question': "Donnez la surface de l'Europe.",
        'answer': [
            "f'{exo12()} à 0.1 près'"
        ]
    },
    {
        'question': "Donnez la surface de la Polynésie.",
        'answer': [
            "f'{exo13()} à 0.1 près'"
        ]
    },
    {
        'question': "Combien y-a-t’il de pays en Océanie de plus 10000 km² ?",
        'answer': [
            "exo14()"
        ]
    },
    {
        'question': "Quelles sont les langues officielles des pays d'Europe de l'est ?",
        'answer': [
            "afficher_table(exo15(), 0, 10)",
            "len(exo15())"
        ]
    },
    {
        'question': "Quelle est la population moyenne dans les pays d'Asie ?",
        'answer': [
            "exo16()"
        ]
    },
    {
        'question': "Quelle est la population moyenne dans les villes des pays d'Asie ?",
        'answer': [
            "exo17()"
        ]
    },
    {
        'question': "Quelles sont les capitales d'Europe, ordonnées par ordre alphabétique ?",
        'answer': [
            "afficher_table(exo18(), 0, 10)",
            "len(exo18())"
        ]
    },
    {
        'question': "Donnez les villes des pays d'Afrique où la capitale a plus de 3 000 000 d'habitants ?",
        'answer': [
            "afficher_table(exo19(), 0, 10)",
            "len(exo19())"
        ]
    },
    {
        'question': "Quels sont les pays d’Amérique du Nord ayant accédé à l’indépendance avant 1912, où l’on parle portugais et pour lesquels sont répertoriées dans la base plus de 49 villes?",
        'answer': [
            "afficher_table(exo20(), 0, 10)",
            "len(exo20())"
        ]
    },
    {
        'question': "Quels sont les pays dont toutes les villes répertoriées dans la base ont plus de 100000 habitants ?",
        'answer': [
            "afficher_table(exo21(), 0, 10)",
            "len(exo21())"
        ]
    },
    {
        'question': "Quels sont les pays dont toutes les villes ont plus d’habitants que la ville la plus peuplée du Népal ?",
        'answer': [
            "afficher_table(exo22(), 0, 10)",
            "len(exo22())"
        ]
    },
    {
        'question': "Quels sont les pays où l’on parle français mais pas anglais ?",
        'answer': [
            "afficher_table(exo23(), 0, 10)",
            "len(exo23())"
        ]
    },
    {
        'question': "Quels sont les pays pour lesquels au moins une ville est répertoriée dans la base ?",
        'answer': [
            "afficher_table(exo24(), 0, 10)",
            "len(exo24())"
        ]
    },
    {
        'question': "Quels sont les pays pour lesquels aucune langue n’est répertoriée ?",
        'answer': [
            "afficher_table(exo25(), 0, 10)",
            "len(exo25())"
        ]
    },
    {
        'question': "Donnez les pays pour lesquels la somme du nombre d’habitants de ses villes est supérieure à 10000000. La France en fait-elle partie ?",
        'answer': [
            "afficher_table(exo26(), 0, 10)",
            "len(exo26())"
        ]
    },
    {
        'question': "Donnez le pays asiatique ayant l’espérance de vie la plus courte.",
        'answer': [
            "exo27()"
        ]
    },
    {
    'question': "Quel est le nombre de villes répertoriées dans les pays qui parlent au moins trois langues, dont le français est langue officielle et dont l’espérance de vie des habitants est supérieure à l’espérance de vie de tous les habitants d’Amérique du Sud ?",
    'answer': [
            "afficher_table(exo28(), 0, 10)",
            "len(exo28())"
        ]
    }
]

# print(function.afficher_table)

# print(function.MustBeAnOperator)
c = 0
for item in dir(function):
    c += 1
    if not item.startswith("__"):
        # exec(f'global {item}')
        exec(f'{item} = function.{item}')
        print(f'loaded {item}')
        # if c== 1 : break
        # exec(f'{item} = function.{item}')
        # print(dir(globals()[item]))

# print([item for item in dir(function) if not item.startswith("__")])

text2display = []

for exercise in data:
    exo = {
        'question': exercise['question']
    }
    for i in exercise['answer']:
        exec("tempSto = " + i)
        if 'answer' in exo.keys(): exo["answer"].append(tempSto)
        else : exo['answer'] = [tempSto]
    text2display.append(exo)

# print(text2display)