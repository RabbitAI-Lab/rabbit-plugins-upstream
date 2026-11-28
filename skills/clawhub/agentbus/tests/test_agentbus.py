#!/usr/bin/env python3
"""agentbus v0.2 自测。零依赖，直接 python3 tests/test_agentbus.py 跑。

每个用例都起独立临时总线，互不干扰。断言的是"出错时会不会留下错误记录"，
不只是"顺利时能不能跑通"。
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "agentbus.py"


class BusCase(unittest.TestCase):
    def setUp(self) -> None:
        self.base = Path(tempfile.mkdtemp(prefix="agentbus-test-"))
        self.root = self.base / "bus"

    def tearDown(self) -> None:
        shutil.rmtree(self.base, ignore_errors=True)

    # -- 帮手

    def run_cli(self, *args, expect_ok=True):
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root), *args],
            capture_output=True,
            text=True,
        )
        if expect_ok and proc.returncode != 0:
            self.fail(f"{args} 失败（exit {proc.returncode}）\n{proc.stdout}\n{proc.stderr}")
        return proc

    def json_of(self, *args):
        return json.loads(self.run_cli(*args).stdout)

    def init(self):
        return self.json_of("init")

    def dispatch(self, *extra, title="测试任务", goal="把活干完"):
        return self.json_of("dispatch", "--title", title, "--goal", goal, *extra)

    def write_receipt(self, task_id, verdict="结论：COMPLETED", body="干完了。"):
        path = self.root / "tasks" / task_id / "回执包.md"
        path.write_text(f"# 回执包 {task_id}\n\n{body}\n\n{verdict}\n", encoding="utf-8")
        return path

    def ledger_text(self):
        return (self.root / "shared" / "ledger.md").read_text(encoding="utf-8")

    # -- 初始化

    def test_init_creates_structure_and_contract(self):
        payload = self.init()
        self.assertEqual(payload["status"], "INITIALIZED")
        for relative in ("tasks", "queue/pending", "queue/claimed", "shared/review", "CONTRACT.md"):
            self.assertTrue((self.root / relative).exists(), relative)
        contract = (self.root / "CONTRACT.md").read_text(encoding="utf-8")
        self.assertIn(str(self.root), contract)
        self.assertIn("## 参与者", contract)

    def test_init_on_existing_bus_attaches_instead_of_refusing(self):
        """接管旧总线是主场景：已存在就该挂上去补齐缺件，而不是报错。"""
        self.init()
        task_id = self.dispatch()["id"]
        ledger_before = self.ledger_text()
        payload = json.loads(self.run_cli("init").stdout)
        self.assertEqual(payload["status"], "ATTACHED")
        self.assertIn("未改动", payload["reused"])
        self.assertEqual(payload["counts"]["pending"], 1)
        self.assertEqual(self.ledger_text(), ledger_before)  # 历史记录一行没动
        self.assertTrue((self.root / "queue" / "pending" / f"{task_id}.json").is_file())

    # -- 派单

    def test_dispatch_auto_id_and_package(self):
        self.init()
        payload = self.dispatch()
        self.assertRegex(payload["id"], r"^T-\d{8}-\d{3}$")
        package = Path(payload["package"])
        self.assertTrue(package.is_file())
        text = package.read_text(encoding="utf-8")
        self.assertIn("把活干完", text)
        self.assertIn(payload["id"], text)
        self.assertIn("结论：COMPLETED", text)  # 任务包里就得告诉人怎么写结论

    def test_dispatch_sequence_increments(self):
        self.init()
        first = self.dispatch()["id"]
        second = self.dispatch()["id"]
        self.assertNotEqual(first, second)
        self.assertEqual(int(second[-3:]), int(first[-3:]) + 1)

    def test_duplicate_id_refused(self):
        self.init()
        payload = self.dispatch()
        proc = self.run_cli(
            "dispatch", "--id", payload["id"], "--title", "重复", "--goal", "x", expect_ok=False
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("已存在", proc.stderr)

    def test_bad_id_refused(self):
        self.init()
        proc = self.run_cli(
            "dispatch", "--id", "../evil", "--title", "t", "--goal", "g", expect_ok=False
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("无效编号", proc.stderr)

    # -- 领取

    def test_claim_takes_lease(self):
        self.init()
        task_id = self.dispatch()["id"]
        payload = self.json_of("claim", "--worker", "alice")
        self.assertEqual(payload["status"], "IN_PROGRESS")
        self.assertEqual(payload["claimed_by"], "alice")
        self.assertEqual(payload["attempt"], 1)
        self.assertTrue((self.root / "queue" / "claimed" / f"{task_id}.json").is_file())

    def test_claim_empty_queue_is_not_an_error(self):
        self.init()
        payload = self.json_of("claim", "--worker", "alice")
        self.assertEqual(payload["status"], "EMPTY")

    def test_claim_quarantines_corrupt_pending_file(self):
        self.init()
        (self.root / "queue" / "pending" / "T-20261128-999.json").write_text("{broken", encoding="utf-8")
        proc = self.run_cli("claim", "--worker", "alice")
        self.assertIn("QUARANTINED", proc.stderr)
        self.assertTrue((self.root / "queue" / "corrupt" / "T-20261128-999.json").is_file())
        self.assertEqual(json.loads(proc.stdout)["status"], "EMPTY")

    # -- 提交

    def test_complete_happy_path_updates_ledger_with_real_worker(self):
        self.init()
        task_id = self.dispatch(title="写一份报告")["id"]
        self.run_cli("claim", "--worker", "alice")
        self.write_receipt(task_id)
        payload = self.json_of("complete", "--id", task_id)
        self.assertEqual(payload["result"], "COMPLETED")
        self.assertEqual(payload["ledger"], "updated")
        self.assertEqual(payload["worker"], "alice")
        line = [row for row in self.ledger_text().splitlines() if task_id in row][0]
        self.assertIn("alice", line)  # 不是派单时的占位名
        self.assertIn("COMPLETED", line)
        review = Path(payload["review"]).read_text(encoding="utf-8")
        self.assertIn(task_id, review)

    def test_pass_is_accepted_as_completed(self):
        self.init()
        task_id = self.dispatch()["id"]
        self.run_cli("claim", "--worker", "alice")
        self.write_receipt(task_id, verdict="结论：PASS")
        payload = self.json_of("complete", "--id", task_id)
        self.assertEqual(payload["result"], "COMPLETED")

    def test_verdict_inside_sentence_is_not_a_verdict(self):
        """最危险的一种：正文里写着"未达到 PASS"，不能被读成通过。"""
        self.init()
        task_id = self.dispatch()["id"]
        self.run_cli("claim", "--worker", "alice")
        self.write_receipt(task_id, verdict="本次核查未达到 PASS，仍需返工。")
        proc = self.run_cli("complete", "--id", task_id, expect_ok=False)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("缺少结论", proc.stderr)
        self.assertTrue((self.root / "queue" / "claimed" / f"{task_id}.json").is_file())

    def test_unknown_verdict_is_refused(self):
        self.init()
        task_id = self.dispatch()["id"]
        self.run_cli("claim", "--worker", "alice")
        self.write_receipt(task_id, verdict="结论：APPROVED")
        proc = self.run_cli("complete", "--id", task_id, expect_ok=False)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("不在允许集", proc.stderr)

    def test_two_verdicts_are_refused(self):
        self.init()
        task_id = self.dispatch()["id"]
        self.run_cli("claim", "--worker", "alice")
        self.write_receipt(task_id, verdict="结论：COMPLETED\n\n结论：PARTIAL")
        proc = self.run_cli("complete", "--id", task_id, expect_ok=False)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("多个不同结论", proc.stderr)

    def test_missing_receipt_is_refused(self):
        self.init()
        task_id = self.dispatch()["id"]
        self.run_cli("claim", "--worker", "alice")
        proc = self.run_cli("complete", "--id", task_id, expect_ok=False)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("回执不存在", proc.stderr)

    def test_complete_before_claim_gives_hint(self):
        self.init()
        task_id = self.dispatch()["id"]
        self.write_receipt(task_id)
        proc = self.run_cli("complete", "--id", task_id, expect_ok=False)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("先 claim", proc.stderr)

    def test_result_flag_must_match_receipt(self):
        self.init()
        task_id = self.dispatch()["id"]
        self.run_cli("claim", "--worker", "alice")
        self.write_receipt(task_id, verdict="结论：COMPLETED")
        proc = self.run_cli("complete", "--id", task_id, "--result", "FAIL", expect_ok=False)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("不一致", proc.stderr)

    def test_fail_moves_to_failed_and_records(self):
        self.init()
        task_id = self.dispatch()["id"]
        self.run_cli("claim", "--worker", "alice")
        self.write_receipt(task_id, verdict="结论：FAIL")
        payload = self.json_of("complete", "--id", task_id)
        self.assertEqual(payload["status"], "FAILED")
        self.assertTrue((self.root / "queue" / "failed" / f"{task_id}.json").is_file())
        self.assertIn("FAIL", self.ledger_text())

    def test_ledger_row_is_backfilled_when_missing(self):
        """队列是手工建的、或从备份恢复的：台账里没有行也不能静默漏记。"""
        self.init()
        task_id = self.dispatch()["id"]
        self.run_cli("claim", "--worker", "alice")
        self.write_receipt(task_id)
        ledger = self.root / "shared" / "ledger.md"
        header = ledger.read_text(encoding="utf-8").split("|---|---|---|---|---|---|---|")[0] + "|---|---|---|---|---|---|---|\n"
        ledger.write_text(header, encoding="utf-8")
        payload = self.json_of("complete", "--id", task_id)
        self.assertEqual(payload["ledger"], "appended")
        self.assertIn(task_id, ledger.read_text(encoding="utf-8"))

    # -- 运维

    def test_requeue_puts_expired_task_back(self):
        self.init()
        task_id = self.dispatch("--lease-seconds", "1")["id"]
        self.run_cli("claim", "--worker", "alice")
        time.sleep(1.2)
        self.assertEqual(self.json_of("status")["lease_expired"], [task_id])
        payload = self.json_of("requeue")
        self.assertEqual(payload["ids"], [task_id])
        self.assertTrue((self.root / "queue" / "pending" / f"{task_id}.json").is_file())
        claim = self.json_of("claim", "--worker", "bob")
        self.assertEqual(claim["attempt"], 2)  # 次数累加，能看出被领过两次

    def test_heartbeat_extends_lease(self):
        self.init()
        task_id = self.dispatch("--lease-seconds", "60")["id"]
        before = self.json_of("claim", "--worker", "alice")["lease_expires_at"]
        after = self.json_of("heartbeat", "--id", task_id, "--seconds", "600")["lease_expires_at"]
        self.assertGreater(after, before)

    def test_doctor_ok_on_fresh_bus(self):
        self.init()
        payload = self.json_of("doctor")
        self.assertEqual(payload["status"], "OK")

    def test_doctor_reports_missing_package_and_fixes(self):
        self.init()
        task_id = self.dispatch()["id"]
        (self.root / "tasks" / task_id / "任务包.md").unlink()
        proc = self.run_cli("doctor", expect_ok=False)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("任务包缺失", proc.stdout)
        self.json_of("doctor", "--fix")
        self.assertTrue((self.root / "queue" / "corrupt" / f"{task_id}.json").is_file())

    # -- 契约与适配

    def test_contract_participants_are_parsed(self):
        self.init()
        self.run_cli("claim", "--worker", "stranger")
        # 副本里没有 pending 也无所谓：警告只看名字在不在契约里
        proc = self.run_cli("claim", "--worker", "stranger")
        self.assertIn("不在 CONTRACT.md", proc.stderr)

    def test_adapter_prints_contract_path(self):
        self.init()
        proc = self.run_cli("adapter", "codex")
        self.assertIn(str(self.root / "CONTRACT.md"), proc.stdout)
        self.assertIn("claim", proc.stdout)

    def test_adapter_refuses_to_overwrite_without_force(self):
        self.init()
        target = self.base / "AGENTS.md"
        target.write_text("已有内容\n", encoding="utf-8")
        proc = self.run_cli("adapter", "codex", "--write", str(target), expect_ok=False)
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(target.read_text(encoding="utf-8"), "已有内容\n")
        self.run_cli("adapter", "codex", "--write", str(target), "--force")
        self.assertIn("已有内容", target.read_text(encoding="utf-8"))
        self.assertIn("CONTRACT.md", target.read_text(encoding="utf-8"))

    # -- 端到端

    def test_demo_runs_end_to_end(self):
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "demo"], capture_output=True, text=True
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("台账新增的行", proc.stdout)
        self.assertIn("COMPLETED", proc.stdout)
        self.assertIn("临时目录已清理", proc.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
