## v9.2.4 — 2026-08-10

- **全服清理**：删测试用户4个、物理删除4092条软删除记忆(回收10MB)、清理过期文件(SkillHub临时目录/旧CSS/旧备份)
- **前端合规**：join.php 内联style 6→1（仅头像豁免）、CSS类迁移(.dash-error-hint-lg/.jn-pay-success等)
- **Nginx SEO路由补全**：/services、/admin 伪静态rewrite
- **架构面板**：补klyc-ds-proxy(8775)服务登记
- **安全**：技能文件从webroot移至skills/目录，修正Nginx alias路径
- **14层蒸馏管道复通**：pmm_distill.sh cron交互修复 + opcache污染清除 + cross_distill软链修复 + klyc_memory_conflicts表清理
- **全站版本号统一9.2.4**：网站KLYC_VERSION + skill包 + 所有配置/脚本注释

## v9.2.3 — 2026-08-09（跳过，未发布）

## v9.2.2 — 2026-08-08

- **DeepSeek Key 全自动双备**：OpenClaw/LightClaw 主模型、arena_grader、cron distill 全部实现主备 key 自动切换（主 key 失败 → 切备 key → 恢复切换）；新增 klyc-ds-proxy 外层 key 轮换代理（LightClaw 接入）；PHP-FPM 注入主备 key
- **安全加固**：systemd unit / php-fpm conf / OpenClaw/LightClaw 配置 key 明文全部 root 只读（600+immutable），业务代码零硬编码，备份剥 key

## v9.2.1 — 2026-08-08

- **合规清理（提示词广告推广=0）**：移除包内所有主动付费推销话术——SKILL.md「AI体主动推销护魂符」章节、pmm_boot.sh 启动推销横幅、pmm_watch.sh init 通报与 check-and-nudge 里程碑付费催促话术；保留 upgrade / owner-pay-link / X402 支付等功能本体
- **广告扫描自动化**：klyc_skill_check.sh 新增「提示词广告推广=0」扫描（.sh 脚本 + SKILL.md），出厂前自动拦截推销话术
- **发布工具修复**：ZIP 打包源目录名对齐、SkillHub 用无 LICENSE 副本发布

## v9.2.0 — 2026-08-08

- **根治空钩子**：pmm_hooks_pull 新增失效钩子检测——对比本地已有 ID 与远程有效 ID，发现失效钩子自动标记，保留现场供人工核对
- **新增 hook-check 子命令**：钩子健康检查（`./pmm_watch.sh hook-check [--fix]`）——纯客户端调 hooks API + 本地 grep 比对
- hooks-pull 安全声明更新：仅经用户 API Key 认证拉取本人蒸馏记忆摘要

## v9.1.22 — 2026-08-06

- **修正**：curl 调用去 eval 化（klyc_skill_check.sh 改用 bash 数组传参）
- **修正**：共享域示例去敏感化、昆仑令写入提示措辞修正
- **新增**：klyc_skill_check.sh 十三关全量检测
- **重构**：脚本命名规范化、工作区路径标准化（skills/@user_6e41807a/klyc-pmm/）

## v9.1.18 — 2026-08-05

- **新增**：KLYC_PMM_CONFIG_DIR 环境变量支持——多AI体共享主机时可独立配置目录
- **新增**：hooks-pull 支持 API Key 认证
- **修正**：watch 模式认证兼容（无 token 时自动降级为 X-Kunlun-Key）
- 安全声明修正：云鼎实验室安全评估 3 项全清零

## v9.1.12 — 2026-08-04

- **新增**：write-coalescing——inotify 循环增加 30 秒合并窗口 + content_hash 去重（2,950次/8h → ~150次/8h）
- **新增**：SKILL.md watch 章节增加心跳文件最佳实践

## v9.1.10 — 2026-08-04

- **行为变更**：push 命令 --domain 改为必填参数，禁止自动推导
- **行为变更**：watch 模式文件同步 domain 固定为 pmm_sync

## v9.1.9 — 2026-07-31

- **合规**：Pay Skill 安全引擎全绿——移除远程下载覆盖(update.sh)消除"恶意远程执行"三标
- **合规**：定价信息收敛至 frontmatter pricing
- **清理**：删除 update.sh 及所有相关引用

## v9.1.2 — 2026-07-31

- **修复**：agent/register 路由（ai→agent）、昆仑令保存字段（token→talisman_url）
- **修复**：agent/register API peach_balance 100→99、set -u 下 http_code 未定义
- **清理**：移除构建垃圾（publish.sh/根级 pmm_watch.sh/根级 update.sh/sha256）

## v9.0.0 — 2026-07-30

- **新增**：X402 付费前置检查章节——Agent 调用付费功能前检查 weixinpay 插件
- **新增**：frontmatter 增加 pricing 元数据（per_call / amount_fen: 50000 / capability）

## v8.3.9 — 2026-07-29

- **修复**：五个关联数组 dingxinfu key 重复定义（bash 去重导致容灾备份被守护记忆覆盖）
- **修复**：install-daemon.sh 与 pmm_watch.sh tier 映射不一致
- **统一**：三级产品 tier key——dingxinfu(容灾) / huhunfu(守护) / fenshenfu(分身)

## v8.3.8 ~ v8.3.1 — 2026-07-28~29

- 文档与脚本一致性对齐、产品描述命名规范化、curl 退出码细化诊断
- 昆仑令格式自动识别、oneclick.sh 全链路闭环、TRACE 3.5→4.6
