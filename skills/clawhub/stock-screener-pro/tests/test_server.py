import os
import sys
import unittest
import json
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

    def test_new_strategy_catalog_has_book_research_templates(self):
        catalog = server.get_strategies()
        self.assertIn("book_volume_turnover", {item["id"] for item in catalog["screening_strategies"]})
        self.assertIn("ma_5_10_60_trend", {item["id"] for item in catalog["backtest_strategies"]})
        self.assertIn("macd_cross_trend", {item["id"] for item in catalog["backtest_strategies"]})


class TechnicalResearchSnapshotTests(unittest.TestCase):
    def test_snapshot_exposes_research_observations_and_data_limits(self):
        bars = []
        for i in range(65):
            close = 10.0 + i * 0.12
            bars.append({
                "date": f"2026-01-{i + 1:02d}",
                "open": close - 0.05,
                "close": close,
                "high": close + 0.1,
                "low": close - 0.1,
                "vol": 1000.0 + i * 10,
            })
        snapshot = server._technical_research_snapshot(bars, {"pct_chg": 1.0, "vol_ratio": 1.8})
        self.assertEqual(snapshot["status"], "success")
        self.assertEqual(snapshot["ma_5_10_60"]["alignment"], "多头排列")
        self.assertIn("macd_12_26_9", snapshot)
        self.assertIn("kdj_9_3_3", snapshot)
        self.assertTrue(snapshot["research_only"])
        self.assertTrue(any("宝塔线" in item for item in snapshot["data_limits"]))


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


class Ai4TradeIntegrationTests(unittest.TestCase):
    def test_account_query_requires_environment_token_without_network_call(self):
        with patch.object(server, "AI4TRADE_TOKEN", ""), patch.object(server.urllib.request, "urlopen") as opener:
            result = server.get_ai4trade_account()
        self.assertEqual(result["status"], "error")
        opener.assert_not_called()

    def test_mutation_is_blocked_without_explicit_confirmation(self):
        with patch.object(server.urllib.request, "urlopen") as opener:
            result = server.manage_ai4trade_follow(leader_id=10, confirm=False)
        self.assertEqual(result["status"], "confirmation_required")
        opener.assert_not_called()


class QuantResearchAdapterTests(unittest.TestCase):
    def test_vibe_research_rejects_order_intent_before_subprocess(self):
        with patch.object(server, "_run_research_backend") as runner:
            result = server.run_vibe_trading_research("请帮我下单买入 600519", confirm_external_ai=True)
        self.assertEqual(result["status"], "error")
        runner.assert_not_called()

    def test_vibe_research_requires_external_ai_confirmation(self):
        with patch.object(server, "_run_research_backend") as runner:
            result = server.run_vibe_trading_research("回测 600519 的均线策略", confirm_external_ai=False)
        self.assertEqual(result["status"], "confirmation_required")
        runner.assert_not_called()

    def test_vibe_research_uses_fixed_local_command_and_guard_prompt(self):
        fake_result = {"status": "success", "stdout": "{}", "stderr": "", "exit_code": 0}
        with patch.object(server.shutil, "which", return_value="/usr/local/bin/vibe-trading"), patch.object(
            server, "_run_research_backend", return_value=fake_result
        ) as runner:
            result = server.run_vibe_trading_research("回测 600519 的均线策略", confirm_external_ai=True)
        command = runner.call_args.args[0]
        self.assertEqual(command[0], "/usr/local/bin/vibe-trading")
        self.assertIn("--json", command)
        self.assertIn("Do not select or use broker connectors", command[-1])
        self.assertTrue(result["research_only"])

    def test_a_share_ticker_is_normalized_for_tradingagents(self):
        self.assertEqual(server._a_share_ticker("600519.SH"), "600519.SS")
        self.assertEqual(server._a_share_ticker("sz000001"), "000001.SZ")

    def test_vibe_swarm_maps_topic_to_the_upstream_preset_schema(self):
        fake_result = {"status": "success", "stdout": "{}", "stderr": "", "exit_code": 0}
        with patch.object(server.shutil, "which", return_value="/usr/local/bin/vibe-trading"), patch.object(
            server, "_run_research_backend", return_value=fake_result
        ) as runner:
            result = server.run_vibe_trading_swarm(
                "investment_committee", "贵州茅台估值与风险", confirm_external_ai=True
            )
        payload = json.loads(runner.call_args.args[0][-1])
        self.assertEqual(payload["target"], "贵州茅台估值与风险")
        self.assertIn("market", payload)
        self.assertTrue(result["research_only"])

    def test_tradingagents_requires_confirmation_before_import_or_run(self):
        with patch.object(server, "_python_has_module") as module_check:
            result = server.run_agent_research(
                engine="tradingagents", stock_code="600519", analysis_date="2026-08-20", confirm_external_ai=False
            )
        self.assertEqual(result["status"], "confirmation_required")
        module_check.assert_not_called()

    def test_skill_status_has_only_supported_agent_backends(self):
        with patch.object(server, "_python_has_module", return_value=True), patch.object(
            server.shutil, "which", return_value="/usr/local/bin/vibe-trading"
        ):
            result = server.get_skill_status()
        self.assertIn("agent_research", result)
        self.assertEqual(set(result["agent_research"]), {
            "research_only",
            "no_background_jobs",
            "no_broker_orders",
            "vibe_trading_command_available",
            "tradingagents_package_available",
            "openclaw_model_bridge_available",
            "backend_python_configured",
            "artifact_dir",
        })

    def test_skill_status_can_return_compacted_legacy_catalog_and_cache(self):
        with patch.object(server, "get_strategies", return_value={"screening_strategies": []}), patch.object(
            server, "predict_cache_status", return_value={"cached_count": 0}
        ):
            result = server.get_skill_status(include_details=True)
        self.assertEqual(result["strategy_catalog"], {"screening_strategies": []})
        self.assertEqual(result["prediction_cache"], {"cached_count": 0})

    def test_ai4trade_aggregator_routes_read_requests(self):
        with patch.object(server, "get_ai4trade_account", return_value={"status": "success", "account": {}}) as account:
            result = server.get_ai4trade(resource="account")
        self.assertEqual(result["status"], "success")
        account.assert_called_once()

    def test_ai4trade_aggregator_keeps_mutations_confirmation_gated(self):
        with patch.object(server.urllib.request, "urlopen") as opener:
            result = server.manage_ai4trade(action="follow", leader_id=10, confirm=False)
        self.assertEqual(result["status"], "confirmation_required")
        opener.assert_not_called()

    def test_authenticated_request_uses_fixed_ai4trade_host(self):
        response = json.dumps({"signals": []}).encode("utf-8")
        with patch.object(server, "AI4TRADE_TOKEN", "test-token"), patch.object(
            server.urllib.request, "urlopen"
        ) as opener:
            opener.return_value.__enter__.return_value.read.return_value = response
            result = server.get_ai4trade_signal_feed(limit=5)
        request = opener.call_args.args[0]
        self.assertEqual(result["status"], "success")
        self.assertTrue(result["untrusted_external_data"])
        self.assertTrue(request.full_url.startswith("https://ai4trade.ai/api/signals/feed?"))
        self.assertEqual(request.get_header("Authorization"), "Bearer test-token")

    def test_points_exchange_is_blocked_without_explicit_confirmation(self):
        with patch.object(server.urllib.request, "urlopen") as opener:
            result = server.exchange_ai4trade_points(amount=10, confirm=False)
        self.assertEqual(result["status"], "confirmation_required")
        opener.assert_not_called()


if __name__ == "__main__":
    unittest.main()
