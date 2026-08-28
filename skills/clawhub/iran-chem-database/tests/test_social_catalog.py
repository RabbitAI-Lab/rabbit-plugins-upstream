"""Tests for the v2.10 social (Telegram) catalogue.

Includes explicit regression tests for the two precision bugs found by live
debugging against the real Telegram DOM:

  * the "۱۰۰ میلیون دلار" market-value price false positive (and the subtle
    ``gr``-inside-"group" substring leak);
  * educational news articles being parsed as product listings.

All tests are offline: pages are synthetic fixtures shaped like the real DOM.
"""
from __future__ import annotations

import os

import pytest

from src.crawler.telegram_engine import TelegramMirrorEngine
from src.discovery.social_seed_list import (REJECTED_CHANNELS, SOCIAL_CHANNELS,
                                            active_channels, channel_role,
                                            is_rejected, whatsapp_rfq_link)
from src.parser.social_catalog_pipeline import build_catalog
from src.parser.social_molecule_resolver import (ALIASES, classify_grade,
                                                 find_alias, lint_aliases,
                                                 resolve)
from src.parser.telegram_parser import (extract_price, has_sales_signal,
                                        harvest_forwarded_sources, parse_page)


def _page(channel: str, posts) -> str:
    """Build a page shaped like the real t.me/s/<chan> DOM."""
    out = []
    for pid, text, fwd in posts:
        fwd_html = (f'<a class="tgme_widget_message_forwarded_from_name" '
                    f'href="https://t.me/{fwd}">src</a>' if fwd else "")
        out.append(
            f'<div class="tgme_widget_message_wrap js-widget_message_wrap">'
            f'<div class="tgme_widget_message" data-post="{channel}/{pid}">'
            f'{fwd_html}'
            f'<div class="tgme_widget_message_text js-message_text">{text}</div>'
            f'<time datetime="2026-08-22T10:00:00+00:00"></time>'
            f'</div></div>')
    return "".join(out)


# ---------------------------------------------------------------- seed list
def test_seed_list_roles_are_known():
    valid = {"seller_research", "seller_industrial", "news", "lead_source"}
    for handle, meta in SOCIAL_CHANNELS.items():
        assert meta["role"] in valid, handle
        assert meta["description"]


def test_research_sellers_are_prioritised():
    order = active_channels()
    first_role = channel_role(order[0])
    assert first_role == "seller_research"


def test_rejected_channels_are_not_active():
    for handle in REJECTED_CHANNELS:
        assert handle not in SOCIAL_CHANNELS
        assert is_rejected(handle)


def test_whatsapp_rfq_link_normalises_iranian_number():
    link = whatsapp_rfq_link("09362048289")
    assert link == "https://wa.me/989362048289"
    assert "text=" in whatsapp_rfq_link("09362048289", "hello")


# ------------------------------------------------------- price extraction
def test_price_market_value_false_positive_rejected():
    """REGRESSION: a market statistic must never become a product price."""
    article = "بازار پوشش‌های صنعتی در سال گذشته به ۱۰۰ میلیون دلار رسید."
    assert extract_price(article) is None


def test_price_requires_unit_token_not_substring():
    """REGRESSION: 'gr' inside 'group' must not qualify as a pack unit."""
    text = "Our group announced 25000000 تومان investment"
    assert extract_price(text) is None


def test_real_unit_price_is_extracted():
    text = "اتانول ۹۶٪ قیمت ۴۵۰۰۰۰ تومان هر لیتر"
    price = extract_price(text)
    assert price is not None
    assert price["value"] == 450000
    assert price["currency"] == "IRT"


def test_quote_only_post_has_no_price():
    assert extract_price("متیل متاکریلات استعلام قیمت تماس بگیرید") is None


# ------------------------------------------- listing discriminator (roles)
def test_news_channel_article_is_not_a_listing():
    """REGRESSION: educational article on a news channel is not a listing."""
    article = ("همزمان با افزایش مصرف اتانول در بنزین، کارشناسان عرضه "
               "سوخت را بررسی کردند.")
    ok, reason = has_sales_signal(article, "news")
    assert ok is False
    assert reason == "news_channel_requires_strong_marker"


def test_news_channel_with_strong_marker_is_accepted():
    post = "فروش اتانول #اتانول قیمت ۵۰۰۰۰۰ تومان هر لیتر"
    ok, _ = has_sales_signal(post, "news")
    assert ok is True


def test_seller_channel_verb_is_sufficient():
    ok, reason = has_sales_signal("عرضه تولوئن صنعتی", "seller_industrial")
    assert ok is True
    assert reason in ("sales_verb_on_seller_channel", "strong_marker")


# --------------------------------------------------------------- resolver
def test_alias_dict_has_no_duplicate_keys():
    """REGRESSION: duplicate keys silently override richer alias sets."""
    assert lint_aliases() == []


def test_alias_resolution_offline():
    res = resolve("فروش استون خالص", offline=True)
    assert res["resolved"] is True
    assert res["canonical_name"] == "acetone"
    assert res["cas_number"] == "67-64-1"
    assert res["method"] == "alias"


def test_cas_anchored_fallback_for_unknown_name_variant():
    """A known CAS resolves the molecule even if the name variant is unseen."""
    res = resolve("Tetraethyl orthosilicate reagent", cas_hint="78-10-4",
                  offline=True)
    assert res["resolved"] is True
    assert res["canonical_name"] == "tetraethoxysilane"
    assert res["method"] == "cas_anchor"


def test_unknown_cas_is_kept_not_invented():
    res = resolve("Some novel compound", cas_hint="1234567-89-0", offline=True)
    assert res["method"] == "cas_only"
    assert res["canonical_name"] is None  # never invent an identity


def test_composite_is_not_force_fitted_to_a_cid():
    res = resolve("رزین اپوکسی دو جزئی چسب صنعتی", offline=True)
    assert res["kind"] == "composite"
    assert res["pubchem_cid"] is None
    assert res["inchi_key"] is None


def test_polymer_marked_as_polymer():
    res = resolve("پلی وینیل الکل گرید صنعتی", offline=True)
    assert res["kind"] == "polymer"


def test_find_alias_prefers_longest_match():
    assert find_alias("سولفات سدیم")[0] == "sodium sulfate"


def test_every_alias_value_is_wellformed():
    for key, (canon, cas) in ALIASES.items():
        assert canon and isinstance(canon, str), key
        if cas is not None:
            assert isinstance(cas, str) and cas.count("-") == 2, key


# ---------------------------------------------------------------- grading
def test_grade_from_research_text_marker():
    grade, reason = classify_grade("اتانول گرید HPLC مرک", "ethanol", "news")
    assert grade == "research"
    assert reason == "text_research_marker"


def test_grade_from_molecule_domain():
    grade, reason = classify_grade("موجود", "methyl methacrylate", None)
    assert grade == "industrial"
    assert reason == "molecule_domain"


def test_grade_unknown_when_no_signal():
    grade, reason = classify_grade("موجود", None, None)
    assert grade == "unknown"
    assert reason == "insufficient_signal"


# ------------------------------------------------------------ DOM parsing
def test_parse_page_extracts_posts_and_ids():
    html = _page("merckmillipore", [
        (10, "acetone 67-64-1 موجود", None),
        (11, "ethanol 64-17-5 #اتانول", "fanchem"),
    ])
    posts = parse_page(html)
    assert [p["post_id"] for p in posts] == [10, 11]
    assert posts[0]["channel"] == "merckmillipore"
    assert posts[1]["forwarded_from"] == "fanchem"
    assert "اتانول" in posts[1]["hashtags"]


def test_post_id_extraction_and_stub_detection():
    html = _page("x", [(5, "a", None), (7, "b", None)])
    assert TelegramMirrorEngine.page_post_ids(html) == [5, 7]
    assert TelegramMirrorEngine.page_post_ids("<html>Channel created</html>") == []


def test_forwarded_source_harvest():
    html = _page("c", [(1, "x", "Boof_company"), (2, "y", None),
                       (3, "z", "fanchem")])
    assert harvest_forwarded_sources(parse_page(html)) == ["Boof_company", "fanchem"]


# --------------------------------------------------------------- pipeline
def test_end_to_end_catalog_build(tmp_path):
    base = tmp_path / "mirrors"
    cdir = base / "social" / "telegram" / "merckmillipore"
    cdir.mkdir(parents=True)
    html = _page("merckmillipore", [
        (1, "فروش استون خالص قیمت ۵۰۰۰۰۰ تومان هر لیتر تماس 09121234567", None),
        (2, "tetraethoxysilane 78-10-4 for synthesis گرید آزمایشگاهی", None),
        (3, "مقاله آموزشی درباره تاریخچه شیمی", None),  # not a listing
    ])
    (cdir / "merckmillipore-00000001.html").write_text(html, encoding="utf-8")

    cat = build_catalog(str(base), ["merckmillipore"], offline=True)
    assert cat["metrics"]["listings"] == 2
    assert cat["metrics"]["molecules"] == 2
    names = sorted(m["canonical_name"] for m in cat["molecules"])
    assert names == ["acetone", "tetraethoxysilane"]
    # the educational post is rejected WITH a reason, never silently dropped
    assert cat["metrics"]["rejections"] >= 1
    assert all(r["rejection_reason"] for r in cat["rejections"])
    assert "Telegram" in cat["disclaimer"]


def test_catalog_handles_missing_mirror_gracefully(tmp_path):
    cat = build_catalog(str(tmp_path), ["merckmillipore"], offline=True)
    assert cat["metrics"]["channels_parsed"] == 0
    assert cat["metrics"]["listings"] == 0


def test_engine_state_roundtrip(tmp_path):
    eng = TelegramMirrorEngine(str(tmp_path))
    assert eng.read_state("nope") == {}
    eng._write_state("chan", {"newest_id": 42})
    assert eng.read_state("chan")["newest_id"] == 42
    assert eng.channel_dir("chan").endswith(os.path.join("social", "telegram", "chan"))


@pytest.mark.parametrize("concurrency,expected", [(1, 1), (6, 6), (99, 8), (0, 1)])
def test_concurrency_is_politeness_capped(tmp_path, concurrency, expected):
    eng = TelegramMirrorEngine(str(tmp_path), concurrency=concurrency)
    assert eng.concurrency == expected


# ------------------------------------------- v2.10 recall/robustness fixes
def test_generic_announcement_detected():
    """A post advertising a catalogue but naming no molecule is 'generic'."""
    from src.parser.social_molecule_resolver import is_generic_announcement
    assert is_generic_announcement("فروش مواد شیمیایی تخصصی آزمایشگاهی") is True
    assert is_generic_announcement("راهنمای خرید مواد شیمیایی آزمایشگاهی") is True


def test_named_molecule_is_not_generic():
    from src.parser.social_molecule_resolver import is_generic_announcement
    assert is_generic_announcement("فروش مواد شیمیایی: استون خالص") is False


def test_generic_and_dictionary_gap_are_separate_reasons(tmp_path):
    """Recall metrics stay honest: 'no molecule named' != 'dictionary gap'."""
    base = tmp_path / "m"
    cdir = base / "social" / "telegram" / "minatajhiz"
    cdir.mkdir(parents=True)
    html = _page("minatajhiz", [
        (1, "فروش مواد شیمیایی تخصصی آزمایشگاهی #شیمی", None),
        (2, "فروش نوعی ماده ناشناخته خاص #ماده تماس 09121234567", None),
    ])
    (cdir / "p-00000001.html").write_text(html, encoding="utf-8")
    cat = build_catalog(str(base), ["minatajhiz"], offline=True)
    reasons = {r["rejection_reason"] for r in cat["rejections"]}
    assert "generic_announcement_no_molecule_named" in reasons


def test_cas_only_listing_gets_display_name(tmp_path):
    """REGRESSION: a nameless CAS-only hit must not surface as None."""
    base = tmp_path / "m"
    cdir = base / "social" / "telegram" / "minatajhiz"
    cdir.mkdir(parents=True)
    html = _page("minatajhiz", [
        (1, "reagent 1234567-89-0 موجود تماس 09121234567", None)])
    (cdir / "p-00000001.html").write_text(html, encoding="utf-8")
    cat = build_catalog(str(base), ["minatajhiz"], offline=True)
    assert cat["metrics"]["listings"] == 1
    row = cat["listings"][0]
    assert row["canonical_name"] is None       # honest: identity unknown
    assert row["display_name"] == "CAS 1234567-89-0"
    # molecules list must be sortable (this crashed before the fix)
    assert sorted(m["canonical_name"] for m in cat["molecules"])


# --------------------------------------------------- lead ranking (v2.10)
def test_lead_ranking_filters_noise():
    """Forwarded-from harvesting is noisy: bots/news must not be proposed."""
    from src.discovery.social_seed_list import rank_leads, score_lead
    assert score_lead("chemgroupbot") < 0
    assert score_lead("bbcpersian") < 0
    assert score_lead("ChemIranSanat") > 0
    handles = ["ChemIranSanat", "chemgroupbot", "bbcpersian", "dw_farsi",
               "polyzone", "Audiobook_p"]
    kept = [r["handle"] for r in rank_leads(handles)]
    assert "ChemIranSanat" in kept
    for noise in ("chemgroupbot", "bbcpersian", "dw_farsi", "Audiobook_p"):
        assert noise not in kept


def test_newly_verified_channel_is_seeded():
    """ChemIranSanat was discovered via forwarded-from and content-verified."""
    assert SOCIAL_CHANNELS["ChemIranSanat"]["role"] == "seller_research"
    assert not is_rejected("ChemIranSanat")


def test_content_checked_rejects_recorded_with_reason():
    from src.discovery.social_seed_list import rejection_reason
    for handle in ("polyzone", "labsnet", "WKPlast", "chemical_leaders"):
        assert is_rejected(handle)
        assert rejection_reason(handle)


def test_incremental_run_reports_status_not_zero_coverage():
    """REGRESSION: an up-to-date channel must not report coverage 0%."""
    import src.crawler.telegram_engine as te

    eng = te.TelegramMirrorEngine("/tmp/_t_inc")
    eng._write_state("c", {"newest_id": 100})
    page = _page("c", [(99, "x", None), (100, "y", None)])
    eng.fetch_page = lambda ch, before=None: page  # type: ignore[assignment]
    stats = eng.mirror_channel("c")
    assert stats["status"] == "incremental_up_to_date"
    assert stats["coverage_pct"] is None


# ------------------------------------------- job-advert filter (v2.10)
def test_job_advert_is_not_a_product_listing():
    """REGRESSION: lab marketplaces are dominated by recruitment posts that
    carry salary figures, phones and hashtags — every 'strong marker'."""
    from src.parser.telegram_parser import is_job_advert
    ad = ("#استخدام_آزمایشگاه #تهران کارشناس علوم آزمایشگاهی "
          "#شیفت_صبح حقوق توافقی + بیمه تماس 09121234567")
    assert is_job_advert(ad) is True
    ok, reason = has_sales_signal(ad, "lead_source")
    assert ok is False
    assert reason == "job_advert_not_a_product_listing"


def test_product_post_is_not_flagged_as_job_advert():
    from src.parser.telegram_parser import is_job_advert
    assert is_job_advert("فروش استون خالص قیمت ۵۰۰۰۰۰ تومان هر لیتر") is False


def test_job_advert_filtered_on_every_role():
    ad = "استخدام کارشناس آزمایشگاه با حقوق و بیمه شیفت صبح"
    for role in ("seller_research", "seller_industrial", "news", "lead_source"):
        ok, _ = has_sales_signal(ad, role)
        assert ok is False, role


def test_mined_metal_stearates_resolve():
    """Aliases mined from live seller posts, CAS PubChem-verified."""
    for text, canon, cas in [
        ("فروش استئارات روی گرید صنعتی", "zinc stearate", "557-05-1"),
        ("calcium stearate bulk", "calcium stearate", "1592-23-0"),
        ("استئارات منیزیم", "magnesium stearate", "557-04-0"),
        ("کولین کلراید", "choline chloride", "67-48-1"),
    ]:
        r = resolve(text, offline=True)
        assert r["canonical_name"] == canon, text
        assert r["cas_number"] == cas
