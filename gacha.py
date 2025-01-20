import random
from rank import RANKS_SINGLE, RANKS_ELEVEN
from character_pool import CharacterPool


class Gacha:
    NORMAL_COST = 100
    ELEVEN_COST = 1000

    def __init__(self):
        self.character_pool = CharacterPool()

    def _draw_character(self, ranks):
        rank = random.choices([r.name for r in ranks],
                              [r.probability for r in ranks])[0]
        character = self.character_pool.get_random_character(rank)
        return rank, character

    def draw_single(self, session):
        rank, character = self._draw_character(RANKS_SINGLE)
        session['play_count'] += 1
        session['single_count'] += 1
        session['cost'] += self.NORMAL_COST

        # セッションからリストを取得して更新
        characters = set(session['collected_characters'][rank])
        characters.add(character)
        session['collected_characters'][rank] = list(characters)

        return rank, character

    def draw_eleven(self, session):
        results = []
        for _ in range(10):
            rank, character = self._draw_character(RANKS_ELEVEN)
            results.append((rank, character))

            # セッションからリストを取得して更新
            characters = set(session['collected_characters'][rank])
            characters.add(character)
            session['collected_characters'][rank] = list(characters)

        # ボーナスの1回 (SR固定)
        sr_character = self.character_pool.get_random_character("SR")
        results.append(("SR", sr_character))
        characters = set(session['collected_characters']["SR"])
        characters.add(sr_character)
        session['collected_characters']["SR"] = list(characters)

        session['play_count'] += 11
        session['eleven_count'] += 1
        session['cost'] += self.ELEVEN_COST
        return results

    def get_summary(self, session):
        return {
            "play_count": session['play_count'],
            "single_count": session['single_count'],
            "eleven_count": session['eleven_count'],
            "cost": session['cost'],
            "collected_counts": {
                rank: len(session['collected_characters'][rank])
                for rank in session['collected_characters']
            }
        }
