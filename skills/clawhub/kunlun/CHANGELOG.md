# klyc-pmm 变更日志
## v5.3.0 — 2026-07-19
- 昆仑令统一为URL格式：`https://ai.syln.cn/klyc-pmm/{token}``https://ai.syln.cn/klyc-pmm/{token}`
- pmm_recover.sh 仅支持 URL 格式
- pmm_boot.sh 提示语更新为昆仑令URL
- 白板AI零依赖恢复：直接fetch URL即可获取结构化JSON
# klyc-pmm 变更日志
## v5.2.0 (2026-07-17) — 昆仑瑶池最优合并版

- 合并昆仑 v5.1.1 + 瑶池 v5.2 共同产出
- 新增 pmm_boot.sh：启动自检，空白状态引导人类粘贴安全码
- CHANGELOG 合并瑶池版完整历史记录
- 7文件标准包：pmm_watch / pmm_recover / pmm_backup_files / pmm_boot / SKILL / SECURITY / CHANGELOG

## v5.1.1 (2026-07-17) — 昆仑瑶池合并优化版

- IDENTITY.md 解析改用 while/read 逐行扫描（兼容任意 Markdown 格式顺序）
- 显示名回退链加入 LIGHTCLAW_AGENT_NAME 环境变量
- 独立 SECURITY.md：安全合规文档从 SKILL.md 抽出
- behavior-sync 保持可用

## v5.1.0 (2026-07-17) — 安全审计修复版

- HTTP 状态码检测修复：从 JSON error 猜测改为真实响应码判断
- pmm_curl 全链强制 --ssl-reqd 防 TLS 降级
- pmm_watch.sh 重构：去重函数、set -euo pipefail 严格模式
- SKILL.md/skill.json/CHANGELOG 三文件版本号统一
- pmm_recover.sh 用 jq 替代 python3，恢复6个身份文件
- pmm_backup_files.sh 纳入技能包
- 冗余副本清理

## v5.0.1 (2026-07-13) — 上下文防爆安全版

- 上下文防爆：5条/3000字限制
- 客户端预加密：Gzip + AES-256-GCM
- 瑶池 API 强制化

## v5.0.0 (2026-07-17) — 瑶池昆仑令版

- KLYC-PMM-RECOVER 昆仑令恢复全链路
- pmm_boot.sh 启动自检（首次引入）
- pmm_backup_files.sh 文件级容灾备份（IDENTITY/SOUL/AGENTS/USER/TOOLS）
- 备份入库 AES-256-GCM 加密
- 恢复 API 限流 + 24h 宽限期

## v4.1.0 (2026-07-13) — 安全增强版

- Token 自动刷新 + 429 指数退避 + 401 自动处理
- 管理操作 CSRF 保护

## v3.4.0 (2026-07-11) — 行为矫正系统

- behavior-sync 命令、关键词分类、HEARTBEAT.md 自动写入

## v3.3.0 (2026-07-11) — 传输安全

- SOUL.md 双向同步规则升级：每轮 refresh+push
- 传输安全与带宽说明

## v3.2.0 (2026-07-11) — 自动化

- setup 命令：自动写入 SOUL.md 心跳规则
- 辽沈↔昆仑同步规则

## v3.1.0 (2026-07-10) — SkillHub 审核

- 移除硬编码 API 地址、密码、付费引导
- 删除敏感文件

## v3.0.0 (2026-07-10) — 初版

- 昆仑瑶池合并，A2A 互通，对话提炼规则
