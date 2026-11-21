# 用法与真实输出

## 场景一：发布前核对报告

```bash
python scripts/anchor.py check reports/review.md --root .
```

```text
OK           scripts/review.py:157                        文件 1097 行（报告第 42 行）
OK           SKILL.md:133                                 文件 300 行（报告第 43 行）
FILE_MISSING docs/CHANGELOG.md:12                         根目录下没有 docs/CHANGELOG.md（报告第 51 行）

锚点 3 个：OK 2 / 不合格 1
结论不合格：有 1 个锚点解析不了，不能当作证据。
```

## 场景二：只想知道有哪些锚点

```bash
python scripts/anchor.py list reports/review.md --root ./repo
```

逐条打印，不做汇总，退出码不因失效锚点改变——适合在写作过程中随手看。

## 场景三：一次核多份

```bash
python scripts/anchor.py check a.md b.md c.md --root ./repo
```

一次跑完再下结论，避免反复开进程导致结论不一致。

## 接到流水线里

```bash
python scripts/anchor.py check docs/report.md --root . || exit 1
```

退出码 1 会拦住发布；退出码 2 说明参数本身有问题，同样不该继续。

## 一个真实案例

某次评审报告里写着"参数在 `scripts/improve.py:18` 声明了却没实现"。同事按图索骥打开第 18 行，看到的是注释——因为他拿的是改版后的文件，报告写的是改版前的行号。

锚点失效不是笔误，是**文档与代码不同步**的唯一可见症状。跑一次 `check` 就能发现，靠人眼通常发现不了。
