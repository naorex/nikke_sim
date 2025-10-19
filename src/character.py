class Character:
    """ニケのキャラクターパラメータを扱うクラス"""

    def __init__(self):
        self.name = "test"
        self.hp = 244350
        self.attack_power = 4805
        self.defence_power = 1837
        self.combat_power = self.combat_power_calc()

    def combat_power_calc(self):

        # クリティカル補正
        critical_coef = 1.075  # 仮入力

        # 体力補正
        health_coef = self.defence_power * 100 + self.hp

        # ステータス補正
        status_coef = (self.attack_power * 18 * critical_coef) + (health_coef * 0.7)

        # スキル補正
        skill_level_one = 1
        skill_level_two = 1
        skill_level_burst = 1
        sum_except_advance_code_rank = 0
        sum_of_advance_code_rank = 0

        skill_coef = (
            skill_level_one * 0.01
            + skill_level_two * 0.01
            + skill_level_burst * 0.02
            + sum_except_advance_code_rank * 0.0069
            + sum_of_advance_code_rank * 0.0091
        )

        # 戦闘力計算
        combat_power = round(status_coef * (1.3 + skill_coef) / 100)

        return combat_power
