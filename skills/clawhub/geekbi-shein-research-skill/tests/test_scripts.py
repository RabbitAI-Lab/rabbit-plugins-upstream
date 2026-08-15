import base64
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import shein_category_search
import shein_goods_search
import shein_image_search
import shein_keyword_search
import shein_review_search
import shein_shop_search
import shein_site_list
from shein_search_common import build_url, validate_search_response


class SearchParameterTests(unittest.TestCase):
    def test_goods_accepts_repeated_categories_and_full_filters(self):
        params = shein_goods_search.parse_params(
            [
                "siteId=1",
                "catIds=10",
                "catIds=20",
                "hostingMode=2",
                "similarNumMin=1",
                "similarNumMax=10",
                "onSaleTimeMin=2026-05-13T00:00:00+08:00",
                "onSaleTimeMax=2026-08-13T00:00:00+08:00",
                "sort=daySold",
                "order=desc",
            ]
        )
        self.assertEqual(params.count(("catIds", "10")), 1)
        self.assertEqual(params.count(("catIds", "20")), 1)

    def test_goods_rejects_removed_and_unknown_parameters(self):
        for value in ("status=1", "similarNum=10", "siteUID=us"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                shein_goods_search.parse_params([value])

    def test_all_searches_reject_noncanonical_order(self):
        parsers = (
            shein_goods_search.parse_params,
            shein_shop_search.parse_params,
            shein_category_search.parse_params,
            shein_keyword_search.parse_params,
        )
        for parser in parsers:
            with self.subTest(parser=parser.__module__), self.assertRaises(ValueError):
                parser(["order=descend"])

    def test_ranges_and_page_are_validated(self):
        with self.assertRaises(ValueError):
            shein_goods_search.parse_params(["soldMin=100", "soldMax=99"])
        with self.assertRaises(ValueError):
            shein_goods_search.parse_params(["soldMin=1.5"])
        with self.assertRaises(ValueError):
            shein_goods_search.parse_params(["salesMin=NaN"])
        with self.assertRaises(ValueError):
            shein_shop_search.parse_params(["size=201"])
        with self.assertRaises(ValueError):
            shein_keyword_search.parse_params(
                ["firstOnSaleTimeMin=2026-08-13T00:00:00", "firstOnSaleTimeMax=2026-08-12T00:00:00"]
            )
        with self.assertRaises(ValueError):
            shein_keyword_search.parse_params(["firstOnSaleTimeMin=2026-08-13T00:00:00"])

    def test_all_searches_match_nonnegative_and_result_window_contracts(self):
        invalid_ranges = (
            (shein_goods_search.parse_params, "soldMin=-1"),
            (shein_shop_search.parse_params, "dayFollowerMin=-1"),
            (shein_category_search.parse_params, "dayItemCountMin=-1"),
            (shein_keyword_search.parse_params, "totalSalesMin=-1"),
        )
        for parser, value in invalid_ranges:
            with self.subTest(parser=parser.__module__, value=value), self.assertRaises(ValueError):
                parser([value])

        parsers = (
            shein_goods_search.parse_params,
            shein_shop_search.parse_params,
            shein_category_search.parse_params,
            shein_keyword_search.parse_params,
        )
        for parser in parsers:
            with self.subTest(parser=parser.__module__), self.assertRaises(ValueError):
                parser(["page=51", "size=200"])

        self.assertIn(
            ("dayItemCountRateMin", "-0.5"),
            shein_category_search.parse_params(["dayItemCountRateMin=-0.5"]),
        )

    def test_review_requires_goods_and_limits_result_window(self):
        with self.assertRaises(ValueError):
            shein_review_search.parse_params(["siteId=1"])
        with self.assertRaises(ValueError):
            shein_review_search.parse_params(["goodsId=1", "page=51", "size=200"])
        with self.assertRaises(ValueError):
            shein_review_search.parse_params(["goodsId=1", "specs=" + "x" * 301])
        self.assertIn(
            ("goodsId", "1"),
            shein_review_search.parse_params(["goodsId=1", "scoreMin=1", "scoreMax=2"]),
        )


class TransportContractTests(unittest.TestCase):
    def test_url_preserves_repeated_values(self):
        url = build_url("https://example.test/", "/search", [("catIds", "1"), ("catIds", "2")])
        self.assertEqual(url, "https://example.test/search?catIds=1&catIds=2")

    def test_search_response_contract(self):
        payload = {"code": 0, "data": {"total": 1, "list": [{}], "site": {"id": 1}}}
        self.assertEqual(validate_search_response(payload, "失败"), payload)
        with self.assertRaises(ValueError):
            validate_search_response({"code": 0, "data": {"total": "1", "list": []}}, "失败")
        with self.assertRaises(ValueError):
            validate_search_response({"code": 0, "data": {"total": 1, "list": []}}, "失败")

    def test_image_data_uri_and_multipart(self):
        png = b"\x89PNG\r\n\x1a\n" + b"payload"
        source = "data:image/png;base64," + base64.b64encode(png).decode("ascii")
        data, content_type, filename = shein_image_search.read_image_source(source, 1)
        self.assertEqual(data, png)
        self.assertEqual(content_type, "image/png")
        body, multipart_type = shein_image_search.build_multipart(data, content_type, filename)
        self.assertIn(b'name="file"', body)
        self.assertIn(b"Content-Type: image/png", body)
        self.assertTrue(multipart_type.startswith("multipart/form-data; boundary="))

    def test_image_rejects_svg(self):
        source = "data:image/svg+xml;base64," + base64.b64encode(b"<svg/>").decode("ascii")
        with self.assertRaises(ValueError):
            shein_image_search.read_image_source(source, 1)

    def test_site_resolution_keeps_all_and_us_distinct(self):
        sites = [
            {"id": 1, "siteUID": "us", "siteHost": "us.shein.com", "cnName": "全部"},
            {"id": 2, "siteUID": "us", "siteHost": "us.shein.com", "cnName": "美国"},
        ]
        self.assertEqual(shein_site_list.resolve_site(sites, "全部")[0]["siteId"], 1)
        self.assertEqual(shein_site_list.resolve_site(sites, "美国")[0]["siteId"], 2)
        self.assertEqual(len(shein_site_list.resolve_site(sites, "us")), 2)


if __name__ == "__main__":
    unittest.main()
