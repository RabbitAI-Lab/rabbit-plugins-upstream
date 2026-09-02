"""Tests for pre-built HTTrack profile templates (spec §3.2)."""
from src.crawler.httrack_profiles import HTTrackProfiles


def test_standard_profile():
    cfg = HTTrackProfiles.standard_catalog_site(1, "acme", "https://acme.ir")
    assert cfg.depth == 5
    assert cfg.sockets == 4
    assert cfg.connections_per_second == 2.0


def test_pdf_profile_prefers_pdfs():
    cfg = HTTrackProfiles.pdf_catalog_site(1, "acme", "https://acme.ir")
    assert "+*.pdf" in cfg.include_filters
    assert cfg.depth == 3


def test_large_db_profile_gentler():
    cfg = HTTrackProfiles.large_database_site(1, "acme", "https://acme.ir")
    assert cfg.depth == 8
    assert cfg.sockets == 2
    assert cfg.connections_per_second == 1.0


def test_sensitive_profile_ultra_polite():
    cfg = HTTrackProfiles.sensitive_site(1, "acme", "https://acme.ir")
    assert cfg.connections_per_second == 0.5
    assert cfg.sockets == 1
    assert "-G" in cfg.extra_flags


def test_ir_domain_profile_utf8():
    cfg = HTTrackProfiles.ir_domain_site(1, "acme", "https://acme.ir")
    assert "--charset=UTF-8" in cfg.extra_flags


def test_auto_select_ir_domain():
    cfg = HTTrackProfiles.for_supplier("distributor", 1, "acme", "https://acme.ir")
    assert "--charset=UTF-8" in cfg.extra_flags
