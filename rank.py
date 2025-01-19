# キャラごとに振り分けるランクと確率を管理するクラス
class Rank:

  # コンストラクタ
  def __init__(self, name, probability):
    self.name = name
    self.probability = probability


# 通常ガチャのランクと確率(0-100%)の定義
RANKS_SINGLE = [
    Rank("N", 33),
    Rank("N+", 25),
    Rank("R", 20),
    Rank("R+", 15),
    Rank("SR", 5),
    Rank("SR+", 2),
]

RANKS_ELEVEN = [
    Rank("N", 33),
    Rank("N+", 25),
    Rank("R", 57),
    Rank("R+", 30),
    Rank("SR", 10),
    Rank("SR+", 3),
]
