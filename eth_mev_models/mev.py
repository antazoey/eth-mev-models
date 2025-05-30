from typing import Union, Optional

from eth_pydantic_types.hex.bytes import HexBytes32, HexBytes
from eth_pydantic_types.address import Address
from eth_pydantic_types.hex.int import HexInt
from pydantic import Field
from eth_mev_models.basemodel import BaseModel

from eth_mev_models.common import ProtocolVersion, Refund, Privacy


class Inclusion(BaseModel):
    """
    Data used by block builders to check if the bundle should be considered for inclusion.
    """

    block: HexInt
    """
    The first block the bundle is valid for.
    """

    max_block: Union[HexInt, None] = Field(None, alias="maxBlock")
    """
    The last block the bundle is valid for.
    """


class BundleHashItem(BaseModel):
    """
    The hash of either a transaction or bundle we are trying to backrun.
    """

    hash: HexBytes32
    """
    Tx hash.
    """


class BundleTxItem(BaseModel):
    """
    A new signed transaction.
    """

    tx: HexBytes
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


class RefundConfig(BaseModel):
    """
    Specifies what addresses should receive what percent of the overall refund for this bundle,
    if it is enveloped by another bundle (e.g. a searcher backrun).
    """

    address: Address
    """
    The address to refund.
    """

    percent: int
    """
    The minimum percent of the bundle's earnings to redistribute.
    """


class Validity(BaseModel):
    """
    Requirements for the bundle to be included in the block.
    """

    refund: Union[list[Refund], None] = None
    """
    Specifies the minimum percent of a given bundle's earnings to redistribute
    for it to be included in a builder's block.
    """

    refund_config: Optional[list[RefundConfig]] = Field(None, alias="refundConfig")
    """
    Specifies what addresses should receive what percent of the overall refund for this bundle,
    if it is enveloped by another bundle (e.g. a searcher backrun).
    """


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

    body: list[Union[BundleHashItem, BundleTxItem, BundleNestedItem]]
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

    @classmethod
    def build_for_block(
        cls,
        block: HexInt,
        max_block: Optional[HexInt] = None,
        version: Optional[ProtocolVersion] = None,
        body: Optional[
            list[Union[BundleHashItem, BundleTxItem, BundleNestedItem]]
        ] = None,
        validity: Optional[Validity] = None,
        privacy: Optional[Privacy] = None,
    ) -> "Bundle":
        return cls(
            version=version or ProtocolVersion.V0_1,
            inclusion=Inclusion(block=block, max_block=max_block),
            body=body or [],
            validity=validity,
            privacy=privacy,
        )

    def add_tx(self, tx: HexBytes, can_revert: bool) -> "Bundle":
        self.body.append(BundleTxItem(tx=tx, can_revert=can_revert))

    def add_hash(self, hash: HexBytes32):
        self.body.append(BundleHashItem(hash=hash))

    def add_bundle(self, bundle: "Bundle"):
        self.body.append(BundleNestedItem(bundle=bundle))
