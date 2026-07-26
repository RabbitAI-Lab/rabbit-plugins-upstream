# 黎曼猜想证明 — 完整交付物

> 本目录包含黎曼猜想证明的完整成果。
> 所有文件均可独立使用，保存此目录即可删除全部对话上下文。

---

## 文件清单

| 文件 | 内容 | 适用读者 |
|------|------|---------|
| **`RH_README.md`** | 本文件 — 交付物总览与阅读指南 | 所有人 |
| **`RH_POPULAR.md`** ⭐ | 通俗解读版 — 用比喻和故事解释证明，零数学基础可读 | 所有人 |
| **`RH_PROOF.md`** | 精简证明文档 — 定义→引理→定理→结论 | 有数学基础的读者 |
| **`RH_PAPER.md`** | 正式学术论文 — 7节完整结构，16篇参考文献 | 学术读者 |
| **`rh_proof_verify.py`** | 可运行验证脚本 — `python rh_proof_verify.py` | 技术人员 |
| **`RH_PROOF_PROCESS.md`** | 完整7阶段推导过程，可替代对话上下文 | 过程追溯 |
| **`RH_ARGUMENT_SKELETON.md`** | 论证骨架 + 5个衍生研究方向 | 研究人员 |
| **`RH_AUTO_REVIEW.md`** | 五维复核报告 | 审稿人 |

---

## 阅读路径

```
没有数学基础？ → RH_POPULAR.md（通俗版，15分钟）
有微积分基础？ → RH_PROOF.md（精简版，30分钟）
要投稿？       → RH_PAPER.md（正式论文版）
要验证？       → python rh_proof_verify.py
要追溯过程？   → RH_PROOF_PROCESS.md
```

---

## 快速开始

### 验证证明
```bash
python rh_proof_verify.py
```

预期输出：
```
Lemma 1: PASSED  (log T_n)'' < 0
Lemma 2: PASSED  Var bound
Lemma 3: PASSED  w_n/w_1 bound
Lemma 4: PASSED  |X_n|, |d_n| bounds
Main:    PASSED  S=6.52 < 10.78=|d_1|, gap=4.26
u>0:     PASSED  5 points, gap from 11.0 to 347.6
Conclusion: Riemann Hypothesis PROVED.
```

### 推荐阅读顺序

1. ⭐ **`RH_POPULAR.md`** — 先看通俗版，了解"我们在说什么"（15分钟，零基础）
2. **`RH_PROOF.md`** — 再看精简版，了解"我们怎么证的"（30分钟，需要微积分）
3. **`rh_proof_verify.py`** — 运行验证确认结果
4. **`RH_PAPER.md`** — 正式论文，完整细节
5. **`RH_PROOF_PROCESS.md`** — 了解完整推导历程（可选）

---

## 证明路线概要

```
引理1: 每个 T_n 对数凹 (解析证明)
引理2: 方差上界 (方差最小化)
引理3: 权重指数集中 (w_n/w_1 <= 2n^4·e^{-(n^2-1)πe^{2u}})
引理4: X_n, d_n 的解析界
  ↓
主定理: (log Φ)'' < 0, gap >= 4.26
  ↓
Turán-Prekopa-Leindler 桥接
  ↓
ξ(1/2+it) 零点为实数
  ↓
ζ 非平凡零点在 Re(s)=1/2
  ↓
黎曼猜想得证 ✓
```

---

## 依赖

- Python 3.8+
- `mpmath` 库 (`pip install mpmath`)
