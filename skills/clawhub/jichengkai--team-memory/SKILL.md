---
name: team-memory
description: 管理者的团队长期记忆。自动保存相关沟通原话、成员与公司资料、事件、反馈、判断、待办及摘要，支持可追溯查询、1:1、周报、绩效材料和团队看板；独立JSON记忆库通过Notion在Amoo、OpenClaw等设备间合并同步，提供旧记忆导入、导出恢复及安全升级。
metadata:
  short-description: 团队记忆、沟通吸收与多设备合并同步
  version: "3.0.1"
license: MIT
---

# Team Memory 3.0

能力程序与团队记忆分开。安装目录只存规则、脚本和通用模板；真实数据、角色、别名及评价维度属于独立记忆库。运行需要 Python 3.10+，只使用标准库。

## 首次接入

先读 `references/new-device-join.md`。已有云库必须 `library join`，核对库身份并完整下载校验，不能自行 `init` 新空库。新设备不复制其他设备的 `.runtime/`、身份、凭据或锁。

统一入口：`python3 <本skill目录>/scripts/team-memory.py`。以下以 `TM` 代指该命令；不是已安装的系统别名。默认库在 `~/.team-memory/libraries/<library-id>/`；可用全局参数 `--library-root <目录>` 显式指定。所有命令默认返回 JSON，正常状态只返回版本、数量和异常。

## 每段团队沟通

1. 新段沟通、明确要求最新情况、正式材料前执行 `TM session prepare --fresh`。连续普通追问复用本端快照，按对象和关键词 `record query`；需要完整内容时 `record show`，核对原话时 `record source`。不把整库全文送进上下文。
2. 本轮包含有价值的团队信息时，在回复前用 `record capture --input <本端临时JSON>` 保存相关用户原话、结构化内容及关键结论；生成稳定的 `input_id` 与条目 `key`，重试复用。临时输入保存在独立库的 `.runtime/` 或系统临时目录，不写进skill目录。
3. 按 `references/record-format.md` 区分事件、反馈、用户判断和AI推断，关联已有对象ID。只把明确动作设为任务，不把期待自动变成承诺。没有日期、身份或核实状态就保持未知。相关方可以是 person/company/department/project 等 entity。
4. 修订先读取当前记录，提供 `expected_revision`；使用同一记录ID形成新修订。新增或修改用 `record put`。角色、别名、评价维度等用 `configuration` 记录保存；不修改程序模板保存个人配置。
5. 普通相关追问结束时执行 `TM session checkpoint`，即使本轮没有新事实，也让15分钟空闲时间从本轮重新计算。同一设备多个聊天共用一个批次。捕获和checkpoint会按需启动后台worker。
6. 用户明确要求保存或表示沟通结束时，执行 `TM session flush`，提交本端所有待提交内容。普通回复有修改时简短显示“已保存本端，等待合并同步”。只有返回已确认的云端版本且 `pending=0` 时，才能说已同步云端；冲突、重试或可读视图滞后照实说明。

自动保存团队内容和临时失败后的补传已包含在本工作流中。敏感凭据不作为团队记忆保存。普通任务不得触发与团队无关的内容采集。

## 同步与后台

- 最后一次相关沟通后空闲15分钟提交；worker每60秒只看本端截止时间，不调用模型。没有待提交内容或派生视图修复时退出，没有数据变化的空闲检查零云端请求。
- 关机、暂停或进程终止后，重新启动worker或下一次prepare会处理已到期批次。宿主应用应在启动时运行一次 `TM worker run`，并允许后台子进程；配置方法见接入指南。
- 提交前检查云端、下载增量并合并。另一端只看到已提交的内容。本端未提交的内容也能查询和分析，正式输出标明本端待提交状态。
- 暂时失败本端保留，按服务端提示与1、5、15、60分钟退避，随后最多每小时重试。授权、权限或完整性错误暂停；处理后运行 `TM session flush --retry`。
- 独立新增自动合并。同一记录不兼容修订保留双方原文，生成冲突记录。其他安全内容照常提交；涉及冲突的结论明确标注待确认。用户选定后 `record resolve --conflict-id <ID> --take local|remote`，随后flush。
- 删除必须明确确认，用 `record delete --id <ID> --expected-revision <修订> --confirm` 生成墓碑。历史继续保留；恢复用同参数的 `record restore`。

## 查询与管理场景

人物卡、公司及部门背景、近期表现、相关方反馈、管理者反思、追踪项、我的承诺和阶段摘要统一查询新记录。准备1:1、周报/月报、绩效/晋升、复盘和向上汇报时，按需阅读 `references/management-workflows.md`，综合来源并给出证据ID，区分事实、反馈、判断和建议。

正式材料先prepare。`TM report --format markdown|json|svg --output <路径>` 生成证据视图或A4摘要；`--scope tasks --period week|month` 按最近修订时间复盘任务，不冒充事件发生时间。SVG只展示最近24条并标明范围；Markdown/JSON保留完整正文与来源。报告不能根据记录数量自动形成绩效结论。

摘要也是带来源的 `summary` 记录，保留历史修订；只在相关内容变化且确有价值时更新，不为每轮聊天调用额外模型蒸馏全库。

## 迁移、恢复和升级

- 日常路径只读3.0 JSON。旧文件名、旧字段和Markdown兼容只存在于 `library import-legacy` 单向导入器，不使用旧脚本混读。
- 导入、标准导出和独立恢复见 `references/migration-and-upgrade.md`。示例按本次指定的文件和区段隔离，不能按“张三”等名字永久排除人物。
- `TM library doctor` 检查记录、来源、日期与历史引用；索引为可重建缓存，不覆盖正式数据。
- 替换skill程序包不覆盖独立记忆目录。同格式版本更新不迁移数据；格式更新仅运行新版程序内已注册、可验证的迁移链，取得云端租约后快照、暂存转换、校验、切换。失败保留现场和原库。未知格式停止，不猜测兼容。
- `TM library export --output <完整包.tmemory.zip>` 包含原文、正式记录、全部历史、冲突、配置、迁移清单和逐文件哈希；不含程序、凭据、设备身份、缓存或日志。恢复不依赖Notion。
- 当前正式适配Notion。FlowUs/NAS可使用平台无关标准包做以后迁移；本版本不宣称已实现其双向适配。

## 权限和网络范围

仅向所配置的Notion云库上传必要记忆包及派生视图；附件下载使用Notion返回的临时HTTPS地址。Notion令牌从本进程 `TEAM_MEMORY_NOTION_TOKEN` 环境变量读取，不能出现在JSON输入、日志、导出包或聊天里。后台程序仅执行本安装包脚本，不安装远程代码。详细协议见 `references/sync-protocol.md`，异常处理见 `references/troubleshooting.md`。
