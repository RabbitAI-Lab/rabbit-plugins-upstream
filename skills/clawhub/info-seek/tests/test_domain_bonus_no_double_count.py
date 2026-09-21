#!/usr/bin/env python3
"""test_domain_bonus_no_double_count.py — R1-b/P2-5 domain_bonus 收敛守护

锁定三链路口径一致性（§8.4）：
- 聚合真源 aggregate_score_v2 正确计入 domain_bonus（链A 路径）
- 链B score_source 报告 domain_bonus 字段但不计入 final（防双重计分，
  因链B 的 trust_bonus 已含 KB 段，见 infoseek_core_v2.score_source 口径声明）
纯 import，无网络、无副作用。
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / 'core'))
sys.path.insert(0, str(ROOT / 'scripts'))

_fails = []


def check(name, cond, detail=''):
    if cond:
        print(f'  [PASS] {name}')
    else:
        _fails.append(name)
        print(f'  [FAIL] {name} {detail}')


def main():
    from anchor_score_v2 import aggregate_score_v2, compute_final_score_v2  # noqa: E402
    from infoseek_core_v2 import score_source  # noqa: E402

    print('--- 链A 聚合真源 domain_bonus 计入 final ---')
    r_agg = aggregate_score_v2(40, trust_bonus=10, domain_bonus=20)
    check('链A 聚合计入 domain_bonus', r_agg['final_score'] == 70, str(r_agg))

    print('--- 链B score_source 报告 domain_bonus 但不计入 final（无双重计分）---')
    # 用 _scoring 注入非零 domain_bonus，验证链B 不折叠进 final
    src = {'score': 40, 'url': 'https://example.com/x', 'title': 't', 'snippet': 's',
           '_scoring': {'domain_bonus': 12}}
    rb = score_source(src, '主题', prefer_kb=False)
    exp_b = min(rb['base_score'] + rb['trust_bonus'], 100)
    check('链B final 不计入 domain_bonus（_scoring=12 仍不折叠）',
          rb['domain_bonus'] == 12 and rb['final_score'] == exp_b,
          f"domain={rb.get('domain_bonus')} final={rb['final_score']} != exp={exp_b}")
    check('链B 报告 domain_bonus 字段', 'domain_bonus' in rb, str(sorted(rb.keys())))

    print('--- 链A compute_final_score_v2 经聚合真源计入 domain ---')
    ra = compute_final_score_v2({'score': 40, 'url': 'https://example.com/x'},
                                '主题', with_domain=True, prefer_kb=True)
    exp_a = aggregate_score_v2(ra['base_score'], trust_bonus=ra['trust_bonus'],
                               domain_bonus=ra.get('domain_bonus', 0))['final_score']
    check('链A final == aggregate(base,trust,domain)（domain 已计入）',
          ra['after_whitelist_final'] == exp_a,
          f"final={ra['after_whitelist_final']} != exp={exp_a} ra={ra}")

    print()
    if _fails:
        print(f'FAIL: {len(_fails)} 项失败 → {_fails}')
        sys.exit(1)
    print('ALL PASS (test_domain_bonus_no_double_count) ✅')
    sys.exit(0)


if __name__ == '__main__':
    main()
