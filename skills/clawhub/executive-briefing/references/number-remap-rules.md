# 章节编号自动重排规则

## 插入规则

当在第 N 章之后插入新章节时：

```
当前：Part 1, Part 2, Part 3, Part 4
操作：在 Part 1 后插入 → 后续+1

结果：
  Part 1（不变）
  Part 2（新内容）
  Part 3（原 Part 2 → +1）
  Part 4（原 Part 3 → +1）
  Part 5（原 Part 4 → +1）
```

## 子节跟随

```
Part 2 下的 2.1, 2.2, 2.3
→ Part 2 被移到 Part 3
→ 自动变为 3.1, 3.2, 3.3
```

## 算法

1. 解析所有 `## Part N` 和 `### N.M` 模式
2. 从后向前替换（避免位置偏移）
3. 目标章节 > after_n 的全部 +1
4. 子节的 Part 编号同步更新

## 边界情况

| 情况 | 处理 |
|------|------|
| after_n > 最大章节号 | 报错退出 |
| 文件无 Part 章节 | 报错退出 |
| Part 编号已跳号 | `--fix` 模式从1重排 |
| 文件不存在 | 报错退出 |

## 使用

```bash
python3 scripts/renumber.py report.md --after 2
python3 scripts/renumber.py report.md --fix
python3 scripts/renumber.py report.md --after 2 --dry-run
```
