#!/usr/bin/env python3
"""Offline correctness tests. No network.

Runs recorded SOAP responses (`assets/fixtures/`) through the real
adapters via a fake session, and the captured registry dump through the
real provisioning path. Exits non-zero on the first failed assertion.

    python3 _selftest.py

Coverage is deliberately weighted toward the things that silently produce
wrong data rather than errors: the two Inventory versions, the two Product
Data versions, a supplier that omits every optional field, and the
distinction between "quantity is zero" and "quantity is absent".
"""

from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import adapters  # noqa: E402
import registry  # noqa: E402
import soap  # noqa: E402
from client import PromoStandardsClient  # noqa: E402
from config import SupplierConfig  # noqa: E402
from errors import (  # noqa: E402
    ConfigError,
    EscalationRequired,
    NotSupportedError,
    ServiceMessageError,
    SoapFaultError,
    TransportError,
)

FIXTURES = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "assets", "fixtures",
)

_PASSED = 0


def fixture(name: str) -> str:
    with open(os.path.join(FIXTURES, name), encoding="utf-8") as handle:
        return handle.read()


class FakeResponse:
    def __init__(self, text: str, status: int = 200) -> None:
        self.text = text
        self.status_code = status


class FakeSession:
    """Returns canned XML and records what was sent."""

    def __init__(self, text: str = "", status: int = 200,
                 raises: Exception | None = None) -> None:
        self.text = text
        self.status = status
        self.raises = raises
        self.calls: list[dict] = []

    def post(self, url, data, headers, timeout=None):
        self.calls.append({"url": url, "body": data, "headers": headers})
        if self.raises:
            raise self.raises
        return FakeResponse(self.text, self.status)

    @property
    def last_body(self) -> str:
        return self.calls[-1]["body"] if self.calls else ""


def check(condition: bool, label: str) -> None:
    global _PASSED
    if not condition:
        print(f"FAIL: {label}", file=sys.stderr)
        sys.exit(1)
    _PASSED += 1


def expect_raises(exc_type, fn, label: str):
    try:
        fn()
    except exc_type as exc:
        global _PASSED
        _PASSED += 1
        return exc
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL: {label} — raised {type(exc).__name__}: {exc}",
              file=sys.stderr)
        sys.exit(1)
    print(f"FAIL: {label} — nothing raised", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# config
# ---------------------------------------------------------------------------

def config_for(services: dict, supplier: str = "testco") -> SupplierConfig:
    os.environ["PS_TEST_ID"] = "test-user"
    os.environ["PS_TEST_PASSWORD"] = "test-secret"
    return SupplierConfig.from_dict({
        "supplier": supplier,
        "credentials": {"id": "${PS_TEST_ID}", "password": "${PS_TEST_PASSWORD}"},
        "services": services,
    })


def test_config() -> None:
    config = config_for({
        "INV": {"url": "https://a.invalid/inv", "wsVersion": "2.0.0"},
        "PO": {"url": "https://a.invalid/po", "wsVersion": "1.0.0",
               "testUrl": "https://test.invalid/po"},
    })
    check(config.credential_id == "test-user", "credentials resolve from env")
    check(config.supports("INV"), "INV supported")
    check(not config.supports("MED"), "MED not configured")

    # Per-service map: each service keeps its own URL and version.
    check(config.endpoint("INV").url != config.endpoint("PO").url,
          "per-service URLs are independent")
    check(config.endpoint("INV").ws_version == "2.0.0", "per-service version")

    # "PROD" is a common mis-spelling of the registry's "Product".
    check(config_for({"PROD": {"url": "https://x.invalid", "wsVersion": "2.0.0"}})
          .supports("PRODUCT"), "PROD alias normalises to PRODUCT")

    # A literal secret in a config file is refused, not used.
    expect_raises(
        ConfigError,
        lambda: SupplierConfig.from_dict({
            "supplier": "x",
            "credentials": {"id": "hunter2", "password": "${PS_TEST_PASSWORD}"},
            "services": {"INV": {"url": "https://x.invalid",
                                 "wsVersion": "2.0.0"}},
        }),
        "literal credential in config is rejected",
    )

    # An unconfigured service raises before any request is built.
    exc = expect_raises(NotSupportedError, lambda: config.endpoint("PPC"),
                        "unconfigured service raises NotSupportedError")
    check("INV" in exc.available, "NotSupportedError lists what is available")

    # Missing env var names the variable without printing a value.
    os.environ.pop("PS_MISSING_ID", None)
    bare = SupplierConfig.from_dict({
        "supplier": "x",
        "credentials": {"id": "${PS_MISSING_ID}"},
        "services": {"INV": {"url": "https://x.invalid", "wsVersion": "2.0.0"}},
    })
    exc = expect_raises(ConfigError, bare.require_credentials,
                        "missing credential env var raises")
    check("PS_MISSING_ID" in str(exc), "error names the env var")


# ---------------------------------------------------------------------------
# inventory — the two versions
# ---------------------------------------------------------------------------

def test_inventory_2_0_0() -> None:
    session = FakeSession(fixture("inventory_2_0_0_full.xml"))
    config = config_for({"INV": {"url": "https://a.invalid/inv",
                                 "wsVersion": "2.0.0"}})
    result = PromoStandardsClient(config, session=session).get_inventory("PC61")

    check(result.product_id == "PC61", "2.0.0 product id")
    check(len(result.levels) == 2, "2.0.0 parses both parts")

    first = result.levels[0]
    check(first.part_id == "PC61-BLK-S", "2.0.0 partId (lowercase d)")
    check(first.color == "Black", "2.0.0 partColor -> color")
    check(first.size == "S", "2.0.0 labelSize -> size")
    check(first.quantity == 1543.0, "2.0.0 quantity from Quantity/value")
    check(first.uom == "EA", "2.0.0 uom from Quantity/uom")
    check(first.lead_time_days == 7, "2.0.0 replenishmentLeadTime")
    check(first.locations_supported is True, "2.0.0 reports location support")
    check(len(first.locations) == 2, "2.0.0 parses both warehouses")
    check(first.locations[0].name == "Seattle", "2.0.0 warehouse name")
    check(first.locations[0].quantity == 1200.0, "2.0.0 warehouse quantity")
    check(first.locations[1].postal_code is None,
          "2.0.0 absent warehouse postcode stays None")

    # Zero is data, not absence: this distinction drives reorder decisions.
    second = result.levels[1]
    check(second.quantity == 0.0, "2.0.0 zero quantity parses as 0.0")
    check(second.quantity is not None, "2.0.0 zero is not None")
    check(second.locations == [], "2.0.0 part without warehouses")
    check(second.buy_to_order is True, "2.0.0 buyToOrder boolean")

    # Request shape.
    body = session.last_body
    check("GetInventoryLevelsRequest" in body, "2.0.0 request root element")
    check("http://www.promostandards.org/WSDL/Inventory/2.0.0/" in body,
          "2.0.0 service namespace")
    check("shar:wsVersion>2.0.0<" in body, "2.0.0 wsVersion in shared ns")
    check("shar:productId" in body, "2.0.0 productId in shared ns")


def test_inventory_1_2_1() -> None:
    session = FakeSession(fixture("inventory_1_2_1_full.xml"))
    config = config_for({"INV": {"url": "https://a.invalid/inv",
                                 "wsVersion": "1.2.1"}})
    result = PromoStandardsClient(config, session=session).get_inventory("PC61")

    check(result.product_id == "PC61", "1.2.1 productID (capital D)")
    check(len(result.levels) == 2, "1.2.1 parses both variations")

    first = result.levels[0]
    check(first.part_id == "PC61-BLK-S", "1.2.1 partID -> part_id")
    check(first.color == "Black", "1.2.1 attributeColor -> color")
    check(first.size == "S", "1.2.1 attributeSize -> size")
    check(first.quantity == 1543.0, "1.2.1 scalar quantityAvailable")

    # The capability gap that must not look like an empty warehouse list.
    check(first.locations == [], "1.2.1 has no warehouse data")
    check(first.locations_supported is False,
          "1.2.1 flags that locations are unavailable in this version")
    check(first.uom is None, "1.2.1 has no uom element; not assumed to be EA")

    # The namespace trap: 1.2.1 declares InventoryService/1.0.0.
    body = session.last_body
    check("http://www.promostandards.org/WSDL/InventoryService/1.0.0/" in body,
          "1.2.1 uses the InventoryService/1.0.0 namespace, not 1.2.1")
    check("/WSDL/Inventory/1.2.1/" not in body,
          "1.2.1 does not interpolate its version into the namespace")
    check("<ns:Request>" in body, "1.2.1 request root is <Request>")
    check("productIDtype" in body, "1.2.1 sends the required productIDtype")
    check("ns:wsVersion>1.2.1<" in body,
          "1.2.1 wsVersion is the service version, in the single namespace")


def test_inventory_version_divergence() -> None:
    """Same call, both versions: identical canonical shape, different wires."""
    config_2 = config_for({"INV": {"url": "https://a.invalid",
                                   "wsVersion": "2.0.0"}})
    config_1 = config_for({"INV": {"url": "https://a.invalid",
                                   "wsVersion": "1.2.1"}})
    session_2 = FakeSession(fixture("inventory_2_0_0_full.xml"))
    session_1 = FakeSession(fixture("inventory_1_2_1_full.xml"))

    result_2 = PromoStandardsClient(config_2, session=session_2).get_inventory("PC61")
    result_1 = PromoStandardsClient(config_1, session=session_1).get_inventory("PC61")

    for a, b in zip(result_2.levels, result_1.levels):
        check(a.part_id == b.part_id, "both versions agree on part_id")
        check(a.color == b.color, "both versions agree on color")
        check(a.quantity == b.quantity, "both versions agree on quantity")

    check(set(result_2.to_dict()) == set(result_1.to_dict()),
          "canonical keys identical across versions")
    check(session_2.last_body != session_1.last_body,
          "the wire format genuinely differs")


def test_sparse_supplier() -> None:
    """A supplier that omits every optional field must parse, not crash."""
    session = FakeSession(fixture("inventory_2_0_0_sparse.xml"))
    config = config_for({"INV": {"url": "https://a.invalid",
                                 "wsVersion": "2.0.0"}})
    result = PromoStandardsClient(config, session=session).get_inventory("MINIMAL-1")

    check(len(result.levels) == 1, "sparse supplier yields one level")
    level = result.levels[0]
    check(level.part_id == "MINIMAL-1-A", "sparse required field present")
    check(level.quantity is None, "sparse quantity is None, not 0")
    check(level.color is None and level.size is None, "sparse attributes None")
    check(level.locations == [], "sparse locations empty")
    check(level.to_dict()["description"] is None,
          "canonical shape still emits every key")


def test_inventory_errors() -> None:
    config_2 = config_for({"INV": {"url": "https://a.invalid",
                                   "wsVersion": "2.0.0"}})
    config_1 = config_for({"INV": {"url": "https://a.invalid",
                                   "wsVersion": "1.2.1"}})

    # 2.x channel: ServiceMessageArray with severity.
    session = FakeSession(fixture("inventory_2_0_0_error.xml"))
    exc = expect_raises(
        ServiceMessageError,
        lambda: PromoStandardsClient(config_2, session=session).get_inventory("X"),
        "2.0.0 ServiceMessage error raises",
    )
    check(exc.code == "110", "2.0.0 error carries the supplier's code")

    # 1.x channel: a bare errorMessage element.
    session = FakeSession(fixture("inventory_1_2_1_error.xml"))
    exc = expect_raises(
        ServiceMessageError,
        lambda: PromoStandardsClient(config_1, session=session).get_inventory("X"),
        "1.2.1 errorMessage raises",
    )
    check("Invalid product" in str(exc), "1.2.1 error text preserved")

    # SOAP faults surface as faults, not as empty results.
    session = FakeSession(fixture("soap_fault.xml"), status=500)
    exc = expect_raises(
        SoapFaultError,
        lambda: PromoStandardsClient(config_2, session=session).get_inventory("X"),
        "SOAP fault raises",
    )
    check("Authentication failed" in str(exc), "fault string preserved")

    # A non-XML body is a transport problem, not a parse crash. Retries are
    # disabled here so the test does not sit through the real backoff.
    client = PromoStandardsClient(
        config_2, session=FakeSession("502 Bad Gateway", status=502)
    )
    client.soap.retries = 1
    expect_raises(TransportError, lambda: client.get_inventory("X"),
                  "non-XML body raises TransportError")


# ---------------------------------------------------------------------------
# product data — the two versions
# ---------------------------------------------------------------------------

def test_product_2_0_0() -> None:
    session = FakeSession(fixture("product_2_0_0_full.xml"))
    config = config_for({"PRODUCT": {"url": "https://a.invalid",
                                     "wsVersion": "2.0.0"}})
    product = PromoStandardsClient(config, session=session).get_product("PC61")

    check(product.product_id == "PC61", "2.0.0 productId")
    check(product.name == "Essential Tee", "2.0.0 productName")
    check(product.brand == "Port & Company", "2.0.0 unescapes entities")
    check(len(product.description) == 2, "2.0.0 repeated description elements")
    check("tee" in product.keywords, "2.0.0 keywords")
    check(product.categories[0]["sub_category"] == "T-Shirts", "2.0.0 category")
    check(product.primary_image_url == "https://example.invalid/pc61.jpg",
          "2.0.0-only primaryImageUrl")
    check(len(product.parts) == 1, "2.0.0 parses parts")

    part = product.parts[0]
    check(part.part_id == "PC61-BLK-S", "2.0.0 part id")
    check(part.color == "Black", "2.0.0 nested primaryColor/colorName")
    check(part.size == "S", "2.0.0 nested ApparelSize/labelSize")
    check(part.gtin == "00191265000015", "2.0.0 gtin")
    check(part.weight == 0.35, "2.0.0 weight from Dimension")
    check(part.dimensions["uom"] == "IN", "2.0.0 dimension uom")

    body = session.last_body
    check("localizationCountry>US<" in body, "2.0.0 sends required localization")
    check("/ProductDataService/2.0.0/" in body, "2.0.0 namespace")


def test_product_1_0_0_sparse() -> None:
    session = FakeSession(fixture("product_1_0_0_sparse.xml"))
    config = config_for({"PRODUCT": {"url": "https://a.invalid",
                                     "wsVersion": "1.0.0"}})
    product = PromoStandardsClient(config, session=session).get_product("BARE-1")

    check(product.product_id == "BARE-1", "1.0.0 productId")
    check(product.name == "Unadorned Item", "1.0.0 productName")
    check(product.brand is None, "1.0.0 absent brand is None")
    check(product.description == [], "1.0.0 absent descriptions empty")
    check(len(product.parts) == 1, "1.0.0 part parsed despite bare payload")
    check(product.parts[0].color is None, "1.0.0 absent colour is None")
    check(product.primary_image_url is None,
          "1.0.0 has no primaryImageUrl and does not invent one")

    body = session.last_body
    check("/ProductDataService/1.0.0/" in body, "1.0.0 namespace")


# ---------------------------------------------------------------------------
# purchase order — the write path
# ---------------------------------------------------------------------------

SAMPLE_PO = {
    "order_number": "PO-1001",
    "order_date": "2026-08-12T00:00:00Z",
    "total_amount": "125.00",
    "currency": "USD",
    "shipments": [{"shipment_id": "1", "address": {
        "company": "BaconCo", "address1": "1 Main St", "city": "Knoxville",
        "state": "TN", "postal_code": "37902", "country": "US"}}],
    "lines": [{"line_number": 1, "description": "Essential Tee",
               "quantity": 25, "unit_price": "5.00", "line_total": "125.00",
               "product_id": "PC61"}],
}

PO_SERVICES = {"PO": {"url": "https://prod.invalid/po", "wsVersion": "1.0.0",
                      "testUrl": "https://test.invalid/po"}}
PO_NO_TEST = {"PO": {"url": "https://prod.invalid/po", "wsVersion": "1.0.0"}}


def test_purchase_order() -> None:
    # Default target is the test endpoint — production is opt-in.
    session = FakeSession(fixture("po_accepted.xml"))
    client = PromoStandardsClient(config_for(PO_SERVICES), session=session)
    result = client.send_purchase_order(SAMPLE_PO)
    check(result.accepted is True, "accepted PO reports accepted=True")
    check(result.sales_order_number == "SO-99812", "transactionId captured")
    check(result.is_test is True, "defaults to the test endpoint")
    check(session.calls[-1]["url"] == "https://test.invalid/po",
          "test URL actually used by default")

    # Production requires the explicit flag.
    session = FakeSession(fixture("po_accepted.xml"))
    client = PromoStandardsClient(config_for(PO_SERVICES), session=session)
    result = client.send_purchase_order(SAMPLE_PO, allow_production=True)
    check(session.calls[-1]["url"] == "https://prod.invalid/po",
          "allow_production reaches the production URL")
    check(result.is_test is False, "production submission flagged")

    # No test endpoint: refuse rather than silently hit production.
    session = FakeSession(fixture("po_accepted.xml"))
    client = PromoStandardsClient(config_for(PO_NO_TEST), session=session)
    expect_raises(
        ConfigError,
        lambda: client.send_purchase_order(SAMPLE_PO),
        "missing test endpoint refuses instead of using production",
    )
    check(session.calls == [], "nothing was sent when the test URL is missing")

    # An explicit rejection is a result, not an escalation.
    session = FakeSession(fixture("po_rejected.xml"))
    client = PromoStandardsClient(config_for(PO_SERVICES), session=session)
    result = client.send_purchase_order(SAMPLE_PO)
    check(result.accepted is False, "rejected PO reports accepted=False")
    check(result.messages and result.messages[0]["code"] == "300",
          "rejection carries the supplier's message")

    # An ambiguous transport failure escalates and does not retry.
    session = FakeSession(raises=OSError("connection reset"))
    client = PromoStandardsClient(config_for(PO_SERVICES), session=session)
    exc = expect_raises(
        EscalationRequired,
        lambda: client.send_purchase_order(SAMPLE_PO),
        "transport failure during sendPO escalates",
    )
    check(exc.po_number == "PO-1001", "escalation names the PO")
    check(exc.as_dict()["action"] == "escalate_to_human",
          "escalation is machine-readable")
    check(len(session.calls) == 1, "sendPO is never retried")

    # A dry run renders the payload without sending.
    session = FakeSession(fixture("po_accepted.xml"))
    client = PromoStandardsClient(config_for(PO_SERVICES), session=session)
    xml = client.preview_purchase_order(SAMPLE_PO)
    check("<ns:PO>" in xml and "PO-1001" in xml, "preview renders the PO")
    check(session.calls == [], "preview sends nothing")

    # Structural validation happens before anything leaves.
    expect_raises(
        ConfigError,
        lambda: client.preview_purchase_order(
            {**SAMPLE_PO, "lines": []}
        ),
        "PO with no line items is refused",
    )
    expect_raises(
        ConfigError,
        lambda: client.preview_purchase_order(
            {**SAMPLE_PO, "shipments": []}
        ),
        "PO with no shipment is refused",
    )


# ---------------------------------------------------------------------------
# soap helpers
# ---------------------------------------------------------------------------

def test_soap_helpers() -> None:
    # Absent optional fields are omitted, not sent empty.
    check(soap.element("ns:password", None) == "", "None renders nothing")
    check(soap.element("ns:password", "") == "", "empty string renders nothing")
    check(soap.element("ns:id", "x&y") == "<ns:id>x&amp;y</ns:id>",
          "values are escaped")

    os.environ["PS_TEST_ID"] = "test-user"
    os.environ.pop("PS_TEST_PASSWORD", None)
    config = SupplierConfig.from_dict({
        "supplier": "x",
        "credentials": {"id": "${PS_TEST_ID}",
                        "password": "${PS_TEST_PASSWORD}"},
        "services": {"INV": {"url": "https://a.invalid", "wsVersion": "2.0.0"}},
    })
    session = FakeSession(fixture("inventory_2_0_0_full.xml"))
    PromoStandardsClient(config, session=session).get_inventory("PC61")
    check("password" not in session.last_body,
          "unset password is omitted entirely, not sent as an empty element")
    os.environ["PS_TEST_PASSWORD"] = "test-secret"

    # Numbers that will not parse are absent, never coerced to zero.
    import xml.etree.ElementTree as ET
    node = ET.fromstring("<a><q>N/A</q><z>0</z></a>")
    check(soap.number(node, "q") is None, "unparseable number is None")
    check(soap.number(node, "z") == 0.0, "zero parses as zero")


# ---------------------------------------------------------------------------
# registry / provisioning (offline, from the captured dump)
# ---------------------------------------------------------------------------

def test_registry() -> None:
    dump = registry.load_dump()
    check(len(dump.get("companies") or {}) > 1000,
          "dump holds the full company list")

    capabilities = registry.capabilities_for("SanMar", dump=dump)
    check(capabilities, "SanMar has capabilities")
    services = {c.service for c in capabilities}
    check("INV" in services and "PRODUCT" in services, "SanMar services found")

    # SanMar publishes Inventory at both versions; provisioning takes 2.0.0.
    inv_versions = {c.version for c in capabilities if c.service == "INV"}
    check(inv_versions == {"1.2.1", "2.0.0"}, "both INV versions listed")
    best = registry.best_endpoints(capabilities)
    check(best["INV"].version == "2.0.0", "newest drivable version chosen")

    # A published service with no adapter is reported, not hidden.
    unsupported = [c for c in capabilities if not c.supported]
    check(unsupported, "unsupported services are reported, not dropped")
    check(all(c.operations == [] for c in unsupported),
          "unsupported services expose no operations")

    # Case-insensitive company lookup.
    code, _ = registry.find_company(dump, "sanmar")
    check(code == "SanMar", "company lookup is case-insensitive")
    expect_raises(ConfigError, lambda: registry.find_company(dump, "nope-xyz"),
                  "unknown company raises")

    summary = registry.summarize(capabilities)
    check("INV" in summary["capabilities"], "summary lists capabilities")
    check("getInventoryLevels" in summary["operations"], "summary lists ops")


def test_provisioning() -> None:
    import provision

    config_dict = provision.build_config("SanMar")
    check(config_dict["supplier"] == "SanMar", "provisioned supplier code")
    check(config_dict["credentials"]["id"] == "${PS_SANMAR_ID}",
          "credentials are env references, never values")
    check("INV" in config_dict["services"], "INV provisioned")
    check(config_dict["services"]["INV"]["wsVersion"] == "2.0.0",
          "provisioned with the drivable version")
    check(config_dict["services"]["INV"].get("testUrl"),
          "test endpoint captured where registered")

    # The generated config must load through the real config path.
    # Distinctive sentinels: a short value would collide with substrings of
    # the URLs (an "x" or "y" occurs inside "Inventory") and pass vacuously.
    os.environ["PS_SANMAR_ID"] = "sentinel-id-8f21"
    os.environ["PS_SANMAR_PASSWORD"] = "sentinel-secret-4b7c"
    loaded = SupplierConfig.from_dict(config_dict)
    check(loaded.supports("INV"), "generated config loads")
    check(loaded.describe()["credentials"]["id"] is True,
          "describe() reports presence, not the value")
    rendered = str(loaded.describe())
    check("sentinel-secret-4b7c" not in rendered,
          "describe() never leaks the password")
    check("sentinel-id-8f21" not in rendered,
          "describe() never leaks the credential id")

    report = provision.validate(config_dict)
    check(report["valid"] is True, "generated config validates")

    for name in ("PS_SANMAR_ID", "PS_SANMAR_PASSWORD"):
        os.environ.pop(name, None)


def test_runtime_injected_credentials() -> None:
    """The delegated path: a committed config, an environment filled later.

    On a delegated agent-to-agent turn the platform injects the calling
    agent's credentials into this process's environment before the script
    runs. Nothing hands them to the skill directly — so what has to hold is
    that a config written with `${ENV_VAR}` references, and committed long
    before any caller existed, picks up whatever the environment holds at
    load time and puts it on the wire.
    """
    endpoints = {"INV": {"url": "https://a.invalid", "wsVersion": "2.0.0"}}
    raw = {
        "supplier": "SanMar",
        "credentials": {"id": "${PS_DELEGATED_ID}",
                        "password": "${PS_DELEGATED_PASSWORD}"},
        "services": endpoints,
    }

    # Before injection: the references resolve to nothing and the call is
    # refused, naming the env var an operator has to bind.
    os.environ.pop("PS_DELEGATED_ID", None)
    os.environ.pop("PS_DELEGATED_PASSWORD", None)
    unfilled = SupplierConfig.from_dict(raw)
    check(unfilled.credential_id is None, "unset env resolves to no identity")
    check(unfilled.credential_env["id"] == "PS_DELEGATED_ID",
          "env var name kept for diagnostics")
    exc = expect_raises(ConfigError, unfilled.require_credentials,
                        "an unfilled environment refuses the call")
    check("PS_DELEGATED_ID" in str(exc), "the error names the missing env var")

    # The runtime injects the caller's credentials, then the script runs.
    os.environ["PS_DELEGATED_ID"] = "caller-alice"
    os.environ["PS_DELEGATED_PASSWORD"] = "secret-alice"
    filled = SupplierConfig.from_dict(raw)
    check(filled.credential_id == "caller-alice", "injected id resolves")
    check(filled.credential_source == "environment", "source recorded")

    session = FakeSession(fixture("inventory_2_0_0_full.xml"))
    PromoStandardsClient(filled, session=session).get_inventory("PC61")
    body = session.last_body
    check("caller-alice" in body, "injected id sent")
    check("secret-alice" in body, "injected password sent")

    # describe() is what an operator reads; it must never leak the value.
    described = filled.describe()
    check(described["credentials"]["id"] is True, "presence reported")
    check("caller-alice" not in json.dumps(described),
          "describe() never echoes a credential value")

    # A second caller's turn is a second process with a different
    # environment. Same committed config, different identity on the wire.
    os.environ["PS_DELEGATED_ID"] = "caller-bob"
    os.environ["PS_DELEGATED_PASSWORD"] = "secret-bob"
    session = FakeSession(fixture("inventory_2_0_0_full.xml"))
    PromoStandardsClient(SupplierConfig.from_dict(raw),
                         session=session).get_inventory("PC61")
    check("caller-bob" in session.last_body, "second caller's identity sent")
    check("caller-alice" not in session.last_body,
          "no trace of the first caller")

    # A literal secret in the credentials block stays rejected: that block
    # is the shape that gets committed.
    expect_raises(
        ConfigError,
        lambda: SupplierConfig.from_dict({
            "supplier": "x",
            "credentials": {"id": "literal-in-config"},
            "services": endpoints,
        }),
        "literal credential in the config block is rejected",
    )

    # A config with no credentials block cannot authenticate at all — there
    # is no env var for the runtime to inject into.
    bare = SupplierConfig.from_dict({"supplier": "SanMar",
                                     "services": endpoints})
    check(bare.credential_source == "none", "no credentials configured")
    exc = expect_raises(ConfigError, bare.require_credentials,
                        "a config without a credentials block refuses")
    check("no 'credentials' block" in str(exc),
          "the error explains there is nowhere to inject")

    os.environ.pop("PS_DELEGATED_ID", None)
    os.environ.pop("PS_DELEGATED_PASSWORD", None)


def test_namespace_override() -> None:
    """Non-compliant suppliers can override the request namespace.

    Taken from a live WSDL sample: 3M serves Inventory 1.2.1 under
    `http://inventoryservice.promostandards.mmm/` rather than the spec's
    namespace. Responses parse regardless (local-name matching), but the
    request has to match or the service rejects it.
    """
    custom = "http://inventoryservice.promostandards.mmm/"
    session = FakeSession(fixture("inventory_1_2_1_full.xml"))
    config = config_for({"INV": {
        "url": "https://a.invalid", "wsVersion": "1.2.1",
        "namespaces": {"ns": custom},
    }})
    result = PromoStandardsClient(config, session=session).get_inventory("PC61")

    check(custom in session.last_body, "override namespace used in request")
    check("/WSDL/InventoryService/1.0.0/" not in session.last_body,
          "spec namespace replaced, not appended")
    check(len(result.levels) == 2,
          "response still parses — parsing ignores namespaces")

    # Without an override the spec namespace is still the default.
    session = FakeSession(fixture("inventory_1_2_1_full.xml"))
    plain = config_for({"INV": {"url": "https://a.invalid",
                                "wsVersion": "1.2.1"}})
    PromoStandardsClient(plain, session=session).get_inventory("PC61")
    check("/WSDL/InventoryService/1.0.0/" in session.last_body,
          "default namespace unchanged when no override is configured")

    expect_raises(
        ConfigError,
        lambda: SupplierConfig.from_dict({
            "supplier": "x", "credentials": {"id": "${PS_TEST_ID}"},
            "services": {"INV": {"url": "https://a.invalid",
                                 "wsVersion": "2.0.0",
                                 "namespaces": "not-an-object"}},
        }),
        "malformed namespaces override is rejected",
    )


def test_adapter_registry() -> None:
    check(adapters.versions_for("INV") == ["1.2.1", "2.0.0"],
          "both inventory adapters registered")
    check(adapters.versions_for("PRODUCT") == ["1.0.0", "2.0.0"],
          "both product adapters registered")

    # A version we cannot drive fails loudly, naming what exists — it is
    # never served by a near-miss adapter.
    exc = expect_raises(
        NotSupportedError,
        lambda: adapters.get_adapter_class("INV", "1.0.0"),
        "unimplemented version raises",
    )
    check("1.2.1" in exc.available, "error names the implemented versions")
    expect_raises(NotSupportedError,
                  lambda: adapters.get_adapter_class("MED", "1.1.0"),
                  "unimplemented service raises")

    # Every adapter's namespace is a constant, never built from wsVersion.
    for (service, version), cls in adapters.ADAPTERS.items():
        check(bool(cls.NAMESPACES), f"{service} {version} declares namespaces")
        check(cls.VERSION == version, f"{service} {version} version matches key")
        check(bool(cls.OPERATIONS), f"{service} {version} declares operations")

    # The specific trap: Inventory 1.2.1's namespace says 1.0.0.
    ns = adapters.ADAPTERS[("INV", "1.2.1")].NAMESPACES["ns"]
    check(ns.endswith("/InventoryService/1.0.0/"),
          "INV 1.2.1 namespace is hardcoded to InventoryService/1.0.0")


def main() -> int:
    tests = [
        test_config,
        test_inventory_2_0_0,
        test_inventory_1_2_1,
        test_inventory_version_divergence,
        test_sparse_supplier,
        test_inventory_errors,
        test_product_2_0_0,
        test_product_1_0_0_sparse,
        test_purchase_order,
        test_soap_helpers,
        test_runtime_injected_credentials,
        test_namespace_override,
        test_registry,
        test_provisioning,
        test_adapter_registry,
    ]
    for test in tests:
        test()
        print(f"  ok  {test.__name__}")
    print(f"\n{_PASSED} assertions passed across {len(tests)} tests")
    return 0


if __name__ == "__main__":
    sys.exit(main())
