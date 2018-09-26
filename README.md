# termextract

次の論文の内容を練習で実装しました。

- [中川 裕志, 湯本 紘彰, 森 辰則, 出現頻度と連接頻度に基づく専門用語抽出, 自然言語処理, 2003, 10巻, 1号, p.27-45 ](https://www.jstage.jst.go.jp/article/jnlp1994/10/1/10_1_27/_article/-char/ja)

## Usage

```sh
pip install git+https://github.com/kanjirz50/termextract
```

```python
from termextract import LRValue
from termextract.preprocessing import extract_nouns, morphemes_to_surface, MeCabTokenizer

# https://ja.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E7%9F%A5%E8%83%BD
text = """「人工知能」という名前は1956年にダートマス会議でジョン・マッカーシーにより命名された。
現在では、記号処理を用いた知能の記述を主体とする情報処理や研究でのアプローチという意味あいでも使われている。
日常語としての「人工知能」という呼び名は非常に曖昧なものになっており、多少気の利いた家庭用電気機械器具の制御システムやゲームソフトの思考ルーチンなどがこう呼ばれることもある。"""

tok = MeCabTokenizer()

compound_nouns = []
for sentence in text.splitlines():
    tokens = tok.iter_token(sentence)
    nouns = extract_nouns(tokens)
    # nouns = ['人工', '知能'], ['名前'], ['ダート', 'マス', '会議'], ['ジョン'], ['マッカーシー'], ['命名']]
    compound_nouns.extend(nouns)

lr = LRValue()
lr_values = lr.fit_transform(compound_nouns)

print(lr_values)
"""
{'人工 知能': 3.4641016151377544, '名前': 1.0, 'ダート マス 会議': 1.5874010519681994, 'ジョン': 1.0, 'マッカーシー': 1.0, '命名': 1.0, '記号 処理': 1.4142135623730951, '知能': 1.7320508075688772, '記述': 1.0, '主体': 1.0, '情報処理': 1.0, '研究': 1.0, 'アプローチ': 1.0, '意味あい': 1.0, '日常 語': 1.4142135623730951, '呼び名': 1.0, '非常': 1.0, '曖昧': 1.0, '気': 1.0, '家庭 用 電気 機械 器具': 1.7411011265922482, '制御 システム': 1.4142135623730951, 'ゲーム ソフト': 1.4142135623730951, '思考 ルーチン': 1.4142135623730951}
"""

print(lr.compound_noun)
"""
['人工 知能', '名前', 'ダート マス 会議', 'ジョン', 'マッカーシー', '命名', '記
号 処理', '知能', '記述', '主体', '情報処理', '研究', 'アプローチ', '意味あい', '日常 語', '呼び名', '非常', '曖昧', '気', '家庭 用 電気 機械 器具', '制御 シス
テム', 'ゲーム ソフト', '思考 ルーチン']
"""

print(lr.rn("人工"))
"""
2
"""
```
