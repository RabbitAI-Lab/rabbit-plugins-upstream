import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

from task_plan import approve, plan, verify_plan


def config():
    return {
        'input_type': 'brand_product',
        'name_type': 'category',
        'name': '电视',
        'brand': '海信',
        'date': '2026-09-11',
        'questions': [
            {'id': 'Q01', 'prompt': '预算3000元左右，有哪些电视值得买？', 'intent': '预算选择'},
            {'id': 'Q02', 'prompt': '画质好的电视有哪些推荐？', 'intent': '画质需求'},
        ],
        'combinations': [
            {'name': 'DOUBA', 'thinking_enabled': 0},
            {'name': 'TXYB', 'thinking_enabled': 0},
            {'name': 'TXYBA', 'thinking_enabled': 0},
            {'name': 'TYQWA', 'thinking_enabled': 0},
            {'name': 'TYQWA', 'thinking_enabled': 1},
        ],
        'repeats': 1,
        'sources': [],
    }


class PaidSamplingWorkflow(unittest.TestCase):
    def test_lists_only_supported_product_card_combinations_with_points(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / 'task_plan.py'), 'list-platforms'],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        catalog = json.loads(result.stdout)
        self.assertEqual(
            [(x['平台'], x['终端'], x['模式'], x['单次积分']) for x in catalog],
            [
                ('豆包', '手机', '快速', '0.8'),
                ('元宝', '网页', '快速', '0.8'),
                ('元宝', '手机', '快速', '1'),
                ('千问', '手机', '快速', '1'),
                ('千问', '手机', '深度', '1'),
            ],
        )

    def test_default_catalog_builds_auditable_quote_and_confirmation_card(self):
        planned = plan(config())
        self.assertEqual(planned['task_count'], 10)
        self.assertEqual(planned['total_points'], '9.2')
        self.assertTrue(planned['diagnosis_id'].startswith('aidso-product-20260911-'))
        self.assertIn('海信-电视-2题-5组合', planned['task_name'])
        self.assertEqual(planned['price_source_checked_at'], '2026-08-25')
        card = planned['confirmation_card']
        self.assertIn('确认报价积分：9.2', card)
        self.assertIn('预算3000元左右，有哪些电视值得买？', card)
        self.assertIn('千问·手机版 · 深度：2 次 × 1 = 2 积分', card)
        self.assertIn('只有明确回复“确认执行”', card)

    def test_non_exact_confirmation_is_rejected_even_with_a_complete_quote(self):
        planned = plan(config())
        with self.assertRaisesRegex(ValueError, '确认执行'):
            approve(planned, planned['plan_hash'], '好的')

    def test_cli_writes_manifest_only_inside_task_registry(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            plan_file = workspace / 'plan.json'
            plan_file.write_text(json.dumps(config(), ensure_ascii=False), encoding='utf-8')
            outside = workspace / 'tasks.json'
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / 'task_plan.py'), 'plan', '--config', str(plan_file), '--out', str(outside)],
                cwd=workspace,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(outside.exists())

    def test_price_tampering_invalidates_plan(self):
        planned = plan(config())
        planned['tasks'][0]['unit_points'] = '0'
        planned['total_points'] = '8.4'
        with self.assertRaises(ValueError):
            verify_plan(planned)


if __name__ == '__main__':
    unittest.main()
