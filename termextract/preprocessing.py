import itertools as it
import re
import MeCab

from collections import namedtuple


class MeCabTokenizer:
    Morpheme = namedtuple("Morpheme", "surface pos pos_s1 pos_s2")

    def __init__(self, **kwargs):
        self.tagger = MeCab.Tagger(**kwargs)
        self.tagger.parse("Initialize")

    def iter_token(self, text):
        node = self.tagger.parseToNode(text)
        node = node.next
        while node.next:
            yield self.Morpheme(node.surface, *node.feature.split(",")[:3])
            node = node.next


def filter_noun(n):
    if re.match(r"[#!「」\(\)\[\]]", n.surface):
        return False
    if n.pos == "名詞" and n.pos_s1 == "一般":
        return True
    if n.pos == "名詞" and n.pos_s1 == "接尾" and n.pos_s2 == "一般":
        return True
    if n.pos == "名詞" and n.pos_s1 == "サ変接続":
        return True
    if n.pos == "名詞" and n.pos_s1 == "接尾" and n.pos_s2 == "サ変接続":
        return True
    if n.pos == "名詞" and n.pos_s1 == "固有名詞":
        return True
    if n.pos == "記号" and n.pos_s1 == "アルファベット":
        return True
    if n.pos == "名詞" and n.pos_s1 == "形容動詞語幹":
        return True
    if n.pos == "名詞" and n.pos_s1 == "ナイ形容詞語幹":
        return True
    return False


def simple_filter_noun(n):
    return lambda n: n.pos == "名詞"


def extract_nouns(tokens, f=filter_noun):
    return [morphemes_to_surface(g) for k, g in it.groupby(tokens, f) if k]


def morphemes_to_surface(morphemes):
    return [m.surface for m in morphemes]
