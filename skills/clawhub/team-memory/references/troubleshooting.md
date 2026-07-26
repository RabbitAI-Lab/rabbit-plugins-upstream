# 故障排除

## 主库路径不确定

任何写入前都应能看到 `.team-memory-root.json`。如果没有，先停止：

```bash
python3 scripts/doctor.py
```

已有 `data/` 时运行：

```bash
python3 scripts/adopt-data.py
```

没有数据时运行：

```bash
bash scripts/init.sh
```

如果报告发现多套数据，不要自动合并或删除；先人工确认哪一套是主库。

## 记录无法匹配成员

检查 `skill-config.yaml`：

- `members[].name` 是否与输入姓名一致
- `members[].alias` 是否唯一
- `shortcuts` 是否指向真实存在的 `member-XXX`

如果同一个别名指向多个成员，先修改配置再记录，不要让 AI 猜。

## 迁移脚本提示别名冲突

示例：

```text
ERROR: 配置校验失败
- 成员名称/别名冲突: ZS 同时指向 member-001 和 member-008
```

解决方式：给其中一个成员换唯一别名，并同步更新 `shortcuts`。

## 生成报告缺少数据

常见原因：

- `distill.md` 没有及时更新
- `timeline.md` 记录太少或事件描述过短
- 旧 v1 文件还没有迁移，且查询时没有读取 v1 兼容路径

解决方式：

1. 先查看 `data/members/{member-id}/distill.md`
2. 再查看 `data/members/{member-id}/timeline.md`
3. 如果还没迁移，检查 `data/members/{姓名}-时间轴.md`

## 迁移脚本提示目标文件已存在

脚本不会覆盖已有 v2 文件。请手动比较：

```text
data/members/member-001/timeline.md
data/members/张三-时间轴.md
```

确认后再决定是否归档旧文件或手工合并。

## 文件名或压缩包乱码

v2 的默认路径使用英文和 `member-XXX`，压缩包内部必须使用 `/` 路径分隔符。

推荐：

```text
data/members/member-001/timeline.md
references/record-templates.md
```

不推荐作为默认路径：

```text
data\members\张三-时间轴.md
```

## 隐私顾虑

- 真实姓名只放在 `skill-config.yaml` 和正文必要位置。
- 不要把 `data/` 上传到公共仓库。
- 网盘同步前检查加密和共享权限。
- 离职成员优先归档到 `data/archive/`。

## 搜索历史记录

```bash
rg "张三|member-001|OBS-2024" data/members
```

如果没有安装 `rg`，可用：

```bash
grep -R "张三" data/members
```

## 重建机器索引

如果 JSONL 或 SQLite 缺失、过旧或被误删，直接重建：

```bash
python3 scripts/rebuild-index.py
```

Markdown 是可信源，`data/.index/` 下文件都可以重建。
如果 SQLite 里少了同名事件，升级后重新运行 `rebuild-index.py`。新版索引用 `event_key = source_file:event_id` 做机器唯一键，允许不同文件中存在相同的人类可读事件 ID。

## 待办沉默或重复

先同步追踪项：

```bash
python3 scripts/sync-tasks.py
```

再生成每周扫描：

```bash
python3 scripts/review-tasks.py --weekly
```

如果发现重复待办，不要手工删除原始 `timeline.md`。先看同步报告里的“相似但未自动合并”；脚本只会自动合并同来源行或正文完全一致的事项，避免误吞不同追踪项。确认处理结果后用：

```bash
python3 scripts/resolve-task.py TASK-YYYYMMDD-001 --status done --note "处理结果" --apply
```

`resolve-task.py` 默认只生成草案，只有 `--apply` 才写入。

如果相关方记录里的“后续动作”没有进入待办，先确认已升级到支持对象待办的版本，再运行 `python3 scripts/sync-tasks.py`。脚本支持 `**后续动作**:` 和 `## 后续动作` 两种写法；新待办会显示 `对象类型: stakeholder` 和对应相关方对象。

## 一致性检查有警告

运行：

```bash
python3 scripts/doctor.py
```

报告中的跨文件重复事件 ID 不一定是错误；机器索引用 `event_key` 区分。同一文件内重复事件 ID 必须修复，否则会产生相同 `event_key`，`rebuild-index.py` 会停止重建。还需要优先处理缺失 `反馈类型/证据等级/核实状态` 的 `FBK`、不存在的关联事件、失效待办来源，以及低证据等级内容被写进成员长期蒸馏的情况。
