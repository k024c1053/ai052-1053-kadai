import random
from rank import RANKS_SINGLE, RANKS_ELEVEN
from character_pool import CharacterPool


class Gacha:
    NORMAL_COST = 100     # 通常ガチャのコスト
    ELEVEN_COST = 1000    # 11連ガチャのコスト

    # コンストラクタ
    def __init__(self):
        self.character_pool = CharacterPool()
        self.play_count = 0
        self.cost = 0
        self.single_count = 0
        self.eleven_count = 0
        self.sr_plus_collection = set()

    # 実装部分
    def _draw_character(self, ranks):
        rank = random.choices([r.name for r in ranks],
                              [r.probability for r in ranks])[0]
        character = self.character_pool.get_random_character(rank)
        if rank == "SR+":
            self.sr_plus_collection.add(character)
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
        # 11連目は必ず「SR」
        results.append(("SR", self.character_pool.get_random_character("SR")))
        self.play_count += 11
        self.eleven_count += 1
        self.cost += self.ELEVEN_COST
        return results

    def reset(self):
        self.play_count = 0
        self.cost = 0
        self.single_count = 0
        self.eleven_count = 0
        self.sr_plus_collection = set()

    def get_summary(self):
        return {
            "play_count": self.play_count,
            "single_count": self.single_count,
            "eleven_count": self.eleven_count,
            "cost": self.cost,
            "sr_plus_collection": len(self.sr_plus_collection)
        }
