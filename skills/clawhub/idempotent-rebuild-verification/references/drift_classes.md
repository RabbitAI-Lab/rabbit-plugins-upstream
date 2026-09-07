# 漂移分类语义（供参考 · 定性）

> 依据：POSIX.1 XCU「Command Substitution」（pubs.opengroup.org，2026-09-06 核对）：
> 命令替换以子命令的标准输出替换，**"removing sequences of one or more newline
> characters at the end of the substitution"**（末尾 1..N 个换行被移除；嵌入的换行保留）。
> heredoc（`cat > f <<'EOF'`）内容恒以单个 `\n` 结尾（引号定界符禁止展开）。
> 用途：本工具 `verify` 命令分类语义的解释。定性参考。

## 分类判定顺序（固定、确定性）

```
1. sha256(file) == want                -> ok                    (status ok)
2. sha256(rstrip \n) == want 或
   sha256(rstrip \n + \n) == want      -> trailing_newline_drift (benign)
3. sha256(file.replace(\r\n,\n)) == want -> crlf_drift          (benign)
4. 前 256B 以 <!doctype html/<html 开头，
   或 文件 <4096B 且含 404/error 标记
   且含 < > 标签上下文（纯文本含 "error" 不算）-> html_error_page (error)
5. want_size 存在且 size < 0.9*want_size -> truncated_paste       (error)
6. want_size 存在且 size == want_size    -> content_change        (error)
7. 其余                                 -> unknown               (warn)
```
无 `--want` 时仅尺寸检查：匹配 → `size_ok`（附带当前哈希供补钉），不符 → `size_mismatch`。

## 字段约定

| 字段 | 含义 |
|---|---|
| `trailing_newlines` | 当前文件尾部连续 `\n` 个数 |
| `normalized_match` | 命中哪种归一化：`strip_all`（全部去 \n 后匹配）/ `single_nl`（补单个 \n 后匹配） |
| `crlf_count` | CRLF 行数（crlf_drift 时） |
| `size_delta` | size − want_size（可为负） |
| `magic` | 前 16 字节 hex（unknown/html 时） |
| `next_action` | 一行处置指令（供 agent 直接执行） |

## 良性漂移的两类根因（都是"谁重写了它"，不是"它坏了"）

1. **`$(cat f)` 往返**：`tool set "$(cat f)"` + `open(f,"w").write(text)`
   —— POSIX 命令替换剥掉全部尾部换行，回写不再补 → 少 1..N 个字节。
   处置：**重跑 writer 步骤**（重写规范形式），勿盲目重贴大块 heredoc。
2. **编辑器 CRLF 往返**：行尾被整体改写。处置：转 LF 或按 CRLF 形式重新钉扎。

## 真损坏的三类

- `truncated_paste`：heredoc 粘贴中断/模型下载截断 —— 删除后整块重贴/重下。
- `html_error_page`：下载失败但 curl 返回 0（404/错误页被写入）—— 检查 URL/认证/字节数断言。
- `content_change`：同尺寸内容被改 —— diff 定位。

## 为什么"重跑 writer"优于"重贴"

重贴大 heredoc 会再次引入截断风险（且 LLM 复述内容本身可能漂移）；
writer 步骤是幂等的重放源，重跑它恢复到钉扎形式是字节级确定的路径。
