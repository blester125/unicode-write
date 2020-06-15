from typing import Dict, List, Callable


def white_space_tokenize(string: str) -> List[str]:
    return string.split()


def lowercase(string: str) -> str:
    return string.lower()


class InvertedIndex:
    def __init__(
        self, tokenize: Callable[[str], List[str]] = white_space_tokenize, preprocess: Callable[[str], str] = lowercase,
    ):
        self.tokenize = tokenize
        self.preprocess = preprocess
        self.posting_list: Dict[str, List[int]] = {}
        self.documents: List[str] = []

    @staticmethod
    def intersect(posting_1: List[int], posting_2: List[int]) -> List[int]:
        intersection = []
        if not (posting_1 and posting_2):
            return intersection
        p1, p2 = 0, 0
        while p1 < len(posting_1) and p2 < len(posting_2):
            doc_1 = posting_1[p1]
            doc_2 = posting_2[p2]
            if doc_1 == doc_2:
                intersection.append(doc_1)
                p1 += 1
                p2 += 1
            elif doc_1 < doc_2:
                p1 += 1
            else:
                p2 += 1
        return intersection

    def index(self, documents: List[str]):
        for idx, document in enumerate(documents, len(self.documents)):
            self.documents.append(document)
            self.index_document(document, idx)

    def index_document(self, document: str, document_index: int) -> None:
        pass

    def search(self, query):
        query = self.tokenize(query)
        posting_list = []
        for token in map(self.preprocess, query):
            posting = self.posting_list.get(token, [])
            if posting_list and posting:
                posting_list = InvertedIndex.intersect(posting_list, posting)
            else:
                posting_list = posting
        return [self.documents[i] for i in posting_list]


class InMemoryInvertedIndex(InvertedIndex):
    def index_document(self, document: str, document_index: int) -> None:
        tokens = self.tokenize(document)
        for token in map(self.preprocess, tokens):
            posting = self.posting_list.setdefault(token, [])
            posting.append(document_index)
