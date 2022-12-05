import abc
import dataclasses
import enum
from types import NoneType
from typing import TypeVar, Set


@dataclasses.dataclass
class Product:
    """
    Un article dans sa forme la plus simple (un nom, un prix, un code)
    """

    name: str
    price: float
    barecode: str = None

SET_PO = TypeVar('SET_PO', bound=set["PurchaseOrder"], covariant=True)
class PurchaseManager(SET_PO):
    """ Simple conteneur de commande d'achat"""


class PurchaseOrder(abc.ABC):
    """
    Cette class represente une commande d'achat.
    Elle peut être dans 2 état distinct (Brouillon-> DRAFT, ou Terminé -> DONE)
    Quand elle est brouillon il est possible d'ajouter des article ou de les supprimers, mais quand elle est Terminée
    """

    class State(enum.StrEnum):
        """
        Les état de la commande d'achat
        """

        DRAFT = "DRAFT"
        DONE = "DONE"

    def __init__(self, name: str, state: State = State.DRAFT):
        """
        Constructeur d'une commande d'achat
        :param name: Le nom de la commande
        :param state: Le status, nom modifiable apres instanciation
        """
        self.name = name
        self.state = state

    @abc.abstractmethod
    def add_product(self, product: Product, qty: float = 1) -> float:
        """
        Ajoute un article dans la commande d'achat, la quantité peut être prisée, mais par defaut c'est "1"
        Si l'article est deja dans la liste alors uniquement la quantité est changée
        :param product: L'instance de l'article à ajouter
        :param qty: La quantité ou 1 par defaut
        :return: La nouvelle quantité dans la liste
        """

    @abc.abstractmethod
    def clear(self) -> NoneType:
        """
        Supprime tous les articles dans cette liste
        """

    @abc.abstractmethod
    def remove_product(self, product: Product) -> float:
        """
        Supprime l'article en parametre de la list
        :param product: L'article a supprimer
        :return: La quantité de l'article qu'il y avait dans la liste
        """

    @abc.abstractmethod
    def get_price(self) -> float:
        """
        Retourne le prix total de cette liste, prix de l'article fois le nombre.
        :return: Le prix total ou 0 si pas d'article
        """

    @abc.abstractmethod
    def __repr__(self) -> str:
        """
        Une representation textuel de la liste
        :return: un string montant le contenue de la commande d'achat
        """

    @abc.abstractmethod
    def __eq__(self, other: "PurchaseOrder") -> bool:
        """
        Une commande est considérée comme égale si elle contient le même code et a le même total
        :param other: la commande d'achat à comparer
        :return: vrai ou faux
        """

    @abc.abstractmethod
    def confirm_order(self) -> "PurchaseOrder":
        """
        Retourne une nouvelle liste dont le status sera a DONE
        """
