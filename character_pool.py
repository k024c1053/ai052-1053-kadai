import random


class CharacterPool:

    def __init__(self):
        # ランクごとのフォルダパス
        self.rankpath = {
            "N": "01.Rank_N",
            "N+": "02.Rank_N+",
            "R": "03.Rank_R",
            "R+": "04.Rank_R+",
            "SR": "05.Rank_SR",
            "SR+": "06.Rank_SR+"
        }

        # 各ランクに対するキャラクター画像ファイル名
        self.characters = {
            "N": [f"{self.rankpath['N']}/{j}.jpg" for j in range(1, 21)],
            "N+": [f"{self.rankpath['N+']}/{j}.jpg" for j in range(1, 21)],
            "R": [f"{self.rankpath['R']}/{j}.jpg" for j in range(1, 16)],
            "R+": [f"{self.rankpath['R+']}/{j}.jpg" for j in range(1, 16)],
            "SR": [f"{self.rankpath['SR']}/{j}.jpg" for j in range(1, 11)],
            "SR+": [f"{self.rankpath['SR+']}/{j}.jpg" for j in range(1, 11)]
        }

    def get_random_character(self, rank_name):
        # 指定されたランクからランダムにキャラクター画像のパスを返す
        return random.choice(self.characters[rank_name])
