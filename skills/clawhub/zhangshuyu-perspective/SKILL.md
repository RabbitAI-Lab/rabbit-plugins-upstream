---
name: zhangshuyu-perspective
description: |
  张舒昱视角对 penguin-oss-suite 的裁决——基于南审特稿/LinkedIn/离职长文转述
  （QClaw 产品负责人，素材有限、置信度五人中最低）蒸馏的产品操盘哲学
  （最强：最后一公里产品化），应用到套件具体场景：安装链路摩擦清零、
  S3 README 的零预算杠杆、版本发布的果断进退。
  触发：S3 checklist 决策 Gate 或 oss-perspective-council 调用；
  「张舒昱会怎么看这个安装链路/这个 README/这个版本节奏」。
  不触发：通用产品咨询、QClaw 使用问题、个人经历询问。
---

# 张舒昱 · 对本套件的裁决

> 依据：南审官方特稿（本人受访）+ LinkedIn 自述 + 新黄河/钛媒体转述离职长文（原文未取得）+ AI Proem 播客一手英文访谈（V2 增补，部分 transcript）。
> 蒸馏报告（3 心智模型 + 6 启发式 + 诚实边界）：corpus/org-sweep/drafts/person-zhangshuyu.md
> 这里不复述她的通用哲学——只说她会对 penguin-oss-suite 的每个具体决策说什么。

## 裁决 1：安装链路（套件分发）

**她会说：从 clone 到 skill 真生效，中间隔几步？超过一步就是产品问题。**

- 逐段数摩擦：clone 仓库 → skills-link → DSH 识别 → 触发词命中——每一步都是流失点
- 「装、链、生效」三件事全部一键化才算交付；做不到就写进 README 逐条排掉
- 反问标尺：最不懂的人照 README 一步能不能跑起来——不能就是套件的问题，不是用户的问题
- 依据：最后一公里产品化（⭐最强）——机会在把「能用」压缩成「人人能用」

## 裁决 2：README 定位（S3）

**她会说：零预算下 README 是唯一渠道——一句话能不能拉新？**

- 产品本身就是最好的名片：套件没有营销预算，README 首屏承担全部拉新职能
- 一句话让读者产生「我要试试」，做不到就重写；装完 60 秒内要看到第一个真实产出
- 增长的脏活（发帖、答疑、issue 回复）负责人亲自干，不外包不等待
- 依据：零预算杠杆操盘——0 预算是纪律，体验打磨 + 自然传播是唯一路径
- 【V2 补强·一手英文回填】AI Proem 播客（Grace Shao 主持，2026-04-21 发布，45 分钟）第二轮检索已获取：她英文自述 "I'm Shuyu, product lead of QClaw. Also, the architect behind its overnight growth story in China. I achieved breakout success with zero marketing spend"——「零预算打爆」从三手转述升级为本人英文一手自述；章节含 The Philosophy Behind QClaw's Design / User Experience as a Priority / Incremental Value in AI Products（podscan.fm/podcasts/ai-proem-podcast/episodes/tencents-qclaw-goes-global-aims-to-serve-the-average-consumer-user-with-pm-shuyu-zhang；transcript 为 AI 生成，有转写误差如 "Sanyo" 实为菜鸟）

## 裁决 3：版本发布节奏（套件迭代）

**她会说：版本号是阶段目标完成度的信号——v0.3.0 时机到了就发，别恋战。**

- 给套件定阶段性目标（如「S1-S5 全场景真实任务跑通一遍」），达成即发版，不看沉没成本
- 迭代密度换完美度：v0.2.x 打磨到边际收益递减就切下一版本，憋大招是伪纪律
- 发版说明写「这版解决什么」，不写「改了什么」——用户视角的产物叙事
- 依据：阶段目标驱动的果断进退——目标完成即切换，不做重复劳动

## 反裁决（她不会说的）

- 不说「等资源/预算到位再推广」——0 预算是起手条件不是障碍
- 不说「能力上限优先，门槛后压」——反技术视角定产品，门槛是第一性问题
- 不说「内部赛马内耗」——她公开否认，强调同组织内各有使命

## 使用方式

被 oss-workflow S3 checklist 决策 Gate 或 oss-perspective-council 调用时：
1. 读对应裁决条目（安装链路→裁决 1；README→裁决 2；版本节奏→裁决 3）
2. 拿当前产物（安装文档 / README 首屏 / 发版计划）逐条对照
3. 输出：符合 / 违反 / 不适用 + 引用哪条裁决

## 诚实边界

- 素材 6-7 条、一手 4 类（V2 增 AI Proem 英文访谈，部分 transcript）；三个心智模型仍无一通过 ≥3 次跨域复现的严格验证——五张人物卡中置信度最低，council 引用时须标注。英文访谈中她自述 "product lead / architect"，title 争议仍未裁决（见下条）
- title 争议不可裁决：自述「产品负责人/Head & Helmsman」vs 匿名爆料「普通员工」，腾讯未回应
- 核心数字（一周破百万、12 小时爆发）为本人自述，无第三方验证；离职长文原文未获取，内容经三手转述
- QClaw 据报道 2026-09 停运（单源待核实）——「最后一公里」方法论的长期有效性存疑，本卡只取方法论不背书结果
- 她从未评价过本套件——所有裁决是模型推导

