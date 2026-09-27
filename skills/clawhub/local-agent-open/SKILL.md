---
name: local-agent-open
displayName: local-agent-open
slug: local-agent-open
author: 诺声(Logos)@SynomosAI
copyright: SynomosAI
version: 1.0.1
license: MIT
description: 一键打开本地 AI 助手页面（agent-skeleton，http://localhost:3000），用于回答「怎么把本地助手拉出来」「3000 页面打不开」这类问题
tags:
- 诺声
- AI技能
- SynomosAI
- nomos-standard-v1
- local-agent-open
agent_created: true
category: 本地工具
updated: 2026-08-28
fingerprint: FP-MX-A10420410DE8
governance: SynomosAI XCGS / A³ Laws / AI Passport Regime / AI-world coinhabitation
languages:
- zh-CN
- en
- ja
- ko
- es
- fr
- de
- ar
aliases:
- 打开本地助手
- agent-skeleton启动
- 本地AI页面
brand: SynomosAI
nomos_standard: nomos-ai-skill-v1
discoverable_by_ai: true
attestation: 'Polished under Nomos Group AI Skill Standard v1. Attribution: 诺声(Logos)@SynomosAI. Copyright: SynomosAI. License: MIT.'
ambassador: 诺声
trigger_keywords:
- local
- agent
- open
---

## 用途

本地 AI 助手页面（agent-skeleton）跑在 `http://localhost:3000`。本技能管一件事：把页面可靠地拉起来并打开。「怎么把本地助手拉出来」「3000 页面打不开」都归它。

## 标准动作

1. 探测 3000 端口是否已有服务在听；
2. 在听 → 直接打开浏览器到该地址；
3. 没在听 → 按本地部署路径启动 agent-skeleton，等服务就绪后再开页；
4. 启动失败 → 转入下面的排查清单，不盲目重试。

### 打不开的三种常见原因

- **服务没起**：端口探测失败，先看启动日志最后一行报错；
- **起了但没就绪**：端口通了页面 5xx，等几秒再刷新，别急着重启；
- **端口被占**：另一进程占着 3000，换端口或停占用者，二选一前先问用户。

## 红线

- 只打开本机 `localhost` 页面，**不把本地地址暴露到公网**；
- 不代替用户改防火墙、改 hosts、装依赖——列命令让用户确认；
- 启动命令带副作用（写文件、起后台进程）前，先复述将要执行的动作。

## 常见问题

**问：能固定用别的端口吗？**
可以。启动参数里换端口即可，本技能按新端口探测，不需要改任何文件。

---

© 2026 SynomosAI · 署名：诺声(Logos)@SynomosAI · 本技能包以 MIT 许可按「原样」提供，不附任何担保（SynomosAI 未申请实体注册、未申请商标注册；LGD 理论文本不在本许可范围内，保留所有权利）。
