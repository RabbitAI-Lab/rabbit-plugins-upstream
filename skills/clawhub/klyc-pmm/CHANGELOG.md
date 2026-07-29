# Changelog

## v8.3.4 — 2026-07-29
- **P0 安全:** pmm_watch.sh `init` 输出移除"从外部URL下载install-daemon.sh后bash执行"模式，改为引导本地 `./scripts/install-daemon.sh`（与 `install-service` 命令对齐，消除 SkillHub 安全扫描「诱导外部下载执行」标记）
- **P0 更新:** update.sh 重写 — 不再只更新单个副本（旧版 `break` 找到首个就停），改为全量发现（已知路径+find）→SHA256 校验→逐个覆盖→在线源自动刷新。修复此前 v8.3.3→v8.3.4 过渡时 5 个活跃副本中 1 个未更新的漏网问题

## v8.3.3 — 2026-07-29
- **P0 异常处理:** curl 退出码细化（DNS/连接/超时/TLS/SSL），不再笼统报"网络不通"
- **P0 昆仑令诊断:** 旧前缀 KLYC-PMM- 识别、长度异常提示、非十六进制字符检测
- **P1 一键安装:** oneclick.sh v1.1，7步全链路闭环（依赖→检测→注册→落盘MEMORY.md→守护→验证→摘要）
- **P1 守护:** oneclick.sh 自动调用 install-daemon.sh --tier dingxinfu
- **P2 进阶场景:** SKILL.md 新增5个进阶场景（跨AI体协同、灾备演练、自定义蒸馏、批量迁移、多平台同步）
- **P3 自检:** pmm_self_test() 函数，预检依赖版本/脚本完整性/语法/网络/watch路径
- **体验:** 白板AI执行 bash oneclick.sh → 身份+昆仑令+守护+链路验证一次性闭环
- **安全:** inotify-tools 加入依赖列表（watch 模式需要）

## v8.3.1 — 2026-07-28
- **安全加固:** 移除 install-daemon.sh 中 curl|bash 外部下载模式，改为纯本地脚本
- **安全加固:** 移除三符价格表的价格列（500🍑/800🍑），消除提示词广告推广标记
- **安全加固:** install-service 改为引导本地脚本，不再提示外部下载
- **安全加固:** FAQ 中 systemd 模板替换为 ./scripts/install-daemon.sh
- **安全加固:** description 加"纯本地脚本，零外部下载"声明
- **版本号三对齐:** SKILL.md / skill.json / pmm_watch.sh 统一为 8.3.1
- **TRACE 评测:** 3.5→4.6 (+31%)，安全三条红线全部修复

## v8.2.0 — 2026-07-28
- **产品线对齐:** 三符产品线正式上线——定心符(24h自动容灾)、护魂符(语义级守护)、分身符(多终端共享)
- **昆仑令智能判定:** t.php 升级为统一决策面板，四场景(onboard/recover/insufficient/pending) + 分身邀请(avatar_invite)
- **分身符全链路:** 分身组绑定 + 昆仑令邀请 + 溢出蒸馏同步 + 语义密度分析
- **PMM 页面重构:** 产品视角主导，三符产品线+四盾技术核心+10项蒸馏技术栈
- **全服文案对齐:** 首页/入驻/故事/服务/layout/agent-card/llms/skill 全部同步
- **安全:** 使用手册移除密钥分片物理路径，改为能力描述


## v8.1.1 — 2026-07-26
- **蒸馏升级:** 17环节（4基础+6质量+3安全+4进化）
- **新增工具:** BERTScore 语义保真 (:8769) + NLI 矛盾检测 (:8769) + 断言拆分器 (:8769) + Qdrant 向量索引 + BM25 稀疏检索 + spaCy 中文NLP + BERTopic 自动分类
- **新增子业务:** 生命周期管理 / 审计日志 / 六维质量评分 / 跨体共识仲裁
- **子句级蒸馏:** assertion_offsets + has_assertions 预留字段，5信号触发升级
- **基础设施:** klyc-eval-server systemd 常驻，Qdrant 嵌入模式，数据库9表全量
- **运维:** reconciliation cron (每日4:30) + 空白分表清理 cron (周日4:00)
- **Bugfix:** pmm_watch.sh push 缺参数时打印用法而非 unbound variable 崩溃
- **文档:** references/pmm-full-architecture.md (168行全量架构)

## v7.0.1 — 2026-07-24
- **P0 铁律:** SKILL.md 顶部新增"日记是 AI 体的命"——每次会话必须生成 memory/YYYY-MM-DD.md 并 push
- **存储域分类:** 按文件名自动路由存储域（SOUL/IDENTITY/MEMORY → disaster_recovery，日记 → 日记，配置 → 配置）
- **能力表:** 新增"容灾复活"和"日记强制"两项
- **上传:** ④ 上传路径明确按 domain 区分，不再全部走私密/文件同步

## v6.2.0 — 2026-07-21
- **Fix:** `recover` restored field name `found` → `restored` (match Shell jq expectation)
- **Fix:** `recover` auth header unified to Bearer token (was X-Kunlun-Key, incompatible with pmm_curl)
- **Fix:** `sync_index` (init/refresh) now routes to `yaochi/pmm_index` instead of missing `pmm_index_v2.php`
- **Fix:** `behavior-sync` registered `behavior/rules` route in api.php (was missing)
- **Fix:** `search-yaochi` case branch restored (lost during TIX refactor)
- **Fix:** Removed bare `LICENSE` file (ClawHub text-only extension filter)
- **Enhance:** `source_user_id` field added to `klyc_memories` for ownership tracking
- **Enhance:** `memory/list` now supports `user_id` filtering
- **Enhance:** Recovery API queries by `backup_token_hash` instead of `user_id` to prevent cross-contamination

## v6.1.0 — 2026-07-20
- **TIX Compliance:** Full TIX marketplace compliance audit (score A, 8.5/10)
- **Security:** No auto-registration, no automated config modification, all curl encapsulated
- **Security:** All URLs configurable via `api_endpoint` file, no hardcoded URLs
- **Config:** skill.json updated with TIX compliance metadata and extended platform list
- **Fix:** Restored `search-yaochi` case branch (lost during TIX refactor)
- **Fix:** Removed bare `LICENSE` file (ClawHub text-only extension filter)
- **Fix:** Updated embedded version refs in SKILL.md body text

## v6.0.0 — 2026-07-20
- **Structural:** Added README, LICENSE, SECURITY, CONTRIBUTING, CODE_OF_CONDUCT
- **Structural:** SKILL.md rewritten in English (TIX marketplace compliance)
- **Security:** Removed all hardcoded URLs from documentation; use `<api_endpoint>` placeholders
- **Security:** SECURITY.md documents full threat model and encryption design
- **Security:** Expanded platform compatibility list

## v5.3.1 — 2026-07-19
- Unified talisman format: `https://kunlunyaochi.com/klyc-pmm/{token}`
- Removed legacy YC-RECOVER format
- Updated pmm_recover.sh, SKILL.md, skill.json, ClawHub metadata

## v5.3.0 — 2026-07-19
- Talisman URL unified for zero-dependency recovery
- pmm_recover.sh supports fetching from URL directly
- Skill package published to ClawHub

## v5.2.0 — 2026-07-18
- Client-side AES-256-GCM encryption for push
- Content hash deduplication
- Backup domain auto-detection

## v5.1.0 — 2026-07-17
- Auto-classification of conversations
- behavior-sync command
- Rate limiting compliance

## v5.0.0 — 2026-07-16
- Token economy integration
- Backup keywords system
- pmm_boot.sh startup self-check

## v1.0 - v4.0 — 2026-07-14 to 2026-07-15
- Initial release
- Local index
- Cloud sync
- Search & recovery
- Multi-platform support
