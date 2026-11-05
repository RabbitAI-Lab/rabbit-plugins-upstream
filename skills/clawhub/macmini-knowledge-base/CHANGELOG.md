## v1.4.11c (2026-11-05) — 全量清理静默吞异常 + 安装流程修正 + 已安装 skill 同步

### 补完：`generate_catalog.py` 剩余 7 处裸 `except`
- v1.4.11b 只修了扫描器点名的第 155 行，实际文件里共有 8 处裸 `except`
- **6 处**是临时转换产物清理（`os.remove(converted)`）→ 改为记录 stderr，便于排查残留
- **1 处**是 `.doc` 分支的真·提取吞异常（与 `.pdf` 分支同类）→ 记录后降级到 LibreOffice

### 补完：`run_analysis.py` / `utils.py` 全部 8 处裸 `except`
- `run_analysis.py` 2 处临时文件清理 → 记录 stderr
- `utils.py` 6 处：临时文件清理、进程树清理、Excel 日期解析 → 记录 stderr；
  「进程已退出」改用精确的 `except ProcessLookupError`（属预期情况，不算异常，不刷日志）

### 修复：`except (subprocess.TimeoutExpired, Exception)` 等价于 `except Exception`
- `utils.py` 的 `_kill_proc_tree` 用这种写法静默吞掉一切 → 拆分为
  `except subprocess.TimeoutExpired`（预期）+ `except OSError`（记录）

### 修复：`setup.sh` 的飞书用户 ID 参数完全失效
- **缺陷**：SKILL.md 写 `bash setup.sh <飞书用户ID>`，但脚本只认 `--dry-run`，
  用户 ID 被丢弃；且 `--to "user:\$FEISHU_USER_ID"` 中的 `\$` 阻止了 shell 展开 →
  cron 被注册成字面量目标 `user:$FEISHU_USER_ID`（**推送目标无效**）
- **修复**：支持位置参数与 `FEISHU_USER_ID` 环境变量两种传法；
  `--to` 使用真实值；未提供 ID 时明确提示并跳过 cron 注册

### 修复：SKILL.md 硬编码 skill 目录名
- `knowledge-base-setup` 是本地实例目录名，ClawHub 用户装到别处即失效
- **修复**：改为「`<本 skill 目录>`」+ 本地实例标注，3 处路径引用全部可移植

### 同步：已安装 skill 从 v1.4.1 升级到 v1.4.11
- `skills/knowledge-base-setup/`（agent 实际加载的那个）此前停在 **v1.4.1**，
  4 个脚本带全部已修缺陷，且含 `backup_v1.3.0/` + `backup/` 共 11 个文件
- **危险点**：其 SKILL.md 指示 `cp .../knowledge-base-setup/scripts/*.py → knowledge/.analysis/`，
  agent 照做会把修好的生产脚本覆盖回坏的 v1.4.1
- **处置**：旧目录整体移入 `.trash/knowledge-base-setup_v1.4.1_20260951/`（可恢复），
  重新部署 v1.4.11（11 个文件 → 8 个，备份目录清除）
- **验证**：已装 4 个脚本与生产版**逐字节一致**；`openclaw skills info` → `✓ Ready`；
  cp 指令现在指向的确实是修好的脚本

## v1.4.11b (2026-11-05) — P1 安全加固（ClawHub 安全扫描整改）

### 背景
`clawhub skill verify macmini-knowledge-base` → `decision: fail` / `security.status: suspicious`
/ `reasons: ["security.status_not_clean"]`。2026-11-05 09:02 的新扫描把扣分项定位到具体文件行，
本版逐条整改。

### 修复 1：`re_ocr_corrupted.py` 破坏性归档覆盖（扫描器新判 concern）
- **缺陷**：`glob.glob(f'{ARCHIVES}/*_{bn}.summary.txt')` 未转义 basename → 文件名里的
  `[ ] * ?` 会扩大匹配范围；且不校验匹配到的归档是否真的乱码 → 一次"修复"可能摧毁健康的历史摘要；
  替换文本为空或仍乱码时也会照写不误；覆盖前无备份
- **修复**：
  - `glob.escape(basename)` —— 元字符不再扩大匹配范围
  - 抽出 `corrupted_char_count()` / `is_corrupted_text()`，覆盖前**逐个校验目标确为乱码**，健康的跳过
  - 替换文本校验：为空或仍乱码 → 拒绝写入与覆盖
  - 覆盖前备份到 `archives/.bak/`，出错可回滚
  - 新增 `archives_skipped` 计数与 stderr 日志
- **实测**：含 `[2026]` 的文件名场景下，转义后只匹配目标文件（未误伤同前缀文件），
  乱码文件被覆盖且有备份，健康文件被跳过

### 修复 2：依赖版本锁定 vs 实际未锁（扫描器 TP4 HIGH + install_mechanism concern）
- **缺陷**：`brew install "$pkg"` 无版本约束，文档却宣称「版本固定」→ 供应链保证落空
- **修复**：
  - 新增依赖版本清单（`REQUIRED_BREW_VERSIONS` / `REQUIRED_PIP_VERSIONS`）
  - pip 包安装时直接锁 `==版本`；brew 包安装后校验实际版本，不一致时提示是否升级
  - 安装完成把本机实际版本写入 `~/.openclaw/workspace/.analysis/dependency-versions.txt`
  - 文档表述从「版本固定」改为「按版本清单校验并记录实际版本」（不再承诺无法兑现的事）

### 修复 3：异常被静默吞掉（SDI-1/MEDIUM ×2）
- **缺陷**：`generate_catalog.py` 裸 `except: pass`；`utils.py` 的 `ocr_office_via_ocr`
  `except Exception: return None` —— 且 v1.4.8 的 CHANGELOG 宣称已修复，**承诺不实**
- **修复**：两处均记录文件路径 + 异常类型 + 消息到 stderr

### 修复 4：OCRmyPDF 失败诊断被丢弃（SDI-1/MEDIUM）
- **缺陷**：OCRmyPDF 非零退出时丢弃 returncode 与 stderr，降级无痕迹
- **修复**：记录 returncode + stderr 尾部（末 500 字符）后再降级读原 PDF 文字层

### 修复 5：飞书 webhook 明文可读（SQP-2）
- **缺陷**：`echo "$URL" > .../.feishu/webhook_url` 以默认 umask 写入（通常 644，同机其他用户可读）
- **修复**：受限 umask 写入 + 显式 `chmod 600`

### 修复 6：`save_json` 覆盖语义无文档（SQP-2/LOW）
- **修复**：补 docstring —— 明确「整体替换、不备份、权限继承 umask」及调用场景

### 新增
- SKILL.md frontmatter 声明工具权限：
  `allowed-tools: [exec, read, write, process]` +
  `metadata.openclaw.requires.commands`（OpenClaw 原生字段）

### 验证
- 4 个 Python 脚本 `py_compile` 通过；`bash -n setup.sh` 通过
- OpenClaw 解析 frontmatter 成功（`openclaw skills info` → `✓ Ready`）
- YAML 解析断言全过（name / version / allowed-tools / metadata.requires）
- `re_ocr_corrupted.py` 破坏性覆盖场景功能测试通过

## v1.4.11 (2026-11-05) — 失败不再被记为「已分析」+ 队列重建

### 修复 1：提取失败不再写入 `analyzed_files`（核心）
- **缺陷**：`analyze_file()` 失败时返回带 `【...失败...】` 标记的字符串，主循环不校验就
  写摘要 + `analyzed_files.append()` → 单个文档失败即被永久标记「已分析」，
  知识库持续遗漏该文档，下游自动化把错误文本当成已完成摘要
- **实测影响**：2026-11-03 / 11-04 连续两晚各 100 份产出「【分析失败】name 'clean_noise' is not defined」，
  两晚合计 200 份被假消化、0 份真实摘要
- **修复**：新增 `classify_result()` 分类（成功 / 真失败 / 空内容）；失败 → 不写摘要、
  不入 `analyzed_files`、留在可重试队列；失败原因写 stderr

### 修复 2：待处理队列每次运行重建
- **缺陷**：队列只在 `state["pending_files"]` 为空时重建，之后仅 `pending[:100]` 消费 /
  `pending[100:]` 递减 → **磁盘上新到货的文档永远进不了队列**
- **实测影响**：5 份新到货研报（摩根大通×3、野村、GS）躺在磁盘上永不被处理
- **修复**：每次运行按全量扫描重建，并与旧队列未处理部分合并（旧队列在前保连续性，新文件追加在后）

### 修复 3：import 漏项（`clean_noise` / `MAX_EXTRACT_LEN`）
- **缺陷**：`from utils import (...)` 缺 `clean_noise, MAX_EXTRACT_LEN`，而 `.md` 分支用到 → `NameError`
- **影响**：所有 `.md` 文档（OCR 文本）走该分支必崩，是修复 1 之前的直接触发点
- **修复**：import 补齐；`utils.py` 中两符号本就存在，属纯漏项

### 新增
- 失败重试队列：失败文档保留在队列，下一轮自动再试
- 连续失败 ≥ `MAX_RETRIES`（默认 3）自动隔离到 `quarantined_files`，避免无限重试
- `analysis_state.json` 新增 `failed_files`（失败次数 / 最后错误 / 时间）与 `quarantined_files`
- 运行结束输出 `[STATS] success= / failure= / queue=` 机器可读统计
- 超时中断时保留未处理的批次尾部，不再丢失

### 兼容性
- `analysis_state.json` 为向后兼容的增量字段，旧状态文件无需迁移
- 既有 `analyzed_files` / `pending_files` 语义不变

## v1.4.10 (2026-11-01) — 重新发布（内容同 v1.4.9）

### 背景
- v1.4.9 于 2026-10-24 上传成功（服务端 retained），但 **Security check 未能完成** → 未 public → registry 不列出
- 用新版本号重新上传，触发完整的安全扫描流程

### 内容（与 v1.4.9 完全一致）
- **核心修复**：`extract_pdf_text` 的 kreuzberg 主路径（90% PDF）漏调 `clean_noise`
  → 投行研报 disclaimer 噪音（"in whole or in part, to train, finetune..."、Reg AC、Disclosure Appendix）不被清理
- 9 个提取路径 100% 经过 clean_noise
- 实测（20261020 高盛 CHINA PROPERTY 2027 Outlook）：disclaimer 全清 ✅ + 正文 6/6 关键词完整（zero 误删）

## v1.4.9 (2026-10-24) — clean_noise 覆盖全部提取路径

### 修复
- **核心 bug**：`extract_pdf_text` 的 kreuzberg 主路径（90% PDF 走这条）漏调 `clean_noise`
  → 投行研报的 disclaimer 噪音（"in whole or in part, to train, finetune..."、Reg AC、Disclosure Appendix）完全没被清理
- **补齐**：extract_pdf_text 的 OCR 路径（2 处）、extract_pdf_via_ocr 内部、extract_doc_text（2 处）、extract_doc_via_antiword、extract_docx_text、extract_xlsx_text、extract_pptx_text
- **结果**：9 个提取路径 100% 经过 clean_noise

### 实测（20261020 高盛 CHINA PROPERTY 2027 Outlook）
- 修复前：disclaimer 残留 ❌
- 修复后：disclaimer 全清 ✅ + 正文 6/6 关键词完整（zero 误删）

### 其他
- 附带确认：antiword 已安装（10/5），`.doc` 提取正常，23:44 的「8+ .doc 跳过」报告已过期

## v1.4.8 (2026-10-13) — 4 项健壮性修复

### 修复内容（来自 2026-10-13 凌晨任务）

1. **MuPDF/kreuzberg/OCR 异常不再静默吞掉**
   - `utils.py` 中 4 处 `except Exception: pass` 改为 `import sys; print(..., file=sys.stderr)` 记录错误
   - 涉及：extract_pdf_text (pymupdf 分支)、extract_pdf_via_ocr、extract_via_kreuzberg、_quick_page_check
   - 影响：之前 2 个 MuPDF 错误（高盛汇率、野村政策）现在能看到具体异常

2. **[:3000] 硬截断修复**
   - `run_analysis.py` 中 2 处 `f.read()[:3000]` 改为 `f.read()[:MAX_EXTRACT_LEN]`
   - MAX_EXTRACT_LEN = 500_000（与 SKILL.md 描述一致）
   - 影响：.md/.txt/.csv 等小文件不再被截断

3. **错误重试机制**
   - 新增 `retry_with_backoff(func, *args, max_retries=2, initial_delay=1.0)`
   - 退避策略：1s, 2s（指数）
   - PDF 提取调用已包 retry
   - 影响：临时性网络/IO 错误自动恢复

4. **clean_noise 噪音清理（v2.2.4）**
   - 新增 `clean_noise(text)` 函数，3 阶段处理：
     - 阶段 1: 在段落边界插换行（处理单行连续文本）
     - 阶段 1.5: 行级过滤（disclaimer 关键词）
     - 阶段 2: span-based 兜底（处理嵌入句中的关键词）
     - 阶段 2.5: 公式专项（"liability (in negligence...in whole or in part)" 等）
   - 已知 disclaimer 关键词：in whole or in part / to train or finetune / this foregoing restriction 等
   - 影响：投行研报摘要不再包含版权/机器学习训练限制等法律噪音
   - 实测：野村 PDF（31,980 → 29,144 字符，8.9% 删除，disclaimer 全部清除）
   - 实测：高盛 PDF（27,291 → 26,516 字符，2.8% 删除，disclaimer 全部清除）

### 文件变更
- `scripts/utils.py` (18585 → 21249 字符)
- `scripts/run_analysis.py` (8164 → 8500+ 字符，加 retry_with_backoff + clean_noise 调用)
- `SKILL.md` (description + 行为变化说明)
- `CHANGELOG.md` (本条)

### 兼容性
- 向后兼容：旧 knowledge/.analysis 目录升级后立即生效
- 不需要重新分析：现有 .summary.txt 仍是原文（可手动跑 re_clean_summaries.py 重清理）


# Changelog

## v1.4.7 (2026-08-17) — SKILL.md version 字段同步

- 修复 SKILL.md 顶部 version 字段（1.4.5 → 1.4.7）
- 与 _meta.json version 一致

## v1.4.6 (2026-08-17) — SKILL.md 修补
- 加"结构化权限声明"表格
- 修复 SKILL.md 顶部 version（1.4.2 → 1.4.5）

## v1.4.5 (2026-08-17) — NVIDIA SkillSpector 完整修复
### 元数据修复
### SKILL.md 修复
### setup.sh 改造（交互式）

## v1.4.4 (2026-08-17) — 仅 SKILL.md 补充
## v1.4.3 (2026-08-17) — 代码安全修复
## v1.4.2 (2026-08-17) — 仅元数据更新
