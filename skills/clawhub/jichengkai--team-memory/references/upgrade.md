# Team Memory 升级与兼容说明

当前产品版本：`v2.7.0`
当前数据结构版本：`schema-version: "2.2"`

发布包可以是 lean runtime 包，也可以自带 `data/`。未启用双向在线同步时 Markdown 文件树是唯一可信源；双向模式也必须先把在线变更同步为本地 Markdown。JSONL/SQLite 只作为可重建机器索引。

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

## v2.8.1 变更摘要

- 修复双向拉取使用渲染正文导致谈话原文换行变化、来源 hash 不匹配的问题；拉取已提交文件现在验证并写入原始字节，不重写远端载荷。
- 本机状态增加独立的原文载荷基线，正确识别其他实例仅修改换行或空白的提交，避免用旧本地副本反向覆盖。
- 谈话原文/拆解映射的直接在线编辑隔离为冲突；普通业务页继续支持在线修改。全部待拉取载荷通过校验后才写本地，拉取后刷新查询索引。
- 新增两个独立实例交换并重新处理完整谈话的回归验证；既有 schema `2.3` 与在线协议 `2.0` 保持兼容。

同一在线库的实例应一起升级至 v2.8.1 或更高兼容版本，避免旧版继续按渲染正文拉取。原始载荷尚完好的文件可在新版保持原样；已经被旧版改写的原文不会自动猜测修复，应核对仍保留的原文或历史载荷。

## v2.8.0 变更摘要

- 扩充公司时间轴/摘要、管理者反思/摘要和正式谈话来源空间；部门沿用现有相关方。
- 新增 `ingest-conversation.py capture/apply`，保存原文、稳定来源 ID 和拆解映射，支持重复跳过、修订保留、待确认部分和中断重试。
- 统一索引支持 `CMP`/`REF`、说话人、信息性质、来源行号和主记录；补齐成员证据字段。待办扫描覆盖公司和管理者明确动作，原文不直接生成任务。
- 看板避免把关联摘要重复计数，也不把未核实自述、判断或推断转换为人员绩效信号。
- 在线协议升级为 `2.0`，增加原始字节恢复载荷及完整性校验；旧 manifest 兼容读取，升级后的远端库拒绝旧客户端写入。
- 新初始化的数据 schema 为 `2.3`；已有 `2.2` Markdown 主库保留并兼容。初始化/接管仅补缺失目录和文件，不覆盖已有记录。

升级前先完整导出。使用原主库配置及锁，运行新版 `init.sh` 或正常接管补目录；不要删除或另建一套主库。已连接在线笔记时先看 `plan`，新版首次写入会升级远端协议；同一库的其他机器同时升级 skill。原文载荷只从本地现存原文补齐，不能还原早期备份已经丢失的格式。

## v2.7.0 变更摘要

- 新增 Notion 与 FlowUs 在线笔记适配器，支持单向备份和单笔记本双向同步
- 新增 `scripts/notebook-sync.py` 连接、预览、同步、恢复、冲突、删除确认、模式切换和 macOS 定时任务命令
- 新增远端租约、三方比较、manifest 双槽事务、写时复制页面、未完成事务回滚和“当前版 + 一个上一版”保护
- 跨机器已确认删除不得复活；恢复过程持有远端租约并在落盘前复核快照
- 新增 `.team-memory-notebook.json` 非敏感连接配置和 `data/.sync/` 本机状态目录
- `doctor.py --online` 检查凭据、仓库 ID、manifest、未完成事务、冲突、墓碑和不支持的 Markdown
- `export-data.py` 排除 `.sync/` 和凭据，只附带脱敏在线同步摘要
- 本地 Markdown schema 保持 `2.2`；在线连接协议独立使用 `notebook-schema-version: 1.0`

从 v2.6 升级不需要迁移 Markdown。在线连接默认关闭；只有主动运行 `notebook-sync.py connect` 才会创建配置和远端页面。

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
