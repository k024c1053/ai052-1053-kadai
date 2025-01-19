import random


# キャラクターの画像パスを管理するクラス
class CharacterPool:

    # コンストラクタ
    def __init__(self):
        # ランクごとのフォルダパスの管理(辞書)
        self.rankpath = {
            "N": "01.Rank_N",
            "N+": "02.Rank_N+",
            "R": "03.Rank_R",
            "R+": "04.Rank_R+",
            "SR": "05.Rank_SR",
            "SR+": "06.Rank_SR+"
        }

        # 各ランクに対するキャラクター画像ファイルパス
        self.characters = {
            "N": [
                f"images/chara/{self.rankpath['N']}/{j}.jpg"
                for j in range(0, 20)
            ],  # 20種類
            "N+": [
                f"images/chara/{self.rankpath['N+']}/{j}.jpg"
                for j in range(0, 20)
            ],  # 20種類
            "R": [
                f"images/chara/{self.rankpath['R']}/{j}.jpg"
                for j in range(0, 15)
            ],  # 15種類
            "R+": [
                f"images/chara/{self.rankpath['R+']}/{j}.jpg"
                for j in range(0, 15)
            ],  # 15種類
            "SR": [
                f"images/chara/{self.rankpath['SR']}/{j}.jpg"
                for j in range(0, 10)
            ],  # 10種類
            "SR+": [
                f"images/chara/{self.rankpath['SR+']}/{j}.jpg"
                for j in range(0, 10)
            ]  # 10種類
        }


    def get_random_character(self, rank_name):
        # 指定されたランクからランダムにキャラクター画像のパスを返す
        return random.choice(self.characters[rank_name])
