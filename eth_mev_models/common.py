from typing import Optional

from eth_pydantic_types.hex.int import HexInt
from eth_mev_models.basemodel import BaseModel
from enum import Enum


class ProtocolVersion(str, Enum):
    """
    The version of the MEV-share API to use.
    """

    BETA1 = "beta-1"
    """
    The beta-1 version of the API.
    """

    V0_1 = "v0.1"
    """
    The 0.1 version of the API.
    """


class Refund(BaseModel):
    """
    Specifies the minimum percent of a given bundle's earnings to redistribute for it to be included
    in a builder's block.
    """

    body_idx: HexInt
    """
    The index of the transaction in the bundle.
    """

    percent: HexInt
    """
    The minimum percent of the bundle's earnings to redistribute.
    """


class PrivacyHint(str, Enum):
    """
    Hints on what data should be shared about the bundle and its transactions.
    """

    CALLDATA = "calldata"
    """
    The calldata of the bundle's transactions should be shared.
    """

    CONTRACT_ADDRESS = "contract_address"
    """
    The address of the bundle's transactions should be shared.
    """

    LOGS = "logs"
    """
    The logs of the bundle's transactions should be shared.
    """

    FUNCTION_SELECTOR = "function_selector"
    """
    The function selector of the bundle's transactions should be shared.
    """

    HASH = "hash"
    """
    The hash of the bundle's transactions should be shared.
    """

    TX_HASH = "tx_hash"
    """
    The hash of the bundle should be shared.
    """


class Privacy(BaseModel):
    """
    Preferences on what data should be shared about the bundle and its transactions
    """

    hints: Optional[list[PrivacyHint]] = None
    """
    Hints on what data should be shared about the bundle and its transactions.
    """

    builders: Optional[list[str]] = None
    """
    Names of the builders that should be allowed to see the bundle/transaction.
    """
