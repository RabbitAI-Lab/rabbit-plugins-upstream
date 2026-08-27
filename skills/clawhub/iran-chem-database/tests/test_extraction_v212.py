"""v2.12 — hardened Telegram extraction, Persian gate, easy retrieval.

Three guarantees are locked down here:

1. **Structured extraction** — the catalogue-line shape that Iranian importers
   actually post ("006123 Exir Melamine, 99% 500g") is parsed into fields and
   resolved, instead of being discarded as ``no_alias_or_cas_match``.
2. **Persian gate** — every channel must publish Persian/Farsi; Arabic-script
   and English-only channels are refused.
3. **Retrieval** — listings carry the commercial fields a buyer needs and can
   be written straight to CSV/JSON.
"""
from __future__ import annotations

import json

import pytest

from src.parser.listing_extractor import (BRANDS, ExtractedListing,
                                          extract_availability, extract_brand,
                                          extract_cas_numbers,
                                          extract_listing_fields,
                                          extract_pack_size,
                                          extract_product_names,
                                          extract_purity, extract_sku,
                                          is_structured_catalogue_post)
from src.parser.persian_gate import (MIN_CHANNEL_PERSIAN_RATIO,
                                     channel_persian_profile, fa_digits_to_en,
                                     is_persian_post, normalize_persian,
                                     post_language)
from src.parser.telegram_parser import has_sales_signal

# Real post shapes observed on the live channels.
POST_CATALOGUE = ("006123 Exir Melamine, 99% 500g\n"
                  "🔜 موجود و آماده تحویل\n"
                  "✅ شیمیران صنعت فقط اصلی\n"
                  "📱 سفارش کالا 👇 🆔 @ChemIranAdmin")
POST_PERSIAN_TRADE = ("سدیم هیدروکسید مرک آلمان گرید GR خلوص ۹۸ درصد "
                      "بسته ۵ کیلوگرم قیمت ۲,۵۰۰,۰۰۰ تومان موجود")
POST_EDUCATIONAL = ("گیاه یا حیوان! موجوداتی که همانند گیاهان از طریق "
                    "فتوسنتز به حیات خود ادامه میدهند.")
POST_JOB = "استخدام کارشناس آزمایشگاه خانم با سابقه کار تماس 09121234567"


# ---------------------------------------------------------------------------
# Structured field extraction
# ---------------------------------------------------------------------------


def test_catalogue_line_yields_every_field():
    e = extract_listing_fields(POST_CATALOGUE)
    assert e.sku == "006123"
    assert e.brand == "Exir"
    assert e.product_name == "Melamine"
    assert e.purity == 99.0
    assert e.pack_size["normalised_value"] == 500.0
    assert e.pack_size["normalised_unit"] == "g"
    assert e.availability == "in_stock"
    assert e.field_count >= 5


def test_persian_trade_post_fields():
    e = extract_listing_fields(POST_PERSIAN_TRADE)
    assert e.brand == "Merck"          # «مرک»
    assert e.purity == 98.0            # Persian digits «۹۸ درصد»
    assert e.grade_token.upper() == "GR"
    assert e.pack_size["normalised_value"] == 5000.0   # ۵ کیلوگرم -> g
    assert e.availability == "in_stock"


@pytest.mark.parametrize("text,expected", [
    ("1,4-Butanediol 99% 1L", "1,4-Butanediol"),
    ("N,N-Dimethylformamide 99.8% 2.5L", "N,N-Dimethylformamide"),
    ("013484 Exir 2-Propanol, USP >99.5% 2.5L", "2-Propanol"),
    ("Sodium hydroxide 98% 5kg", "Sodium hydroxide"),
])
def test_locants_and_purity_are_not_swallowed(text, expected):
    """Locants are chemically significant; trailing purity digits are not."""
    assert extract_product_names(text)[0] == expected


def test_marketing_noise_is_not_a_product_name():
    for junk in ("Telegram", "phone", "polyzone", "free delivery", "www"):
        assert extract_product_names(junk) == [], junk


def test_cas_checksum_rejects_lookalikes():
    assert extract_cas_numbers("CAS 2210-25-5") == ["2210-25-5"]
    assert extract_cas_numbers("methanol 67-56-1") == ["67-56-1"]
    # Valid shape, wrong check digit -> rejected.
    assert extract_cas_numbers("CAS 7647-14-9") == []
    # A date/phone must never be read as a CAS.
    assert extract_cas_numbers("تاریخ 1403-05-2") == []


@pytest.mark.parametrize("text,value,unit", [
    ("500g", 500.0, "g"), ("2.5L", 2500.0, "ml"), ("25 kg", 25000.0, "g"),
    ("100ml", 100.0, "ml"), ("۵ کیلوگرم", 5000.0, "g"), ("250 گرم", 250.0, "g"),
])
def test_pack_size_normalisation(text, value, unit):
    p = extract_pack_size(text)
    assert p and p["normalised_value"] == value and p["normalised_unit"] == unit


def test_sku_is_not_a_phone_or_year_or_cas():
    assert extract_sku("تماس 09121161187") is None
    assert extract_sku("سال 1404 محصول جدید") is None
    assert extract_sku("CAS 110-63-4") is None
    assert extract_sku("006123 Melamine") == "006123"


def test_purity_ignores_discounts_and_concentrations():
    assert extract_purity("تخفیف 20% ویژه") is None
    assert extract_purity("خلوص 99.5%") == 99.5


@pytest.mark.parametrize("text,state", [
    ("موجود و آماده تحویل", "in_stock"),
    ("ناموجود", "unavailable"),      # must beat the "موجود" substring
    ("قابل سفارش", "to_order"),
])
def test_availability(text, state):
    assert extract_availability(text) == state


def test_brand_detection_persian_and_latin():
    assert extract_brand("مواد مرک اصل") == "Merck"
    assert extract_brand("Sigma-Aldrich reagent") == "Sigma-Aldrich"
    assert extract_brand("محصول اکسیر") == "Exir"
    assert extract_brand("no brand here") is None


def test_brand_is_product_metadata_not_supplier_country():
    """A foreign brand must never be read as a foreign supplier (v2.11 rule)."""
    assert "merck" in BRANDS and BRANDS["merck"] == "Merck"
    e = extract_listing_fields(POST_PERSIAN_TRADE)
    assert e.brand == "Merck"
    assert not hasattr(e, "country")


# ---------------------------------------------------------------------------
# Listing discriminator
# ---------------------------------------------------------------------------


def test_structured_post_is_admitted_without_sales_verb():
    assert is_structured_catalogue_post(POST_CATALOGUE) is True
    ok, reason = has_sales_signal(POST_CATALOGUE, "seller_research")
    assert ok and reason == "structured_catalogue_line"


def test_educational_and_job_posts_still_rejected():
    assert is_structured_catalogue_post(POST_EDUCATIONAL) is False
    ok, _ = has_sales_signal(POST_EDUCATIONAL, "news")
    assert ok is False
    ok, reason = has_sales_signal(POST_JOB, "seller_research")
    assert ok is False and reason == "job_advert_not_a_product_listing"


def test_empty_and_garbage_never_crash():
    for junk in ("", None, "🙂🙂🙂", "..."):
        e = extract_listing_fields(junk)
        assert isinstance(e, ExtractedListing)
        assert e.field_count >= 0


# ---------------------------------------------------------------------------
# Persian / Farsi gate
# ---------------------------------------------------------------------------


def test_persian_post_detected():
    assert post_language(POST_PERSIAN_TRADE) == "fa"
    assert is_persian_post(POST_PERSIAN_TRADE) is True


def test_arabic_is_not_accepted_as_persian():
    """Persian and Arabic share a script — they must not be conflated."""
    ar = "مرحبا بكم في قناة المواد الكيميائية يرجى الاتصال بنا"
    assert post_language(ar) == "ar"
    assert is_persian_post(ar) is False


def test_english_post_detected():
    assert post_language("Sodium hydroxide 99% in stock") == "en"


def test_mixed_persian_latin_catalogue_line_counts_as_persian():
    assert post_language(POST_CATALOGUE) in ("fa", "mixed")
    assert is_persian_post(POST_CATALOGUE) is True


def test_channel_gate_accepts_persian_channel():
    prof = channel_persian_profile("x", [POST_PERSIAN_TRADE] * 10)
    assert prof.is_persian is True
    assert prof.persian_ratio >= MIN_CHANNEL_PERSIAN_RATIO
    assert prof.trade_words_seen


def test_channel_gate_rejects_english_only_channel():
    prof = channel_persian_profile("x", ["Sodium hydroxide 99% 5kg"] * 10)
    assert prof.is_persian is False
    assert "ratio" in prof.reason


def test_channel_gate_rejects_arabic_channel():
    prof = channel_persian_profile(
        "x", ["مرحبا بكم في قناة المواد الكيميائية يرجى الاتصال"] * 10)
    assert prof.is_persian is False
    assert "Arabic" in prof.reason


def test_tiny_persian_sample_is_accepted_but_flagged():
    """A small channel that is unambiguously Persian is still Persian.

    Refusing on sample size alone would drop genuine low-volume Iranian
    vendors, so the verdict stands and the reason records the weak evidence.
    """
    prof = channel_persian_profile("x", [POST_PERSIAN_TRADE])
    assert prof.is_persian is True
    assert "small sample" in prof.reason


def test_tiny_arabic_sample_is_rejected():
    prof = channel_persian_profile("x", ["مرحبا بكم في قناة المواد الكيميائية"])
    assert prof.is_persian is False


def test_no_text_posts_is_rejected():
    prof = channel_persian_profile("x", ["", "   "])
    assert prof.is_persian is False
    assert "no text posts" in prof.reason


def test_persian_channel_keeps_latin_catalogue_posts():
    """Enforcement is per CHANNEL: Latin catalogue lines must not be dropped."""
    texts = [POST_PERSIAN_TRADE] * 8 + ["Melamine 99% 500g"] * 2
    assert channel_persian_profile("x", texts).is_persian is True


def test_normalisation_unifies_arabic_persian_variants():
    assert normalize_persian("كيميا") == normalize_persian("کیمیا")
    assert fa_digits_to_en("۱۲۳۴۵") == "12345"
    assert fa_digits_to_en("٤٥٦") == "456"


# ---------------------------------------------------------------------------
# Seed list: country + Persian must BOTH be recorded
# ---------------------------------------------------------------------------


def test_every_seeded_channel_declares_persian():
    from src.discovery.social_seed_list import SOCIAL_CHANNELS
    for handle, meta in SOCIAL_CHANNELS.items():
        assert meta.get("language") == "fa", handle
        assert meta.get("persian_verified_on"), handle


# ---------------------------------------------------------------------------
# Retrieval
# ---------------------------------------------------------------------------


def test_write_listings_csv_and_json(tmp_path):
    from src.scripts.social_crawl import write_listings
    rows = [{
        "channel": "ChemIranSanat", "display_name": "melamine",
        "canonical_name": "melamine", "cas_number": "108-78-1",
        "pubchem_cid": 7955, "molecular_formula": "C3H6N6", "brand": "Exir",
        "sku": "006123", "purity_percent": 99.0, "grade_token": None,
        "pack_size": {"raw": "500g", "normalised_value": 500.0,
                      "normalised_unit": "g"},
        "price": {"value": 2500000.0, "currency": "IRT"},
        "availability": "in_stock", "grade": "research",
        "identity_method": "structured_pubchem", "post_language": "mixed",
        "date": "2026-08-01", "url": "https://t.me/ChemIranSanat/1",
    }]
    csv_path = tmp_path / "out.csv"
    assert write_listings(rows, str(csv_path)) == 1
    body = csv_path.read_text(encoding="utf-8-sig")
    assert "melamine" in body and "006123" in body and "500" in body

    json_path = tmp_path / "out.json"
    assert write_listings(rows, str(json_path)) == 1
    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data["count"] == 1
    assert data["listings"][0]["pack_unit"] == "g"


def test_catalog_exposes_persian_policy(tmp_path):
    from src.parser.social_catalog_pipeline import build_catalog
    res = build_catalog(str(tmp_path), channels=[])
    assert res["persian_language_policy"]["policy"] == "iranian_persian_channels_only"
    assert res["supplier_country_policy"]["allowed_countries"] == ["IR"]
