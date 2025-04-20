

def combat_power_calc(hp,
                      attack_power,
                      defence_power,
                      skill_level_one,
                      skill_level_two,
                      burst_level):
    """戦闘力計算
    """

    # クリティカル補正
    critical_coef = 1.075  # => 仮入力

    # 体力補正
    health_coef = defence_power * 100 + hp

    # ステータス補正
    status_coef = (attack_power * 18 * critical_coef) \
                + (health_coef * 0.7)

    # スキル補正（アプデ前）
    skill_coef = skill_level_one * 0.01 \
                + skill_level_two * 0.01 \
                + burst_level * 0.02

    # スキル補正（アプデ後）
    rank_sum_except_adv_code = 84  # => 仮入力
    rank_sum_of_adv_code = 0       # => 仮入力

    skill_coef = skill_coef \
            + rank_sum_except_adv_code * 0.0069 \
            + rank_sum_of_adv_code * 0.0091

    # 戦闘力計算
    combat_power = round(status_coef * (1.3 + skill_coef) / 100)

    return combat_power
