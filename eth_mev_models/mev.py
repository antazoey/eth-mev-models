from typing import Union, Optional
from pydantic import BaseModel, Field

from eth_mev_models.common import ProtocolVersion, Refund, Privacy


class Inclusion(BaseModel):
    """
    Data used by block builders to check if the bundle should be considered for inclusion.
    """

    block: int
    """
    The first block the bundle is valid for.
    """

    max_block: Union[int, None] = Field(None, alias="maxBlock")
    """
    The last block the bundle is valid for.
    """


class BundleHashItem(BaseModel):
    """
    The hash of either a transaction or bundle we are trying to backrun.
    """

    hash: bytes
    """
    Tx hash.
    """


class BundleTxItem(BaseModel):
    """
    A new signed transaction.
    """

    tx: bytes
    """
    Bytes of the signed transaction.
    """

    can_revert: bool = Field(alias="canRevert")
    """
    If true, the transaction can revert without the bundle being considered invalid.
    """


class BundleNestedItem(BaseModel):
    """
    A nested bundle request.
    """

    bundle: "Bundle"
    """
    A bundle request of type Bundle
    """


class Validity(BaseModel):
    """
    Requirements for the bundle to be included in the block.
    """

    refund: Union[list[Refund], None] = None


class Bundle(BaseModel):
    """
    A bundle of transactions to send to the matchmaker.
    """

    version: ProtocolVersion
    """
    The version of the MEV-share API to use.
    """

    inclusion: Inclusion
    """
    Data used by block builders to check if the bundle should be considered for inclusion.
    """

    bundle_body: list[Union[BundleHashItem, BundleTxItem, BundleNestedItem]]
    """
    The transactions to include in the bundle.
    """

    validity: Optional[Validity] = None
    """
    Requirements for the bundle to be included in the block.
    """

    privacy: Optional[Privacy] = None
    """
    Preferences on what data should be shared about the bundle and its transactions
    """
