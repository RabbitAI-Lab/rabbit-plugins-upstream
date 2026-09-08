import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import mercadolibre_category_info
import mercadolibre_category_list
import mercadolibre_goods_info
import mercadolibre_goods_search
import mercadolibre_mall_info
import mercadolibre_mall_search
import mercadolibre_review_search
import mercadolibre_site_list
from mercadolibre_search_common import build_url, validate_object_response, validate_search_response


class ParameterTests(unittest.TestCase):
    def test_goods_accepts_supported_filters(self):
        params = mercadolibre_goods_search.parse_params([
            "siteId=2", "catId=MLB123", "totalSoldMin=100", "priceMax=50",
            "goodsScoreMin=4.2", "full=true", "crossBorder=false",
            "sort=totalSold", "order=desc", "page=1", "size=100",
        ])
        self.assertIn(("catId", "MLB123"), params)

    def test_goods_rejects_unsupported_conditions(self):
        for value in ("imageUrl=x", "order=descend", "sort=mallReviewNum", "full=yes"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                mercadolibre_goods_search.parse_params([value])
        with self.assertRaises(ValueError):
            mercadolibre_goods_search.parse_params(["page=2", "size=200"])

    def test_mall_and_review_validation(self):
        self.assertIn(("sort", "mallSold"), mercadolibre_mall_search.parse_params([
            "mallSoldMin=1000", "sort=mallSold",
        ]))
        with self.assertRaises(ValueError):
            mercadolibre_mall_search.parse_params(["sort=reviewNum"])
        with self.assertRaises(ValueError):
            mercadolibre_review_search.parse_params(["scoreMin=1"])
        self.assertIn(("goodsId", "MLB123"), mercadolibre_review_search.parse_params([
            "goodsId=MLB123", "scoreMax=2", "sort=helpful",
        ]))

    def test_identifier_commands(self):
        with self.assertRaises(ValueError):
            mercadolibre_goods_info.build_params(" ", 1)
        with self.assertRaises(ValueError):
            mercadolibre_mall_info.build_params("", 1)
        with self.assertRaises(ValueError):
            mercadolibre_category_info.build_params("", 1)
        self.assertEqual(mercadolibre_category_list.build_params("0", 1)[0], ("parentCatId", "0"))


class ContractTests(unittest.TestCase):
    def test_site_resolution(self):
        sites = [
            {"siteId": 1, "regionId": "MLM", "name": "Mexico", "cnName": "墨西哥"},
            {"siteId": 2, "regionId": "MLB", "name": "Brazil", "cnName": "巴西"},
        ]
        self.assertEqual(mercadolibre_site_list.resolve_site(sites, "巴西")[0]["siteId"], 2)
        self.assertEqual(mercadolibre_site_list.resolve_site(sites, "mlm")[0]["siteId"], 1)

    def test_response_contracts_and_encoding(self):
        search = {"code": 0, "data": {"total": 1, "list": [{}], "site": {"siteId": 1}}}
        self.assertEqual(validate_search_response(search, "失败"), search)
        detail = {"code": 0, "data": {"goods": {}, "site": {"siteId": 1}, "history": []}}
        self.assertEqual(validate_object_response(detail, "goods", "失败"), detail)
        self.assertEqual(
            build_url("https://example.test/", "/search", [("keyword", "wireless mouse")]),
            "https://example.test/search?keyword=wireless+mouse",
        )


if __name__ == "__main__":
    unittest.main()
