"""v2.11 — Iranian-suppliers-ONLY enforcement.

The database's hard scope rule is that every supplier is Iranian. These tests
lock that rule down at both entry paths (web discovery and the social/Telegram
catalogue) and, just as importantly, protect the legitimate Iranian importers
that a naive "reject anything foreign-sounding" filter would destroy.
"""
from __future__ import annotations

import pytest

from src.discovery.country_gate import (ADMIT_FAMILIES, IRAN,
                                        ForeignSupplierRejected,
                                        assert_iranian, collect_disqualifiers,
                                        collect_evidence, evaluate,
                                        is_iranian_ip, registrable_domain,
                                        score_evidence)
from src.discovery.social_seed_list import (FOREIGN_CHANNELS, SOCIAL_CHANNELS,
                                            active_channels, channel_country,
                                            country_provenance,
                                            is_foreign_channel,
                                            is_iranian_channel)

# ---------------------------------------------------------------------------
# Default deny
# ---------------------------------------------------------------------------


def test_no_evidence_is_denied():
    v = evaluate(url="https://unknown.com", content="Chemicals for sale.")
    assert v.admitted is False
    assert v.country is None
    assert "default deny" in v.reason


def test_empty_input_is_denied():
    assert evaluate(url="", content="").admitted is False


def test_unreachable_site_cannot_be_admitted():
    """v2.10 gave an unreachable page +10. No content => no evidence => deny."""
    v = evaluate(url="https://somevendor.com", content="")
    assert v.admitted is False


def test_single_signal_family_is_insufficient():
    """A .ir domain alone is NOT enough — cross-referencing is mandatory."""
    v = evaluate(url="https://vendor.ir", content="Chemicals.")
    assert v.admitted is False
    assert "insufficient corroboration" in v.reason
    assert len(v.families) < ADMIT_FAMILIES


def test_two_independent_families_admit():
    v = evaluate(url="https://fanchem.ir",
                 content="تولید کننده افزودنی پلیمری تهران ایران 021-66565700")
    assert v.admitted is True
    assert v.country == IRAN
    assert len(v.families) >= ADMIT_FAMILIES


def test_domain_and_hosting_alone_do_not_corroborate():
    """Same underlying fact (Iranian hosting) must not self-corroborate."""
    ev = collect_evidence(url="https://vendor.ir", content="", ip="217.218.1.1")
    fams = {e.family for e in ev}
    v = evaluate(url="https://vendor.ir", content="", ip="217.218.1.1")
    assert fams == {"domain", "hosting"}
    # domain(40) + hosting(10) = 50 < 60 threshold
    assert v.admitted is False


# ---------------------------------------------------------------------------
# Foreign suppliers are rejected — the core requirement
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("url", [
    "https://www.merckmillipore.com",
    "https://www.sigmaaldrich.com",
    "https://www.thermofisher.com",
    "https://www.tcichemicals.com",
    "https://www.chemicalbook.com",
    "https://www.basf.com",
])
def test_multinational_domains_always_rejected(url):
    """Even with heavy Iranian content, a multinational's own site is foreign."""
    v = evaluate(url=url,
                 content="دفتر تهران ایران +98 21 88776655 کد پستی 1234567890 ریال")
    assert v.admitted is False
    assert v.disqualifiers
    assert v.disqualifiers[0].signal == "multinational_domain"


def test_foreign_cctld_rejected_despite_iranian_content():
    v = evaluate(url="https://chemvendor.de",
                 content="Tehran office تهران ایران +98 21 12345678 ریال")
    assert v.admitted is False
    assert v.disqualifiers[0].signal == "foreign_cctld"
    assert v.disqualifiers[0].country == "DE"


def test_foreign_hq_statement_rejected():
    v = evaluate(url="https://acme.com",
                 content=("Headquartered in Shanghai, China. We serve Iran. "
                          "تهران +98 21 55554444 ریال"))
    assert v.admitted is False
    assert v.disqualifiers[0].signal == "foreign_hq_statement"


def test_disqualifier_overrides_strong_positive_evidence():
    """Positive evidence can never outvote a disqualifier."""
    strong = ("نماد اعتماد الکترونیکی enamad.ir شناسه ملی 10100443156 "
              "کد پستی 1234567890 تهران ایران +98 21 88776655 ریال")
    v = evaluate(url="https://www.merckgroup.com", content=strong)
    assert v.admitted is False


# ---------------------------------------------------------------------------
# Brand vs supplier — protects legitimate Iranian importers
# ---------------------------------------------------------------------------


def test_iranian_importer_selling_foreign_brands_is_admitted():
    """The critical false-positive guard.

    Iranian lab suppliers are overwhelmingly importers of Merck/Sigma/TCI
    product. Foreign brand names and "Made in Germany" must NOT make the
    SUPPLIER foreign.
    """
    v = evaluate(
        url="https://minatajhiz.co.ir",
        content=("واردکننده مواد آزمایشگاهی از برندهای مرک آلمان و سیگما آلدریچ. "
                 "Made in Germany. ساخت آلمان. اصل آلمان. "
                 "تهران، ایران. تلفن: 021-66565700. قیمت: 500000 تومان"),
    )
    assert v.admitted is True
    assert v.country == IRAN


def test_made_in_germany_line_is_not_a_disqualifier():
    dq = collect_disqualifiers(
        url="https://vendor.ir",
        content="Product origin: Made in Germany, headquartered in Darmstadt")
    assert dq == []


def test_vendor_own_hq_statement_still_caught_when_brand_lines_present():
    """Stripping brand lines must not blind the gate to a real foreign HQ."""
    v = evaluate(url="https://vendor.com",
                 content=("Brand: Merck, made in Germany.\n"
                          "Our company is headquartered in Darmstadt, Germany.\n"
                          "تهران ایران +98 21 11112222"))
    assert v.admitted is False
    assert v.disqualifiers[0].signal == "foreign_hq_statement"


def test_iranian_exporter_quoting_usd_is_not_rejected():
    """Iranian exporters routinely quote USD/EUR — not a foreign signal."""
    v = evaluate(url="https://petrochem.ir",
                 content=("Export prices in USD $450/MT. FOB Bandar Abbas. "
                          "تهران ایران +98 21 88990011"))
    assert v.admitted is True


# ---------------------------------------------------------------------------
# Iranian identity signals (Enamad / registry IDs)
# ---------------------------------------------------------------------------


def test_enamad_is_high_confidence_signal():
    ev = collect_evidence(
        url="https://shop.ir",
        content='<img src="https://trustseal.enamad.ir/logo.aspx"> نماد اعتماد الکترونیکی')
    assert any(e.signal == "enamad" and e.confidence == "high" for e in ev)


def test_national_legal_entity_id_detected():
    ev = collect_evidence(url="", content="شناسه ملی: 10100443156")
    assert any(e.signal == "shenase_melli" for e in ev)


def test_postal_code_detected():
    ev = collect_evidence(url="", content="کد پستی: 1968953591")
    assert any(e.family == "registry" for e in ev)


@pytest.mark.parametrize("phone", [
    "+98 21 88776655", "0098 21 88776655", "09121161187", "021-66565700",
])
def test_iranian_phone_forms(phone):
    ev = collect_evidence(url="", content=f"تماس: {phone}")
    assert any(e.family == "phone" for e in ev), phone


def test_strongest_signal_per_family_wins():
    """Repeating weak evidence must not inflate the score."""
    ev = collect_evidence(url="", content="تهران تهران تهران اصفهان شیراز")
    assert score_evidence(ev) <= 40


def test_iranian_ip_ranges():
    assert is_iranian_ip("217.218.1.1") is True
    assert is_iranian_ip("185.143.233.238") is True
    assert is_iranian_ip("8.8.8.8") is False
    assert is_iranian_ip("not-an-ip") is False


@pytest.mark.parametrize("host,expected", [
    ("www.merckmillipore.com", "merckmillipore.com"),
    ("shop.minatajhiz.co.ir", "minatajhiz.co.ir"),
    ("fanchem.ir", "fanchem.ir"),
    ("https://www.temad.com/page", "temad.com"),
])
def test_registrable_domain(host, expected):
    assert registrable_domain(host) == expected


# ---------------------------------------------------------------------------
# Provenance / auditability
# ---------------------------------------------------------------------------


def test_verdict_carries_auditable_provenance():
    v = evaluate(url="https://fanchem.ir",
                 content="تهران ایران 021-66565700 ریال")
    d = v.as_dict()
    assert d["country"] == "IR"
    assert d["verified_at"]
    assert d["country_evidence"]
    for e in d["country_evidence"]:
        assert {"family", "signal", "value", "country", "confidence", "source"} <= set(e)


def test_assert_iranian_raises_on_foreign():
    with pytest.raises(ForeignSupplierRejected):
        assert_iranian(url="https://www.sigmaaldrich.com", content="Tehran ایران")


# ---------------------------------------------------------------------------
# Social path — every seeded channel must be audited Iranian
# ---------------------------------------------------------------------------


def test_every_seeded_channel_has_audited_iranian_provenance():
    for handle, meta in SOCIAL_CHANNELS.items():
        assert meta.get("country") == IRAN, handle
        assert meta.get("country_confidence") in {"high", "medium"}, handle
        assert meta.get("country_verified_on"), handle
        assert meta.get("country_signals"), handle
        assert meta.get("country_evidence"), handle


def test_active_channels_are_all_iranian():
    assert all(is_iranian_channel(h) for h in active_channels())
    assert all(channel_country(h) == IRAN for h in active_channels())


def test_known_foreign_channels_denied():
    for handle in FOREIGN_CHANNELS:
        assert is_foreign_channel(handle) is True
        assert is_iranian_channel(handle) is False


def test_unseeded_channel_denied_by_default():
    assert is_iranian_channel("some_random_unvetted_channel") is False


def test_merckmillipore_channel_is_the_iranian_importer_not_merck_kgaa():
    """Regression: the ``merckmillipore`` Telegram channel is a TEHRAN IMPORTER
    brand-squatting the Merck name (bio 'واردات مرك به صورت عمده', mobile
    09121161187) — not Merck KGaA. It stays; the merckmillipore.com WEBSITE is
    the foreign entity and is rejected. Removing the channel would delete a
    genuine Iranian supplier.
    """
    assert is_iranian_channel("merckmillipore") is True
    prov = country_provenance("merckmillipore")
    assert prov["country"] == IRAN
    assert "importer" in prov["country_evidence"].lower()
    # …while the multinational's own domain is rejected outright.
    assert evaluate(url="https://www.merckmillipore.com",
                    content="تهران ایران").admitted is False


def test_pipeline_excludes_foreign_channel_even_if_explicitly_requested(tmp_path):
    """A foreign handle passed directly to build_catalog must be dropped."""
    from src.parser.social_catalog_pipeline import build_catalog
    res = build_catalog(str(tmp_path), channels=["sigmaaldrich", "thermofisher"])
    assert res["metrics"]["vendors"] == 0
    assert res["metrics"]["excluded_foreign_suppliers"] == 2
    excluded = {e["channel"] for e in res["supplier_country_policy"]["excluded_foreign"]}
    assert excluded == {"sigmaaldrich", "thermofisher"}


def test_catalog_reports_country_policy(tmp_path):
    from src.parser.social_catalog_pipeline import build_catalog
    res = build_catalog(str(tmp_path), channels=[])
    pol = res["supplier_country_policy"]
    assert pol["policy"] == "iranian_suppliers_only"
    assert pol["allowed_countries"] == ["IR"]


# ---------------------------------------------------------------------------
# Web discovery path
# ---------------------------------------------------------------------------


def test_validator_scores_foreign_supplier_zero(monkeypatch):
    """Legacy score() must return 0 for foreign vendors so existing callers
    thresholding on min_verification_score inherit the Iran-only rule."""
    from src.discovery.validator import SupplierValidator
    v = SupplierValidator()
    monkeypatch.setattr(v, "_fetch_homepage",
                        lambda url: "Chemicals. Tehran ایران +98 21 88776655 reagent")
    assert v.score("https://www.sigmaaldrich.com") == 0.0
    assert v.is_iranian("https://www.sigmaaldrich.com") is False


def test_validator_admits_iranian_supplier(monkeypatch):
    from src.discovery.validator import SupplierValidator
    v = SupplierValidator()
    monkeypatch.setattr(
        v, "_fetch_homepage",
        lambda url: ("مواد شیمیایی آزمایشگاهی reagent chemical "
                     "تهران ایران تلفن 021-88776655 ریال"))
    score = v.score("https://kimiasupplier.ir")
    assert score >= 60
    assert v.is_iranian("https://kimiasupplier.ir") is True
