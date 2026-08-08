"""Core algorithm tests for metadata-standards-checker."""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestLocalName:
    def test_strips_namespace(self):
        assert M.localname("{http://x}fileIdentifier") == "fileIdentifier"

    def test_no_namespace(self):
        assert M.localname("idinfo") == "idinfo"


class TestParse:
    def test_parse_iso_string(self):
        xml = M.build_iso_xml([116, 39, 117, 40], complete=True)
        root, fields = M.parse_metadata_xml(xml)
        assert "fileIdentifier" in fields["__present__"]
        # language 的文本存于子元素 CharacterString 中
        assert "eng" in fields.get("CharacterString", [])

    def test_parse_malformed_raises(self):
        with pytest.raises(M.ValidationError):
            M.parse_metadata_xml("<a><b></a>")


class TestDetectStandard:
    def test_detect_iso(self):
        _, fields = M.parse_metadata_xml(M.build_iso_xml([0, 0, 1, 1], True))
        assert M.detect_standard(fields) == "iso19115"

    def test_detect_fgdc(self):
        _, fields = M.parse_metadata_xml(M.build_fgdc_xml([0, 0, 1, 1], True))
        assert M.detect_standard(fields) == "fgdc"


class TestCompleteness:
    def test_full_score(self):
        fields = {"__present__": ["a", "b", "c"]}
        assert M.completeness_score(fields, ["a", "b", "c"]) == 1.0

    def test_partial_score(self):
        fields = {"__present__": ["a"]}
        assert M.completeness_score(fields, ["a", "b", "c", "d"]) == pytest.approx(0.25)

    def test_empty_required(self):
        assert M.completeness_score({"__present__": []}, []) == 1.0


class TestValidate:
    def test_iso_complete_passes(self):
        _, fields = M.parse_metadata_xml(M.build_iso_xml([116, 39, 117, 40], True))
        res = M.validate_metadata(fields, "iso19115")
        assert res["passed"] is True
        assert res["completeness_score"] == 1.0
        assert res["errors"] == 0

    def test_iso_incomplete_detects_missing(self):
        _, fields = M.parse_metadata_xml(M.build_iso_xml([116, 39, 117, 40], False))
        res = M.validate_metadata(fields, "iso19115")
        assert res["passed"] is False
        assert res["errors"] == 2
        assert res["completeness_score"] < 1.0
        missing = {i["field"] for i in res["issues"] if i["level"] == "error"}
        assert missing == {"fileIdentifier", "abstract"}

    def test_fgdc_complete_passes(self):
        _, fields = M.parse_metadata_xml(M.build_fgdc_xml([116, 39, 117, 40], True))
        res = M.validate_metadata(fields, "fgdc")
        assert res["passed"] is True
        assert res["completeness_score"] == 1.0

    def test_fgdc_incomplete_detects_missing(self):
        # 手工构造一个缺少 metainfo / metstdn 的 FGDC 片段
        xml = "<metadata><idinfo><citation/><descript/></idinfo></metadata>"
        _, fields = M.parse_metadata_xml(xml)
        res = M.validate_metadata(fields, "fgdc")
        assert res["passed"] is False
        missing = {i["field"] for i in res["issues"] if i["level"] == "error"}
        assert "metainfo" in missing and "metstdn" in missing

    def test_unknown_standard_raises(self):
        _, fields = M.parse_metadata_xml(M.build_iso_xml([0, 0, 1, 1], True))
        with pytest.raises(M.UsageError):
            M.validate_metadata(fields, "dublin-core")

    def test_controlled_vocab_warning(self):
        xml = ("<MD_Metadata><hierarchyLevel>banana</hierarchyLevel>"
               "<fileIdentifier/><language/><characterSet/><contact/>"
               "<dateStamp/><metadataStandardName/><referenceSystemInfo/>"
               "<identificationInfo><title/><abstract/></identificationInfo>"
               "</MD_Metadata>")
        _, fields = M.parse_metadata_xml(xml)
        res = M.validate_metadata(fields, "iso19115")
        vocab_warns = [i for i in res["issues"]
                       if i["field"] == "hierarchyLevel" and "vocabulary" in i["message"]]
        assert len(vocab_warns) == 1


class TestSynthetic:
    def test_generate_writes_files(self, tmp_path):
        out = str(tmp_path)
        samples = M.generate_synthetic(out, [116, 39, 117, 40])
        assert len(samples) == 3
        for s in samples:
            assert os.path.exists(s["path"])
        # 三个样例都能被解析
        for s in samples:
            root, fields = M.parse_metadata_xml(s["path"])
            res = M.validate_metadata(fields, s["standard"])
            assert "completeness_score" in res

    def test_incomplete_sample_scores_lower(self, tmp_path):
        out = str(tmp_path)
        samples = M.generate_synthetic(out, [116, 39, 117, 40])
        by_name = {os.path.basename(s["path"]): s for s in samples}
        _, fc = M.parse_metadata_xml(by_name["iso_complete.xml"]["path"])
        _, fi = M.parse_metadata_xml(by_name["iso_incomplete.xml"]["path"])
        sc = M.validate_metadata(fc, "iso19115")["completeness_score"]
        si = M.validate_metadata(fi, "iso19115")["completeness_score"]
        assert si < sc
