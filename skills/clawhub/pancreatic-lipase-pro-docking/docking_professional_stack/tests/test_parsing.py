"""Tests for vina log parsing and the PubChem name resolver helpers."""
import docking_10x_pipeline as base
import resolve_names as rn


def test_parse_vina_score(tmp_path):
    log = tmp_path / "vina.log"
    log.write_text(
        "mode |   affinity | dist from best mode\n"
        "-----+------------+----------+----------\n"
        "   1       -7.291          0          0\n"
        "   2       -6.712      1.634      4.137\n"
    )
    assert base.parse_vina_score(log) == -7.291


def test_parse_vina_score_empty_log(tmp_path):
    log = tmp_path / "empty.log"
    log.write_text("")
    assert base.parse_vina_score(log) is None


def test_parse_vina_score_no_mode1(tmp_path):
    log = tmp_path / "weird.log"
    log.write_text("nothing here\n")
    assert base.parse_vina_score(log) is None


def test_asciify_unicode_names():
    assert rn.asciify("17β-Estradiol") == "17beta-Estradiol"
    assert rn.asciify("2,2′-Dipyridylamine") == "2,2'-Dipyridylamine"
    assert rn.asciify("5β-Cholan-24-oic acid") == "5beta-Cholan-24-oic acid"
    assert rn.asciify("α-Humulene") == "alpha-Humulene"
    assert rn.asciify("plain") == "plain"


def test_asciify_does_not_break_plain():
    assert rn.asciify("1,2,4-Triazole") == "1,2,4-Triazole"
