# 语雀 CLI 命令速查

脚本路径：`scripts/yuque_cli.py`（运行它；除非调试，不要直接阅读源码）

全局 flag（所有命令均可用）：`--json`（机器可读输出）、`--dry-run`（预览，不实际执行；dry-run 模式始终输出 JSON）。

---

## 配置

### setup
初始化凭据，解析知识库 URL，验证连接，写入 `.env`，检查 `.gitignore`。

```bash
python scripts/yuque_cli.py setup --url "<知识库URL>" --token "<token>"
```

- `--url`：语雀知识库地址，格式 `https://xxx.yuque.com/group/book`
- `--token`：语雀 API Token。**token 必须在与知识库相同的域名下创建**，有两种来源：
  - 个人版（知识库在 `www.yuque.com` 下）：https://www.yuque.com/settings/tokens
  - 空间/团队版（知识库在子域名下）：个人 token 页 `https://<子域名>.yuque.com/settings/tokens`，团队级 token 页 `https://<子域名>.yuque.com/<group>/settings/tokens`（示例：`https://qianxiaoxia.yuque.com/tn85tw/settings/tokens`）。用 `www.yuque.com` 的个人 token 访问空间知识库会返回 401。
- `--force`：覆盖已有 `.env`
- `--env-path`：指定 `.env` 文件路径（默认项目根目录）

成功后写入 `.env`，包含 `YUQUE_TOKEN` 和 `YUQUE_REPO`。

---

## 文档操作

### list
列出知识库所有文档（ID、标题、slug、更新时间）。

```bash
python scripts/yuque_cli.py list
```

- `--offset`：分页起始位置
- `--limit`：每页数量

### get
获取单篇文档详情（标题、正文、slug、格式）。

```bash
python scripts/yuque_cli.py get <id_or_slug>
```

参数可以是整数文档 ID 或字符串 slug，两者均可。

### create
创建新文档，默认自动追加到目录（TOC）。

```bash
python scripts/yuque_cli.py create -t "标题" -b "正文 markdown"
# 或从文件读取正文
python scripts/yuque_cli.py create -t "标题" -f path/to/file.md
```

- `-t` / `--title`：文档标题（必填）
- `-b` / `--body`：正文内容（含 shell 特殊字符时改用 `-f`）
- `-f` / `--body-file`：从本地文件读取正文（推荐用于非 ASCII 内容）
- `--slug`：指定 slug（默认由语雀自动生成）
- `--no-toc`：不追加到目录（创建隐藏文档时使用）
- `--format`：`markdown`（默认）或 `lake`

> **注意：创建文档不会自动加入 TOC，脚本默认通过 `append_doc_to_toc` 处理。使用 `--no-toc` 可跳过。**

### update
更新已有文档（标题、正文或两者）。

```bash
python scripts/yuque_cli.py update <id_or_slug> -t "新标题" -f updated.md
```

- 至少提供 `-t`、`-b`、`-f`、`--slug`、`--format`、`--public` 其中一个，否则脚本拒绝执行
- `-f` / `--body-file`：从文件读取正文

### delete
删除文档。**`--confirm` 为必填**，脚本不接受未确认的删除。

```bash
python scripts/yuque_cli.py delete <id_or_slug> --confirm
```

删除前先 `get` 确认目标文档，stderr 会打印文档标题。

### toc
查看知识库目录结构（层级展示）。

```bash
python scripts/yuque_cli.py toc
```

> **注意：TOC 追加始终插入知识库根节点，无法通过此 Skill 指定父节点或插入位置。如需自定义结构，用户需在语雀 Web 编辑器中手动调整。**

---

## 同步与状态

### sync
智能增量同步：只推送真正改动的文档，跳过未修改内容。

```bash
python scripts/yuque_cli.py sync
```

- `--check`：只检查差异，不推送（等同 dry-run）
- `--root`：指定本地根目录（默认 cwd）
- `--layout`：强制指定布局 `flat|nested|frontmatter`（首次 sync 会自动检测）
- `--on-missing`：处理本地缺失文件的策略（见下方）
- `--force-title`：强制用文件名（不含扩展名）作为文档标题，忽略 H1 和 frontmatter `title`

**状态文件：** `.yuque-sync.json`（自动加入 `.gitignore`），记录每篇文档的本地内容 SHA-256 哈希和远端 `latest_version_id`。

**布局检测（首次自动识别）：**

| 布局 | 描述 | slug 来源 |
|------|------|---------|
| `flat` | 所有 `.md` 在根目录 | 文件名（不含扩展名） |
| `nested` | `.md` 在子目录下 | 文件名（子目录仅作组织用） |
| `frontmatter` | 每个文件顶部有 `--- slug: xxx ---`（可选 `title` 字段） | 前言中的 slug 值 |
| `empty` | 无 `.md` 文件 | — 建议先 `pull --all` 拉取远端 |

布局混合或部分含前言时脚本报错，需手动传 `--layout` 或规范化目录。

**标题提取优先级链：** frontmatter `title` → 正文首个 `# ` H1 → 文件名（不含扩展名）。回退到文件名的文档会在 `sync --check` / `status` 输出的 **"Title fallback"** 分类中列出，提示补充 H1 或 frontmatter `title`。`sync` 更新文档时会同步标题——仅修改标题（不改正文）也会触发 update 推送。

**本地文件缺失时（exit code 2）：**

`sync` 以退出码 2 停止，打印确认块，需用户选择处理方式后再以 `--on-missing` 重新运行：

```bash
sync --on-missing delete   # 同步删除语雀远端文档
sync --on-missing pull     # 从语雀恢复到本地
sync --on-missing forget   # 保留远端，仅从状态文件移除
```

退出码 2 **不是错误**，是等待确认。收到时把打印块翻译成用户语言展示，收到选择后再重新运行。**不得替用户选择 `delete`。**

**冲突处理：** 本地和远端均有变动时，`sync` 列出冲突并跳过。手动解决：
- `pull --slug <slug> --overwrite` — 以远端版本覆盖本地
- `update <slug> -f file.md` — 以本地版本覆盖远端

**注意：** `sync` 忽略远端草稿（`body_draft`）。变更检测基于 `latest_version_id`（已发布版本）。如怀疑有未发布草稿，先 `pull --slug <slug>` 查看。

### pull
将远端文档下载到本地 Markdown 文件。

```bash
python scripts/yuque_cli.py pull --slug <slug>
# 拉取全部文档
python scripts/yuque_cli.py pull --all
```

- `--slug`：拉取指定文档
- `--all`：拉取知识库所有文档
- `--overwrite`：覆盖本地已有文件
- `--root`：指定保存目录
- `--layout`：指定布局（影响保存路径）

### status
只读展示本地与语雀的差异，不做任何写操作。

```bash
python scripts/yuque_cli.py status
```

- `--root`：指定本地根目录
- `--layout`：指定布局

---

## 高频陷阱

1. **正文含 shell 特殊字符**：用 `--body-file` 代替 `--body`，避免 shell 引号问题。
2. **`id` 参数**：`get`/`update`/`delete` 的参数可以是整数 ID 或字符串 slug，两者均可。
3. **语雀 Lake 格式是私有格式**：始终用 `--format markdown`（默认值），除非用户明确需要 Lake 格式。
4. **远端文档变更检测基于已发布版本**：`sync` 不感知草稿状态。
5. **不得猜测 doc ID 或 slug**：未知时先 `list`、`toc` 或 `status` 定位目标。
