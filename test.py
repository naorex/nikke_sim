import pandas as pd
from Charactor import Charactor

charactor_list = pd.read_csv('./NIKKE_charactor_sheet.csv')

sum_of_combat_power = 0
for i in charactor_list.index:
    params = charactor_list.iloc[i,:].to_dict()

    charactor = Charactor(params)
    print(f'name: {charactor.name},',
          f'battle_power: {charactor.combat_power}')

    sum_of_combat_power += charactor.combat_power

    if i == charactor_list.index[-1]:
        print(f'total combat_power: {sum_of_combat_power}')
