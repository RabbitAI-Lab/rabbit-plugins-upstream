import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import coupang_category_info
import coupang_category_list
import coupang_goods_info
import coupang_goods_search
import coupang_site_list
from coupang_search_common import build_url, validate_object_response, validate_search_response


class ParameterTests(unittest.TestCase):
    def test_goods_accepts_supported_filters(self):
        params = coupang_goods_search.parse_params([
            "siteId=1", "leafCategoryCode=123", "salesLast28dMin=100", "priceMax=50000",
            "ratingMin=4.2", "displayDeliveryMethod=ROCKET", "sort=salesLast28d",
            "order=desc", "page=1", "size=100",
        ])
        self.assertIn(("leafCategoryCode", "123"), params)

    def test_goods_rejects_unsupported_conditions(self):
        for value in ("imageUrl=x", "order=descend", "sort=mallReviewNum", "siteId=2"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                coupang_goods_search.parse_params([value])
        with self.assertRaises(ValueError):
            coupang_goods_search.parse_params(["page=2", "size=200"])

    def test_identifier_commands(self):
        with self.assertRaises(ValueError):
            coupang_goods_info.build_params(" ", None, 1)
        with self.assertRaises(ValueError):
            coupang_category_info.build_params(0, 1)
        self.assertEqual(coupang_category_list.build_params(0, 1)[0], ("parentId", "0"))


class ContractTests(unittest.TestCase):
    def test_site_resolution(self):
        sites = [{
            "siteId": 1, "siteCode": "KR", "country": "KR", "name": "韩国", "currency": "KRW",
        }]
        self.assertEqual(coupang_site_list.resolve_site(sites, "韩国")[0]["siteId"], 1)
        self.assertEqual(coupang_site_list.resolve_site(sites, "kr")[0]["currency"], "KRW")

    def test_response_contracts_and_encoding(self):
        search = {"code": 0, "data": {"total": 1, "list": [{}], "site": {"siteId": 1}}}
        self.assertEqual(validate_search_response(search, "失败"), search)
        detail = {
            "code": 0,
            "data": {"goods": {}, "items": [], "history": [], "site": {"siteId": 1}},
        }
        self.assertEqual(validate_object_response(detail, "goods", "失败"), detail)
        self.assertEqual(
            build_url("https://example.test/", "/search", [("keyword", "wireless mouse")]),
            "https://example.test/search?keyword=wireless+mouse",
        )


if __name__ == "__main__":
    unittest.main()
