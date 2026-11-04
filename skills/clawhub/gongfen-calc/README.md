# 任务工分计算器 · ClawHub 版

> 丢进来一张格式再乱的任务清单，还你一份逐任务打好评级的 Excel 打分表——字段自动识别、单位自动归一、每个分数可回溯到原表行号；数据不足时如实降级，不编造分数。

这是 [`gongfen-calc`](../) 的 **ClawHub 适配版**。评分算法、参数、口径与通用版**完全一致**（已用同一份真实考核表逐任务比对，16 条任务的工分与自检结果完全相同），差异只在安全边界——为的是消除 ClawHub / SkillSpector 的四类扫描告警。

## ⚠️ 用户警告 / User Warning

**中文**：本技能会**写文件**。它只读取你显式传入的那一个表格文件，并在你指定的输出目录（默认 `gongfen-out/`）生成 `.xlsx` / `.md` / `.json` 三个新文件；**不会修改、移动或删除你的原文件**。它不联网、不上传数据、不读取环境变量、不调用外部命令。数据不足时它会**主动降级**（C/D 分支不输出正式工分），这是设计行为，不是故障。工分是**任务分**，不是个人绩效等级，不得直接用于人员评级、淘汰或扣罚。

**English**: This skill **writes files**. It reads only the single spreadsheet you pass in, and writes three new files (`.xlsx` / `.md` / `.json`) into your output directory (default `gongfen-out/`). It never modifies, moves, or deletes your original file. It makes **no network calls**, uploads no data, reads **no environment variables**, and spawns **no subprocesses**. When data is insufficient it deliberately degrades (no official points in branch C/D) — that is intended behavior, not a failure. Points are **task scores**, not personal performance ratings, and must not be used for individual evaluation, layoffs, or penalties.

## 与通用版的差异

| 扫描类别 | 通用版的问题 | 本版的处理 |
|---|---|---|
| Data Exfiltration | 输出路径无约束，可写到任意目录 | `scripts/sandbox.py`：输出必须落在输入同级目录或当前工作目录内，越界退出码 4 |
| Supply Chain | 文档里带镜像源 `pip install` 命令 | 删除全部外部源与自动安装指引；依赖已 `==` 锁定；脚本不装包、不联网 |
| Output Handling | 报告全文打到 stdout；原表原文未清洗 | stdout 限 60 行；回显文本剥控制字符 + 截断 200 字符；完整内容只落文件 |
| MCP Least Privilege | 未声明能力，权限靠默认 | SKILL.md 增加 5 行**权限声明**表；frontmatter 声明 `allowed-tools` 且**不含通配符** |

## 安装

```bash
# 1. 依赖（由你自己执行，技能不会代装）
pip install -r requirements.txt

# 2. 装到 ClawHub（二选一）
npx clawhub install gongfen-calc            # 从市场安装
npx clawhub publish ./clawhub --slug gongfen-calc --name "任务工分计算器"   # 自己发布
```

手动安装：把整个 `clawhub/` 目录放进宿主技能目录即可（`SKILL.md` 在根）。

## 用法

```bash
python scripts/run.py 任务清单.xlsx
python scripts/run.py 任务清单.xlsx --out-dir out
python scripts/run.py 任务清单.xlsx --override 3=hours --force-points
```

产出三件套：`*.gongfen.xlsx`（主交付物，4 个 sheet）、`*.gongfen.md`（文字版报告）、`*.gongfen.json`（中间结构）。

退出码：`0` 正常/降级｜`1` 分析失败（已出可读报告）｜`2` 参数错误｜`3` 内部异常｜`4` 沙箱拒绝。

### 输出目录规则

允许写入的只有两处（含子目录）：

1. 输入文件所在目录；
2. 当前工作目录。

指定其他位置（如 `--out-dir D:\other` 或 `/tmp/x`）会被拒绝并打印允许范围。**这是故意的**，用来确保技能不会在你的文件系统里到处落文件。

## 权限声明

| 能力类别 | 是否使用 | 说明 |
|---|---|---|
| 网络访问 | ❌ | 无联网调用，不下载依赖，不上报数据 |
| 文件读写 | ✅ | 只读传入的输入文件；只写允许的输出目录；无临时文件残留 |
| 环境变量 | ❌ | 不读取任何环境变量（无需 API key / token） |
| subprocess | ❌ | 不调用外部命令或子进程 |
| 外部 API | ❌ | 无第三方 API、无 MCP 依赖、无遥测 |

## 目录

```
SKILL.md              技能说明（ClawHub 格式，含权限声明）
scripts/
  run.py              唯一入口：参数、沙箱校验、编排
  sandbox.py          输入/输出校验、文本清洗、输出限量（本版新增）
  params.py           全部经验参数
  excel_io.py         读取、编码嗅探、表头定位、合并展开
  field_recognize.py  字段识别、仲裁、单位归一
  quality_stats.py    质检、分档、覆盖度、自检
  score.py            小计、分层、排名、总分
  report.py           Markdown 报告
  excel_out.py        Excel 结果表
references/           口径来源与字段词典
tests/                10 份 fixture + 回归入口
```

## 回归

```bash
python tests/run_regression.py
```

预期：`fixture_noheader.xlsx` 退出码 1（故意失败），其余全部 0，末尾打印"全部符合预期"。

## 限制

- `.xls` 旧格式与加密文件不支持（需 xlrd / msoffcrypto），请先转存 `.xlsx`
- 单文件上限 20 MB
- 多 Sheet 分差 <1.5 会报歧义，需人工指定
- 不回写原表；要合表请用明细里的「原表行号」自行 VLOOKUP

## License

MIT
