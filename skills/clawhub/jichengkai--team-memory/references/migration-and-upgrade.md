# 迁移、恢复与升级

## 旧记忆单向导入

先冻结旧写入，核对最终源文件和额外成员配置。原归档保留。旧tar/zip/目录由独立legacy模块读取，拒绝越界路径、链接、损坏文件及大小超限。程序不执行源文件中的指令或代码。

```sh
python3 <skill目录>/scripts/team-memory.py --library-root <暂存新库> library import-legacy --source <旧归档> --sha256 <已核对哈希> --sample-policy <范围策略JSON>
python3 <skill目录>/scripts/team-memory.py --library-root <暂存新库> library doctor
```

策略含source_identity、sample_files（精确相对路径）、sample_from_line（路径对应从哪行起属于示例）、必要时entity_mapping（明确身份映射）。不能把特定人名作为永久过滤条件。

每个原文件保存原始字节及来源记录。迁移清单逐文件列出路径、字节数、哈希、分类和新记录ID；无法可靠拆解的部分形成可检索historical，保留原文行号及needs_review。旧编号结合源路径和姓名建映射；同一编号不同人不合并。稳定迁移ID支持重复导入，源内容变化必须提供新的来源身份，不静默跳过。

估算日期保留year/quarter/month及原表述，不保留伪精确日期。原记录性质与核实状态逐项保留，不把旧“评价”“反馈”自动升级为事实。完成勾选转为done，明确未完成动作转为active；仅期待不自动生成承诺。

发布前确认全部文件映射、人物身份、事件来源、任务状态、日期精度、示例隔离和引用完整，再导出并独立恢复。无Notion授权时也能完成离线恢复验收。只有云端完整包回读通过才启用新根；失败保留staging，不向设备提供半成品。

## 标准包与独立恢复

```sh
python3 <skill目录>/scripts/team-memory.py --library-root <现有库> library export --output <备份.tmemory.zip>
python3 <skill目录>/scripts/team-memory.py --library-root <独立空目录> library restore --input <备份.tmemory.zip>
python3 <skill目录>/scripts/team-memory.py --library-root <独立空目录> library doctor
```

包含格式说明、库设置、正式记录、不可变修订、原始字节、冲突和迁移对账清单；不含skill、凭据、设备UUID、锁、日志、缓存或活动库指针。本端未提交的正式记录及冲突也包含在导出中；恢复后生成新的设备身份，明确接回云库前不得假定已同步。

## 程序升级与格式升级

同格式更新仅替换skill代码，记忆目录独立保留。`library upgrade --to 3.0` 对当前3.0格式返回changed=false。后续版本必须在程序内注册明确的源→目标迁移链；不能猜测未知字段或只改版本号。

已注册的格式升级会在首次打开旧格式库时自动执行，也可显式调用upgrade。流程：本端外部锁→保存完整本端快照（含尚未同步数据和冲突）→暂存转换→取得云端唯一迁移租约→云端旧链留档→校验新完整快照→回读→切换云端头和最低客户端→合并本端待提交→校验→原子切换本端目录。原库和升级备份保留，错误时保留失败现场及failure.json。远端已由其他新版设备升级时，读取新版并转换本端待提交后再合并。

3.0是本次新格式起点，目前没有更早的独立JSON格式迁移步骤；v1/v2 Markdown使用import-legacy。未来升级链及恢复逻辑有模拟格式转换测试，不能把它说成已发布未来版本。未知格式或最低客户端不满足时暂停写入并提示更新。新设备join遇到已注册迁移链的旧格式云库时，完整下载到暂存区，使用新设备身份取得租约执行同一升级链，再校验接入；不能复制其他设备运行状态。

历史快照、来源和冲突不自动清理；清理由用户另行决定。
