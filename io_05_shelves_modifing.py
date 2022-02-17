import shelve

# gra_pao_gai = ['chicken', 'basil', 'chili', 'rice']
# khao_kan_chin = ['rice mixed with pork blood', 'steamed in banana leaf', 'dried chilli']
# khao_kha_mu = ['pork leg\' slices', 'rice', 'soy sauce']
# khao_khai_chiao = ['omelette', 'rice', 'minced pork']
# khao_kluk_khapi = ['shrimp paste rice', 'veggies: mango, cucumber', 'sliced omelette', 'fried garlic']
# khao_mu_krop = ['rice', 'crispy pork']

with shelve.open('thai_dishes', writeback=True) as thai_menu:
    # thai_menu['gra_pao_gai'] = gra_pao_gai
    # thai_menu['khao_kan_chin'] = khao_kan_chin
    # thai_menu['khao_kha_mu'] = khao_kha_mu
    # thai_menu['khao_khai_ciao'] = khao_khai_chiao
    # thai_menu['khao_kluk_khapi'] = khao_kluk_khapi
    # thai_menu['khao_mu_krop'] = khao_mu_krop

    print('=' * 60)
    for dish in thai_menu:
        print(dish, thai_menu[dish])

    # below doesn't work: chilli dip is appended to the object in memory
    # while for loop print object from shelve
    # thai_menu['khao_mu_krop'].append("chilli dip")
    # thai_menu['khao_kha_mu'].append("chilli dip")

    # SOLUTION 1: create temporary object. modify object.
    # assign object value back to the object in database.
    # ADVANTAGE: work with object in memory - fast
    # temp_menu = thai_menu["khao_mu_krop"]
    # temp_menu.append("chilli dip")
    # thai_menu['khao_mu_krop'] = temp_menu

    # SOLUTION 2: writeback = True line 10
    # easier code, but havier memory usage
    # python save modification when close with statement
    thai_menu['tom_yum_khug'] = ['coconut milk', 'tom yum spices', 'chilli', 'shrimps']

    print('=' * 60)
    for dish in thai_menu:
        print(dish, thai_menu[dish])