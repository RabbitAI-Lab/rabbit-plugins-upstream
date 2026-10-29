# Markdown 历史记录导入

用于把已经按成员整理好的旧 Markdown 记录导入到 v2 成员时间轴。导入模块只沉淀历史证据，不自动修改 `profile.md` 或 `distill.md`。

导入前必须已经完成主库锁定：已有 `data/` 运行 `python3 scripts/adopt-data.py`，没有数据运行 `bash scripts/init.sh`。没有 `.team-memory-root.json` 时脚本会停止，避免写到错误目录。

## 输入目录

推荐把旧记录放到：

```text
data/import/incoming/
└── member-001/
    ├── 2023年度沟通.md
    └── 2024旧记录.md
```

目录名也可以使用成员姓名或 alias，但优先使用 `member-XXX`，避免重名。

每条重要记录应有明确日期，支持：

- `2024-01-15`
- `2024/01/15`
- `2024.01.15`
- `2024年1月15日`

日期最好放在标题或段落开头，例如：

```markdown
### 2023-12-20 年度沟通

我的期待：
- 希望他能更主动暴露风险。

发现的问题：
- 项目后段容易自己扛，较少提前同步。

对他说的话：
- 你已经有足够的能力 owner 一个模块，但需要让团队更早看到风险。
```

## 操作流程

先预览：

```bash
bash scripts/import-member-markdown.sh
```

查看 `data/import/reports/` 下生成的报告，确认：

- 成员匹配正确。
- 将写入的事件 ID 正确。
- 没有无法匹配成员的文件。
- 没有完全无法识别日期的文件。
- 疑似重复记录符合预期。

确认后写入：

```bash
bash scripts/import-member-markdown.sh --apply
```

也可以指定输入目录或成员：

```bash
bash scripts/import-member-markdown.sh --input-dir data/import/incoming --apply
bash scripts/import-member-markdown.sh --member member-001 --apply
```

## 写入规则

- 新事件 ID 形如 `OBS-YYYYMMDD-IMPORT-001`。
- 事件写入对应成员 `timeline.md` 的“时间轴（从新到旧）”。
- 事件只写入 `.team-memory-root.json` 锁定的主库。
- 旧内容不会被覆盖、删除或重写。
- 每条导入记录保留来源文件、行号、导入时间和原始记录。
- 脚本会写入隐藏导入指纹，重复执行会跳过已导入记录。
- `--apply` 会先备份被修改的 `timeline.md` 到 `data/.backup/import-YYYYMMDD-HHMMSS/`。

## 画像类信息

MBTI、年度期待、管理判断、发现的问题、对组员说的话，都作为带日期来源的历史证据进入 `timeline.md`。

导入完成后，如果需要刷新人物卡，推荐再让智能体执行：

```text
请基于 member-001 的 profile.md、timeline.md 和 distill.md，生成一份“当前人物卡更新建议”。
要求区分事实、推断和建议；引用日期和事件 ID；不要直接改文件，先给我确认。
```

确认后再更新 `profile.md` 或 `distill.md`，避免把旧判断直接固化成当前状态。

如果导入内容里包含承诺或跟进动作，导入后运行：

```bash
python3 scripts/sync-tasks.py
```

它会把未完成追踪项同步到 `data/tasks/tasks.md`，不改写原始导入记录。
