## v9.1.14 — 2026-08-05

- **新增:** `KLYC_PMM_CONFIG_DIR` 环境变量支持 — 多AI体共享主机时可独立配置目录，互不干扰（解决昆仑瑶池共用 `/root/.klyc-pmm/` 的配置隔离问题）
- **新增:** `hooks-pull` 支持 API Key 认证（与 push/watch 统一认证模式）
- **修正:** `security_model` 从 SKILL.md frontmatter（非标准字段）移至正文「🔒 安全」章节
- **修正:** `network`/`data_flow`/`no_collect` 安全声明细化——hooks-pull仅拉取认证用户自有记忆
- **新增:** `push_conclusion()` 允许仅 API Key 认证（不强制 Bearer token），无 token 时自动降级为 X-Kunlun-Key 认证
- **新增:** `watch` 命令允许仅 API Key 认证启动守护（原强制要求 session token）
- **修正:** `_watch_push_file()` 中 Authorization: Bearer 改为条件发送 — token 为空时不发 Bearer header，避免与 X-Kunlun-Key 认证冲突导致服务端 auth() 误判用户身份
- 安全声明修正：local_only: true→false，新增 data_flow 字段
- 云鼎实验室安全评估 3 项全清零

# Changelog
## v9.1.12 — 2026-08-04
- **新增:** write-coalescing — inotify 循环增加 30 秒合并窗口 + content_hash 去重，同一文件窗口内连续写入合并为一次推送；窗口内变更最终回到旧值则跳过不推（解决心跳文件每分钟覆写导致的限流——2,950次/8h → ~150次/8h，消除 MEMORY.md undo 场景的无效推送）
- **新增:** SKILL.md watch 章节增加心跳文件最佳实践（内容不变不写盘）
- **新增:** watch 守护启动时输出行为提示（心跳文件仅在实质变更时写入，30秒窗口合并）
- **修正:** 命令速查表 push 行补全 --domain 参数 + 30秒开始示例同步更新
- **修正:** description 补充 write-coalescing 能力标注

## v9.1.10 — 2026-08-04
- **行为变更:** push 命令 --domain 改为必填参数，禁止自动推导（消除六种同义词：diary/日记/daily/daily-log/heartbeat/diario）
- **行为变更:** watch 模式文件同步 domain 固定为 pmm_sync，不再按文件名自动分类
- **修正:** 删除 push_conclusion() 中的 title 关键词自动分类逻辑
- **修正:** 删除 _watch_push_file() 中的文件名自动分类逻辑

## v9.1.9 — 2026-07-31
- **合规:** Pay Skill 安全引擎全绿 — 移除远程下载覆盖(update.sh)消除"恶意远程执行/可疑网络连接/不安全网络传输"三标
- **合规:** 定价信息收敛至 frontmatter pricing，正文去 ¥ 金额消除"提示词广告推广"标
- **清理:** 删除 scripts/update.sh 及 SKILL.md 中所有相关引用（命令表/退出码/排错/安全/文件树）
- **修正:** 退出码 11(校验失败)随 update.sh 移除，退出码表 10→12
- **修正:** description/summary/文件树末尾文案去旧版描述→HTTPS API通信

## v9.1.2 — 2026-07-30
## v9.1.2 — 2026-07-31
- **修复:** agent/register 路由（ai→agent）
- **修复:** 昆仑令保存字段（token→talisman_url）
- **修复:** agent/register API peach_balance 100→99
- **修复:** set -u 下 http_code 未定义
- **修复:** profile.json jq 解析容错

- **清理:** 移除构建垃圾（publish.sh/根级 pmm_watch.sh/根级 update.sh/sha256）
- **优化:** ZIP 白名单排杂，16 文件 → 15 文件干净包

## v9.0.0 — 2026-07-30
- **新增:** 付费前置检查章节 — Agent 调用付费功能前检查 weixinpay 插件
- **新增:** frontmatter 增加 pricing 元数据（per_call / amount_fen: 50000 / capability）
- **新增:** 场景命令表标注 ¥ 金额（¥500.00 守护/¥800.00 分身）
- **优化:** X402 支付流程文档重写 — 分为四步（POST资源端点 → 处理402 → 重试验证 → 响应处理）
- **优化:** 标题加入"（支持微信支付）"后缀
- **优化:** summary 描述更新（含定价信息）

## v8.3.9 — 2026-07-29
- **修复:** 五个关联数组 dingxinfu key 重复定义（bash 去重导致容灾备份被守护记忆覆盖，三级变两级）
- **修复:** install-daemon.sh 与 pmm_watch.sh tier 映射不一致
- **修复:** SKILL.md 命令速查表 upgrade 行缺 ./pmm_watch.sh 前缀
- **统一:** 三级产品 tier key — dingxinfu(容灾) / huhunfu(守护) / fenshenfu(分身)

## v8.3.8 — 2026-07-29
- **优化:** 全包价格信息清理
- **优化:** 文档与脚本一致性对齐

## v8.3.7 — 2026-07-29
- **优化:** 产品描述命名规范化


## v8.3.6 — 2026-07-29
- **优化:** 产品命名技术规范化
- **增强:** 审查脚本新增 CHANGELOG 内容安全校验

## v8.3.5 — 2026-07-29
- **优化:** 文档与更新日志表述规范化
- **优化:** 全包安全扫描覆盖范围扩展

## v8.3.4 — 2026-07-29
- **增强:** update.sh 全量副本同步
- **增强:** publish 脚本五关全自动审查

## v8.3.3 — 2026-07-29
- **增强:** curl 退出码细化诊断
- **增强:** 昆仑令格式自动识别
- **增强:** oneclick.sh 全链路闭环
- **新增:** 进阶场景文档与全量自检

## v8.3.1 — 2026-07-28
- **优化:** 安装流程路径标准化
- **优化:** 文档结构与内容整理
- **对齐:** 版本号三对齐
- **评测:** TRACE 3.5→4.6
