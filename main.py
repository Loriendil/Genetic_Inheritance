from abc import ABC, abstractmethod
import random
from typing import List

class Gene(ABC):

    def __init__(self, allele: str) -> None:
        self._allele = allele

    @abstractmethod
    def get_trait(self) -> str:
        pass


class DominantGene(Gene):
    def get_trait(self) -> str:
        return 'Dominant Expressed'


class RecessiveGene(Gene):
    def get_trait(self) -> str:
        return 'Recessive Expressed'


class Individual:
    def __init__(self, genes: List[Gene]) -> None:
        self._genes = genes

    def get_trait(self) -> str:
        # Тут сбоит логика, а не сама по себе код.
        # Нужно пересмотреть свои представления о наследовании
        dominant_probability: float = 0.5
        recessive_probability: float = 0.5
        rnd1 = random.random()
        rnd2 = random.random()
        if rnd1 < dominant_probability:
            return "Dominant trait expressed"
        elif rnd2 < recessive_probability:
            return "Recessive trait expressed"
        return "Unknown trait expressed"

first_gene: str = 'a'
second_gene: str = 'a'

genes: List[Gene] = [
    DominantGene(first_gene),
    RecessiveGene(second_gene)
]

individual = Individual(genes)
trait: str = individual.get_trait()

print(trait)