# Team Memory 升级与兼容说明

当前产品版本：`v2.6.0`  
当前数据结构版本：`schema-version: "2.2"`

发布包可以是 lean runtime 包，也可以自带 `data/`。无论哪种方式，Markdown 文件树都是唯一可信源；JSONL/SQLite 只作为可重建机器索引。

## 升级原则

- 不覆盖 `skill-config.yaml`
- 不覆盖已锁定主库
- 不自动迁移
- 不自动合并多套数据
- 迁移脚本默认 dry-run
- `--apply` 也只复制，不删除，不覆盖
- 新功能需要新目录或默认文件时，由 `init.sh` 在缺失时创建
- 已有 `data/` 时先运行 `scripts/adopt-data.py`，写入 `.team-memory-root.json`

## 主库接管

如果升级包自带已录入数据：

```bash
python3 scripts/adopt-data.py
```

脚本会：

- 把当前 `data/` 固定为主库
- 写入 `.team-memory-root.json`
- 同步 `skill-config.yaml` 的 `settings.data-path`
- 重建 `data/.index/events.jsonl`、`tasks.jsonl` 和 `data/.index/team-memory.sqlite`
- 不移动、不重写、不删除历史 Markdown

如果目标环境已有另一套数据，脚本会停止并生成检查报告。先运行：

```bash
python3 scripts/doctor.py
```

确认主库后再处理，不要让智能体自动合并。

## 智能待办升级

升级到 v2.6.0 后，已有时间轴里的追踪项不会被改写。运行：

```bash
python3 scripts/sync-tasks.py
```

脚本会把未完成的 `追踪项` 和 `我的承诺` 抽取到 `data/tasks/tasks.md`，并自动合并同来源行或正文完全一致的重复待办。原始 `timeline.md` 不会被删除或重写。

当前版本的待办台账支持 `对象类型` 和 `对象` 字段，成员待办与相关方待办可共存。旧的 `成员` 字段仍可读取；重新运行 `scripts/sync-tasks.py` 后，新生成待办会使用对象字段。同一事件下多个不同追踪项不会再因为来源事件相同或文本相似而误合并。

生成每周或月度复盘：

```bash
python3 scripts/review-tasks.py --weekly
python3 scripts/review-tasks.py --monthly
```

## v1 兼容

v2.6.0 同时支持读取：

```text
data/members/member-001/profile.md
data/members/member-001/timeline.md
data/members/member-001/distill.md
```

以及 v1 旧文件：

```text
data/members/张三-档案.md
data/members/张三-时间轴.md
data/members/张三-蒸馏.md
```

如果 v1 和 v2 同时存在，默认优先使用 v2，把 v1 当作只读历史来源。

## 升级前备份

推荐先导出完整数据包：

```bash
python3 scripts/export-data.py
```

迁移脚本在 `--apply` 时也会自动创建：

```text
data/.backup/YYYYMMDD-HHMMSS/
```

## 预览迁移

```bash
python3 scripts/doctor.py
bash scripts/migrate-v1-to-v2.sh
```

预览会显示：

- 将识别哪些成员
- 将复制哪些 v1 文件
- 将创建哪些 v2 目标文件
- 是否存在别名冲突、配置缺失或目标文件已存在

## 执行迁移

确认预览无误后执行：

```bash
bash scripts/migrate-v1-to-v2.sh --apply
```

脚本行为：

- 创建 `data/.backup/{timestamp}/`
- 把旧文件备份进去
- 把旧文件复制到 v2 目录
- 保留所有 v1 原文件
- 遇到目标文件已存在时停止，不覆盖

## 回滚方式

因为迁移不会删除旧文件，最简单的回滚方式是继续使用 v1 文件。

如果想移除已生成的 v2 文件，请先确认备份存在，再手动删除对应 `data/members/member-XXX/` 目录。不要删除 `data/.backup/`。

## 常见升级问题

### 脚本提示缺少主库锁定文件

说明还没有确认唯一主库。已有 `data/` 时运行 `python3 scripts/adopt-data.py`；没有数据时运行 `bash scripts/init.sh`。

### 脚本提示 settings.data-path 冲突

说明 `skill-config.yaml` 指向的目录和 `.team-memory-root.json` 不一致。先运行 `python3 scripts/doctor.py`，确认主库后再接管。

### 迁移脚本提示别名冲突

说明 `skill-config.yaml` 中有两个成员使用同一个 `alias` 或 `shortcuts`。请先改成唯一别名，再重新运行 dry-run。

### 迁移脚本提示目标文件已存在

说明该成员已经有 v2 文件。脚本不会覆盖。请手动比较内容后决定是否保留、重命名或归档。

### 没有找到某个成员的旧文件

脚本会跳过缺失文件。例如只有 `张三-时间轴.md` 时，只迁移时间轴，不伪造档案或蒸馏文件。

## v2.6.0 变更摘要

- 新增 `data/tasks/tasks.md` 待办台账和 `data/tasks/reviews/` 复盘报告
- 新增 `scripts/sync-tasks.py` 自动抽取并合并追踪项
- 新增 `scripts/review-tasks.py` 每周/月度待办复盘
- 新增 `scripts/resolve-task.py` 处理结果草案和确认写入
- `rebuild-index.py` 新增 `tasks.jsonl` 和 SQLite `tasks` 表
- `rebuild-index.py` 使用 `event_key = source_file:event_id` 作为 SQLite 事件主键，避免不同文件中的同名事件 ID 互相覆盖；同一文件内重复事件 ID 会阻止重建
- `sync-tasks.py` 支持扫描相关方“后续动作”，并按 `member` / `stakeholder` 对象生成待办；相似但不完全一致的事项只在报告中提示
- `doctor.py` 增加事件总数/唯一 ID 数、同文件重复事件 ID、跨文件重复事件 ID、相关方必填字段、关联事件和待办来源一致性检查
- 新增 `.team-memory-root.json` 主库锁定
- 新增 `scripts/adopt-data.py` 接管已有 `data/`
- 新增 `scripts/doctor.py` 检查多套数据和路径冲突
- 新增 `scripts/rebuild-index.py` 生成 JSONL/SQLite 机器索引
- 新增 `scripts/export-data.py` 导出 Markdown、JSONL、SQLite、manifest 和校验清单
- 新增成员独立目录结构：`data/members/member-XXX/profile.md`、`timeline.md`、`distill.md`
- 新增 v1 到 v2 的只复制迁移脚本
- `SKILL.md` 改为明确主库锁定和防误写规则
- 发布包可保持 lean，也可随 `data/` 一起迁移后接管
- 中文文件名仍可读，但默认写入路径使用 `member-XXX`
