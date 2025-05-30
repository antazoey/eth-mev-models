from eth_pydantic_types.address import Address
from eth_pydantic_types.hex.bytes import HexBytes

from eth_mev_models.common import PrivacyHint
from eth_mev_models.mev import Bundle


def test_bundle():
    data_str = """
{
    "version": "v0.1",
    "inclusion": {
        "block": "0x1"
    },
    "body": [{
        "tx": "0x02f86b0180843b9aca00852ecc889a0082520894c87037874aed04e51c29f582394217a0a2b89d808080c080a0a463985c616dd8ee17d7ef9112af4e6e06a27b071525b42182fe7b0b5c8b4925a00af5ca177ffef2ff28449292505d41be578bebb77110dfc09361d2fb56998260",
        "canRevert": false
    }],
    "privacy": {
        "hints": [
          "calldata"
        ]
      },
      "validity": {
        "refundConfig": [
          {
            "address": "0x8EC1237b1E80A6adf191F40D4b7D095E21cdb18f",
            "percent": 100
          }
        ]
      }
}
""".strip()
    bundle = Bundle.model_validate_json(data_str)
    assert bundle.body[0].tx == HexBytes(
        "0x02f86b0180843b9aca00852ecc889a0082520894c87037874aed04e51c29f582394217a0a2b89d808080c080a0a463985c616dd8ee17d7ef9112af4e6e06a27b071525b42182fe7b0b5c8b4925a00af5ca177ffef2ff28449292505d41be578bebb77110dfc09361d2fb56998260"
    )
    assert bundle.privacy.hints == [PrivacyHint.CALLDATA]
    assert bundle.validity.refund_config[0].address == Address(
        "0x8EC1237b1E80A6adf191F40D4b7D095E21cdb18f"
    )

    bundle_dict = bundle.model_dump()
    assert (
        bundle_dict["body"][0]["tx"]
        == "0x02f86b0180843b9aca00852ecc889a0082520894c87037874aed04e51c29f582394217a0a2b89d808080c080a0a463985c616dd8ee17d7ef9112af4e6e06a27b071525b42182fe7b0b5c8b4925a00af5ca177ffef2ff28449292505d41be578bebb77110dfc09361d2fb56998260"
    )
    assert bundle_dict["privacy"]["hints"] == ["calldata"]
    assert (
        bundle_dict["validity"]["refundConfig"][0]["address"]
        == "0x8EC1237b1E80A6adf191F40D4b7D095E21cdb18f"
    )
