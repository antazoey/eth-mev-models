from typing import Optional

from pydantic import BaseModel
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

    body_idx: int
    """
    The index of the transaction in the bundle.
    """

    percent: int
    """
    The minimum percent of the bundle's earnings to redistribute.
    """


class PrivacyHint(BaseModel):
    """
    Hints on what data should be shared about the bundle and its transactions.
    """

    calldata: bool
    """
    The calldata of the bundle's transactions should be shared.
    """

    contract_address: bool
    """
    The address of the bundle's transactions should be shared.
    """

    logs: bool
    """
    The logs of the bundle's transactions should be shared.
    """

    function_selector: bool
    """
    The function selector of the bundle's transactions should be shared.
    """

    hash: bool
    """
    The hash of the bundle's transactions should be shared.
    """

    tx_hash: bool
    """
    The hash of the bundle should be shared.
    """


class Privacy(BaseModel):
    """
    Preferences on what data should be shared about the bundle and its transactions
    """

    hints: Optional[PrivacyHint] = None
    """
    Hints on what data should be shared about the bundle and its transactions.
    """

    builders: Optional[list[str]] = None
    """
    Names of the builders that should be allowed to see the bundle/transaction.
    """
