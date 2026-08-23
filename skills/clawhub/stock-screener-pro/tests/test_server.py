import os
import sys
import unittest
from unittest.mock import patch


SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if SKILL_DIR not in sys.path:
    sys.path.insert(0, SKILL_DIR)

import server


class BacktestAccountingTests(unittest.TestCase):
    def test_sell_proceeds_are_added_to_cash(self):
        closes = ([10.0] * 20) + ([12.0] * 5) + ([8.0] * 10)
        bars = [
            {
                "date": f"2026-01-{index + 1:02d}",
                "open": close,
                "close": close,
                "high": close,
                "low": close,
                "vol": 1000.0,
            }
            for index, close in enumerate(closes)
        ]
        with patch.object(server, "_fetch_kline", return_value=bars):
            result = server.backtest_strategy("600519", strategy="sma_cross")

        sell_trades = [trade for trade in result["recent_trades"] if trade["action"] == "SELL"]
        self.assertTrue(sell_trades)
        self.assertGreater(sell_trades[-1]["cash_after"], 0)
        self.assertGreater(result["final_capital"], 0)


class DsaSecurityTests(unittest.TestCase):
    def test_remote_dsa_is_always_blocked(self):
        with patch.object(server, "DSA_BASE_URL", "https://example.com"):
            url, error = server._validated_dsa_base_url()
        self.assertIsNone(url)
        self.assertIn("仅允许", error)

    def test_loopback_dsa_is_allowed(self):
        with patch.object(server, "DSA_BASE_URL", "http://127.0.0.1:8000"):
            url, error = server._validated_dsa_base_url()
        self.assertEqual(url, "http://127.0.0.1:8000")
        self.assertIsNone(error)


class StockCodeValidationTests(unittest.TestCase):
    def test_standard_stock_code_forms_are_normalized(self):
        self.assertEqual(server._clean_code("600519.SH"), ("sh", "600519"))
        self.assertEqual(server._clean_code("sz000001"), ("sz", "000001"))

    def test_stock_code_rejects_non_six_digit_input(self):
        with self.assertRaises(ValueError):
            server._clean_code("600519&unexpected=value")


class TonghuashunParserTests(unittest.TestCase):
    def test_realtime_quote_response_is_normalized(self):
        response = {
            "errorcode": 0,
            "tables": [
                {
                    "thscode": "600519.SH",
                    "table": {
                        "latest": [1500.0],
                        "open": [1490.0],
                        "high": [1510.0],
                        "low": [1488.0],
                        "preClose": [1480.0],
                        "changeRatio": [1.3514],
                        "turnoverRatio": [0.42],
                        "volume": [123400.0],
                        "amount": [185100000.0],
                    },
                }
            ],
        }
        stocks = [{"code": "600519", "name": "贵州茅台", "market": "sh"}]
        with patch.object(server, "_ths_post", return_value=response):
            quotes = server._fetch_batch_quotes_ths(stocks)

        self.assertEqual(len(quotes), 1)
        self.assertEqual(quotes[0]["code"], "600519")
        self.assertEqual(quotes[0]["name"], "贵州茅台")
        self.assertEqual(quotes[0]["price"], 1500.0)
        self.assertEqual(quotes[0]["data_source"], "tonghuashun-ifind")

    def test_history_response_is_normalized(self):
        response = {
            "errorcode": 0,
            "tables": [
                {
                    "thscode": "600519.SH",
                    "time": ["2026-08-20", "2026-08-21"],
                    "table": {
                        "open": [1490.0, 1500.0],
                        "high": [1510.0, 1520.0],
                        "low": [1480.0, 1495.0],
                        "close": [1505.0, 1515.0],
                        "volume": [1000.0, 1200.0],
                    },
                }
            ],
        }
        with patch.object(server, "_ths_post", return_value=response):
            bars = server._fetch_kline_ths("600519", count=2)

        self.assertEqual([bar["date"] for bar in bars], ["2026-08-20", "2026-08-21"])
        self.assertEqual(bars[-1]["close"], 1515.0)
        self.assertEqual(bars[-1]["data_source"], "tonghuashun-ifind")


class NetworkTransportTests(unittest.TestCase):
    def test_tencent_quote_fallback_uses_https(self):
        with patch.object(server.urllib.request, "urlopen") as opener:
            opener.return_value.__enter__.return_value.read.return_value = b""
            server._fetch_batch_quotes_tencent(
                [{"code": "600519", "name": "贵州茅台", "market": "sh"}]
            )
        request = opener.call_args.args[0]
        self.assertTrue(request.full_url.startswith("https://qt.gtimg.cn/"))

    def test_tencent_kline_fallback_uses_https(self):
        response = b'{"data":{"sh600519":{"qfqday":[]}}}'
        with patch.object(server.urllib.request, "urlopen") as opener:
            opener.return_value.__enter__.return_value.read.return_value = response
            server._fetch_kline_tencent("600519", count=2)
        request = opener.call_args.args[0]
        self.assertTrue(request.full_url.startswith("https://ifzq.gtimg.cn/"))


if __name__ == "__main__":
    unittest.main()
