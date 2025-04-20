from module.combat_power_calc import combat_power_calc

class Charactor:
    """ニケのキャラクターパラメータを扱うクラス

    Ref:
        https://youtu.be/r6SZJfq0CTQ?si=Qon1cBYqupGoQLG_
    """

    def __init__(self, params):
        """コンストラクタ（初期化メソッド）
        """
        self.name = params['name']
        self.combat_power = combat_power_calc(params['hp'],
                                              params['attack_power'],
                                              params['defence_power'],
                                              params['skill_level_one'],
                                              params['skill_level_two'],
                                              params['burst_level'])

if __name__ == '__main__':

    params = {
        'name':'Alice',
        'hp':2773971,
        'attack_power':120813,
        'defence_power':16490,
        'skill_level_one':10,
        'skill_level_two':6,
        'burst_level':9}

    # インスタンスを作成
    charactor = Charactor(params)

    # キャラの名前と戦闘力を表示
    print(f'name: {charactor.name},',
          f'battle_power: {charactor.combat_power}')
