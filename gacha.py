import random
from rank import RANKS_SINGLE, RANKS_ELEVEN
from character_pool import CharacterPool


class Gacha:
    NORMAL_COST = 100
    ELEVEN_COST = 1000

    def __init__(self):
        self.character_pool = CharacterPool()
        self.play_count = 0
        self.cost = 0
        self.single_count = 0
        self.eleven_count = 0

        # 各ランクごとのコレクションを追跡
        self.collected_characters = {
            "N": set(),
            "N+": set(),
            "R": set(),
            "R+": set(),
            "SR": set(),
            "SR+": set()
        }

    def _draw_character(self, ranks):
        rank = random.choices([r.name for r in ranks],
                              [r.probability for r in ranks])[0]
        character = self.character_pool.get_random_character(rank)

        # コレクションにキャラクターを追加
        self.collected_characters[rank].add(character)

        return rank, character

    def draw_single(self):
        self.play_count += 1
        self.single_count += 1
        self.cost += self.NORMAL_COST
        rank, character = self._draw_character(RANKS_SINGLE)
        return rank, character

    def draw_eleven(self):
        results = []
        for _ in range(10):
            rank, character = self._draw_character(RANKS_ELEVEN)
            results.append((rank, character))
        # 11連目はSR固定
        sr_character = self.character_pool.get_random_character("SR")
        results.append(("SR", sr_character))
        self.collected_characters["SR"].add(sr_character)
        self.play_count += 11
        self.eleven_count += 1
        self.cost += self.ELEVEN_COST
        return results

    def reset(self):
        self.play_count = 0
        self.cost = 0
        self.single_count = 0
        self.eleven_count = 0
        self.collected_characters = {
            key: set()
            for key in self.collected_characters
        }

    def get_summary(self):
        return {
            "play_count": self.play_count,
            "single_count": self.single_count,
            "eleven_count": self.eleven_count,
            "cost": self.cost,
            "collected_counts": {
                rank: len(characters)
                for rank, characters in self.collected_characters.items()
            }
        }
