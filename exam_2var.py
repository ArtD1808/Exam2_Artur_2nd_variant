import random

class Chef:
    def __init__(self, name: str, skill: int, speed: int, creativity: int):
        self.name = name
        self.skill = int(skill)
        self.speed = int(speed)
        self.creativity = int(creativity)
        self.score = 0
        self.active = True

    def compete(self, opponent: "Chef"):
        if not self.active:
            return

        points = self.skill + self.creativity - opponent.speed
        if points < 1:
            points = 1

        self.score += points
        print(f"{self.name} competes with {opponent.name}")
        print(f"{self.name} takes {points} points. Score: {self.score}")

        opponent.take_points(points)

    def take_points(self, points: int):
        self.score -= points
        if self.score < 0:
            self.score = 0
            if self.active:
                self.active = False
                print(f"{self.name} has been eliminated!")

    def is_active(self) -> bool:
        return self.active

    def show_stats(self):
        status = "active" if self.active else "eliminated"
        print(f"Name: {self.name} | Skill: {self.skill} | Speed: {self.speed} | Creativity: {self.creativity} | Score: {self.score} | Status: {status}")


class CookingContest:
    def __init__(self, seed: int | None = None):
        self.chefs = []
        if seed is not None:
            random.seed(seed)

    def add_chef(self, chef: Chef):
        self.chefs.append(chef)

    def get_active_chefs(self):
        return [c for c in self.chefs if c.is_active()]

    def start_contest(self):
        print("Contest started!\n")
        round_num = 1

        while len(self.get_active_chefs()) > 1:
            active = self.get_active_chefs()
            a, b = random.sample(active, 2)

            print(f"--- Round {round_num} ---")
            a.compete(b)

            if b.is_active():
                b.compete(a)

            print("\nCurrent chefs' states:")
            for c in self.chefs:
                c.show_stats()
            print()
            round_num += 1

        self.show_winner()

    def show_winner(self):
        winners = self.get_active_chefs()
        if len(winners) == 1:
            print(f"Winner: {winners[0].name}")
        elif len(winners) == 0:
            print("No winners (everyone eliminated).")
        else:
            names = ", ".join(w.name for w in winners)
            print(f"Tie between: {names}")


if __name__ == "__main__":
    Art = Chef("Art", skill=10, speed=5, creativity=8)
    ArtD = Chef("ArtD", skill=12, speed=6, creativity=7)
    ArtF = Chef("ArtF", skill=9, speed=4, creativity=10)

    contest = CookingContest(seed=42)
    contest.add_chef(Art)
    contest.add_chef(ArtD)
    contest.add_chef(ArtF)

    contest.start_contest()