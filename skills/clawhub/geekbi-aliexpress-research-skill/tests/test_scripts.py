import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import aliexpress_category_info
import aliexpress_category_list
import aliexpress_goods_info
import aliexpress_goods_search
import aliexpress_mall_info
import aliexpress_site_list
from aliexpress_search_common import (
    build_url,
    sanitize_goods_metrics,
    sanitize_site,
    validate_object_response,
    validate_search_response,
)


class SearchParameterTests(unittest.TestCase):
    def test_goods_accepts_supported_filters(self):
        params = aliexpress_goods_search.parse_params(
            [
                "siteId=1",
                "catId=172282",
                "monthSoldMin=100",
                "monthSoldMax=5000",
                "totalSoldMin=1000",
                "totalSalesMax=500000",
                "priceMin=12.5",
                "onSaleTimeMin=2026-05-01T00:00:00+08:00",
                "sort=monthSold",
                "order=desc",
                "page=1",
                "size=100",
            ]
        )
        self.assertIn(("catId", "172282"), params)

    def test_goods_rejects_unsupported_or_out_of_window_conditions(self):
        for value in (
            "shipsFrom=1", "commentMin=1", "order=descend", "isCross=true",
            "sort=mallReviewNum",
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                aliexpress_goods_search.parse_params([value])
        with self.assertRaises(ValueError):
            aliexpress_goods_search.parse_params(["page=2", "size=200"])
        with self.assertRaises(ValueError):
            aliexpress_goods_search.parse_params(["monthSoldMin=10", "monthSoldMax=9"])

    def test_identifier_commands_validate_required_values(self):
        with self.assertRaises(ValueError):
            aliexpress_goods_info.build_params(" ", 1)
        with self.assertRaises(ValueError):
            aliexpress_mall_info.build_params("", 1)
        with self.assertRaises(ValueError):
            aliexpress_category_info.build_params("", 1)
        self.assertEqual(aliexpress_category_list.build_params("0", 1)[0], ("parentCatId", "0"))


class TransportContractTests(unittest.TestCase):
    def test_url_encoding(self):
        url = build_url("https://example.test/", "/search", [("keyword", "wireless mouse")])
        self.assertEqual(url, "https://example.test/search?keyword=wireless+mouse")

    def test_response_contracts(self):
        search = {"code": 0, "data": {"total": 1, "list": [{}], "site": {"siteId": 1}}}
        self.assertEqual(validate_search_response(search), search)
        detail = {"code": 0, "data": {"goods": {}, "site": {"siteId": 1}, "history": []}}
        self.assertEqual(validate_object_response(detail, "goods", "失败"), detail)
        with self.assertRaises(ValueError):
            validate_search_response({"code": 0, "data": {"total": "1", "list": []}})

    def test_site_resolution_uses_region_or_country_name(self):
        sites = [
            {"siteId": 1, "regionId": "us", "name": "United States", "cnName": "美国"},
            {"siteId": 2, "regionId": "br", "name": "Brazil", "cnName": "巴西"},
        ]
        self.assertEqual(aliexpress_site_list.resolve_site(sites, "美国")[0]["siteId"], 1)
        self.assertEqual(aliexpress_site_list.resolve_site(sites, "United States")[0]["siteId"], 1)
        self.assertEqual(aliexpress_site_list.resolve_site(sites, "br")[0]["siteId"], 2)

    def test_sanitizes_known_source_data_anomalies(self):
        site = {"name": "Untied States"}
        goods = {
            "minPrice": 12,
            "maxPrice": 999999,
            "totalSold": 177,
            "totalSales": 1169.97,
            "monthSold": 22451250,
            "monthSales": 142565437.5,
            "monthSoldRate": 3,
            "monthSalesRate": 4,
            "sku": [{"price": 999999}],
        }

        sanitize_site(site)
        sanitize_goods_metrics(goods, include_skus=True)

        self.assertEqual(site["name"], "United States")
        self.assertIsNone(goods["maxPrice"])
        self.assertIsNone(goods["sku"][0]["price"])
        self.assertIsNone(goods["monthSold"])
        self.assertIsNone(goods["monthSales"])


if __name__ == "__main__":
    unittest.main()
