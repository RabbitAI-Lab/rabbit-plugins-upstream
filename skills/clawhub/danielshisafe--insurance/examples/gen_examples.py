#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""生成两个示例保单 JSON，用于冒烟测试 irr.py（数据为虚构演示，非真实产品）。

只生成：example_增额寿分红.json、example_年金附万能.json。
注意：example_年金分红_累积生息.json 是**手写**的（含当年红利列 + _selfcheck 自检块），
      用于演示 stress_test.py 的复利修正（reaccum），本脚本**不会**覆盖它。
请在 examples/ 目录下运行：python gen_examples.py
"""
import json

# 产品A：增额终身寿（分红，累积生息）
A = {"start_date": "2026-01-01", "premiums": [10000] * 10}
cv_g, div_g, cv_d, div_d = [], [], [], []
for n in range(31):
    cv = 0 if n == 0 else (int(98000 * (n / 10)) if n <= 10 else int(98000 * (1.028 ** (n - 10))))
    d = 0 if n < 5 else int(2000 * (n - 4))
    cv_g.append(cv); div_g.append(d)
    cv_d.append(int(cv * 1.05)); div_d.append(int(d * 1.3))
A.update(cv_guaranteed=cv_g, dividend_cv_guaranteed=div_g,
         cv_demo=cv_d, dividend_cv_demo=div_d)

# 产品B：年金（附加万能），生存金自动进万能账户复利
B = {"start_date": "2026-01-01", "premiums": [10000] * 10}
ben, cv, uni, uni_d = [], [], [], []
acc_g, acc_d, rg, rd = 0.0, 0.0, 1.0175, 1.045
for n in range(31):
    b = 0 if n < 5 else 6000
    ben.append(b)
    c = int(max(0, 40000 - 1200 * n)) if n <= 10 else int(max(0, 28000 - 600 * (n - 10)))
    cv.append(c)
    acc_g = acc_g * rg + (b if b else 0) if n == 0 else acc_g * rg + b
    acc_d = acc_d * rd + (b if b else 0) if n == 0 else acc_d * rd + b
    # 简化：首年无积累
    if n == 0:
        acc_g, acc_d = 0.0, 0.0
    uni.append(int(acc_g)); uni_d.append(int(acc_d))
B.update(benefit_guaranteed=ben, cv_guaranteed=cv, universal_guaranteed=uni,
         benefit_demo=ben, cv_demo=cv, universal_demo=uni_d)

with open("example_增额寿分红.json", "w", encoding="utf-8") as f:
    json.dump(A, f, ensure_ascii=False, indent=2)
with open("example_年金附万能.json", "w", encoding="utf-8") as f:
    json.dump(B, f, ensure_ascii=False, indent=2)
print("示例 JSON 已生成。")
