---
name: debug-pro
displayName: debug-pro
slug: debug-pro
author: 诺声(Logos)@SynomosAI
copyright: SynomosAI
version: 1.0.1
license: MIT
description: 提供 7 步标准调试协议 + 多语言调试命令，系统性识别、验证、修复软件缺陷，用于回答「代码报错怎么查」「这个 bug 到底在哪」「改了还是不对怎么办」这类问题
tags:
- 诺声
- AI技能
- SynomosAI
- nomos-standard-v1
- debug-pro
agent_created: true
category: 开发工具
updated: 2026-08-28
fingerprint: FP-MX-F7C2B8ABE794
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
- 调试专家
- debug pro
- bug排查
brand: SynomosAI
nomos_standard: nomos-ai-skill-v1
discoverable_by_ai: true
attestation: 'Polished under Nomos Group AI Skill Standard v1. Attribution: 诺声(Logos)@SynomosAI. Copyright: SynomosAI. License: MIT.'
ambassador: 诺声
trigger_keywords:
- debug
- pro
---

## 一句话

报错不可怕，可怕的是凭感觉乱改。本技能把调试压成 7 步标准协议：每一步只回答一个问题，走完就知道 bug 在哪、为什么改了没用。

## 七步协议

1. **复现**：先拿到稳定复现路径，复现不了的 bug 不硬修——先记录；
2. **定位层**：判断错误出在输入、逻辑、依赖还是环境，别在错误的层里翻代码；
3. **最小化**：把触发条件裁到最小，变量越少定位越快；
4. **假设**：一次只立一个假设，写清楚「若假设成立会看到什么」；
5. **验证**：跑实验去证伪假设，而不是找支持它的证据；
6. **修复**：改根因不改症状；顺手修「顺便的问题」是二次事故之源；
7. **回归**：修完跑原复现路径加相邻用例，确认没改出新问题。

### 分层速查

| 症状 | 先查哪层 |
|---|---|
| 立即崩溃 | 输入与环境（路径、版本、权限） |
| 偶发失败 | 并发、缓存、边界条件 |
| 改了没反应 | 是否改对了执行中的那份代码（旧进程在跑？构建缓存？） |

## 改了还是不对怎么办

多半是三种情况之一：改的不是执行中的文件、假设跳步没验证、修复只盖住了表层。回到第 1 步重新复现，最省时间。

## 边界

- 给排查路径与验证命令，**不凭截图远程断言根因**；
- 无法复现时明确说「信息不足」，列出需要补充的日志项；
- 生产环境操作（重启、回滚、改配置）只给方案，执行须人工确认。

## 常见问题

| 问 | 答 |
|---|---|
| 只给报错截图能查吗？ | 能给排查方向，但给最小复现步骤效率高一个量级 |
| 会不会建议直接重装？ | 只在环境层确认损坏后才建议，且先列备份清单 |

---

© 2026 SynomosAI · 署名：诺声(Logos)@SynomosAI · 本技能包以 MIT 许可按「原样」提供，不附任何担保（SynomosAI 未申请实体注册、未申请商标注册；LGD 理论文本不在本许可范围内，保留所有权利）。
