from termextract import LRValue
from termextract.preprocessing import extract_nouns, morphemes_to_surface, MeCabTokenizer


def main():
    text = """「人工知能」という名前は1956年にダートマス会議でジョン・マッカーシーにより命名された。
    現在では、記号処理を用いた知能の記述を主体とする情報処理や研究でのアプローチという意味あいでも使われている。
    日常語としての「人工知能」という呼び名は非常に曖昧なものになっており、多少気の利いた家庭用電気機械器具の制御システムやゲームソフトの思考ルーチンなどがこう呼ばれることもある。"""

    tok = MeCabTokenizer()

    compound_nouns = []
    for sentence in text.splitlines():
        tokens = tok.iter_token(sentence)
        compound_nouns.extend(extract_nouns(tokens))

    lr = LRValue()
    lr_values = lr.fit_transform(compound_nouns)

    print(lr_values)
    print(lr.compound_noun)
    print(lr.rn("人工"))


if __name__ == "__main__":
    main()
