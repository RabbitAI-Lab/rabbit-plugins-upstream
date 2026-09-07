# frontmatter_parsing.md — SKILL.md frontmatter 解析规则（供参考）

实现：`scripts/skill_memory.py::parse_frontmatter`。确定性 YAML 子集，够覆盖技能目录；**不是**完整 YAML 解析器（无锚点/多文档/嵌套结构）。

## 输入预处理
1. 剥离 UTF-8 BOM（`\ufeff`）。
2. CRLF → LF 归一（解析用；写回文件时按原始字节形式保留周边内容）。
3. 首行（strip 后）必须为 `---` 才开启 frontmatter；否则视为无 frontmatter（走回退路径）。
4. 闭合 `---` 必须独占一行；找不到 → 整段视为无 frontmatter。
5. 空文件 → 记入 `skipped[]`（reason=`empty`），**不是错误**。

## 标量形式
| 形式 | 例 | 取值 |
| --- | --- | --- |
| 普通 | `description: text` | strip 后的文本 |
| 单/双引号 | `name: "a, b"` | 剥外层引号（内层引号保留） |
| `>` 折叠 | `description: >\n  l1\n  l2` | 非空行单空格连接；空行保留为 `\n` |
| `\|` 字面 | `description: \|\n  a\n\n  b` | 换行连接，剥离公共缩进，去尾部空行 |
| `>-`/`\|-`/`>+`/`\|+` | 同 `>`/`\|` | chomp 指示符忽略（文档化简化） |

块标量行识别：以空白开头且位于当前键之后；空行属于块；遇到非空、非缩进行结束块。

## 未实现（文档化简化，勿依赖）
- **行内注释不剥离**：`desc: a # b` → 值 `a # b`（完整 YAML 取 `a`）。技能文件约定不写行内注释。
- 嵌套映射/序列（如 `tags: [x]`）：`name`/`description` 后跟非标量内容 → 忽略该字段（取首个标量形式命中）。
- 键匹配：`name` / `description` 精确匹配（行首允许缩进，到首个 `:` 为止；大小写敏感）。

## 回退
- `name` 缺失/空 → **目录名**（SKILL.md 所在目录的 basename）。
- `description` 缺失/空 → 正文**首个 `# ` 标题**（剥 `#`）；再缺 → 空串。
- 解析永不抛异常中断全量扫描：单文件异常进 `skipped[]`（reason=`parse_error`）。
