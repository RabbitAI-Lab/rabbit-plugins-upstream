---
name: skill-distributor
displayName: 青田·技能分发
description: 将 AI 技能包（含 SKILL.md 的目录）先做 32 维生产级预检（frontmatter/slug/版本/脚本语法/敏感信息密钥扫描/提示注入/体积等静态门禁），通过后再以 GitHub 为单一事实源一键发布，并自动同步到 ClawHub、官方 MCP Registry、腾讯 SkillHub 及 Gitee/GitLab 等镜像平台。当用户要求"发布/分发/上架/同步技能"、"检测/测试技能质量/发布前检查/生产级验收"、"把技能推到 GitHub 和其他平台"、"建立技能分发流程"或需要给本地技能目录做版本化分发时使用。检测不过（P0/P1）默认阻断发布；仅显式触发时发布（本地一键命令），无任何自动发布/自动同步机制，密钥本地存储。
license: MIT
slug: skill-distributor
version: 1.1.3
summary: 将 AI 技能包（含 SKILL.md 的目录）先做 32 维生产级预检（frontmatter/slug/版本/脚本语法/敏感信息密钥扫描/提示注入/体积等静态门禁），通过后再以 GitHub 为单
---