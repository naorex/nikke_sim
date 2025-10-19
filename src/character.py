from src.service import Service


class Character:

    def __init__(self, name: str, service: Service) -> None:
        self.name = name
        self.hp = service.get_hp(name)
        self.attack_power = service.get_attack_power(name)
        self.defence_power = service.get_defence_power(name)
        self.combat_power = self.calc_combat_power()

    def calc_combat_power(self) -> int:

        critical_coef: float = 1.075  # 仮入力
        health_coef: float = self.defence_power * 100 + self.hp
        status_coef: float = (self.attack_power * 18 * critical_coef) + (
            health_coef * 0.7
        )
        skill_level_one: int = 1
        skill_level_two: int = 1
        skill_level_burst: int = 1
        sum_except_advance_code_rank: int = 0
        sum_of_advance_code_rank: int = 0

        skill_coef: float = (
            skill_level_one * 0.01
            + skill_level_two * 0.01
            + skill_level_burst * 0.02
            + sum_except_advance_code_rank * 0.0069
            + sum_of_advance_code_rank * 0.0091
        )
        combat_power: int = round(status_coef * (1.3 + skill_coef) / 100)

        return combat_power
