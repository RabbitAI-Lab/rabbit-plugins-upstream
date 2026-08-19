# 小红书赛道深度分析引擎（XHS Track Analysis）

> 品牌进入品类/推新品/重做内容策略前，通过公开内容（笔记、达人主页、评论）看清四件事：**用户在问什么、平台内容怎样回答、谁在讲且谁更可信、用户到底信不信**，最终形成带证据边界的品牌建议。

## 一句话定位

不是市场规模估算，也不是平台算法逆向，而是把内容、达人和评论放在同一张桌面看的赛道判断方法。

## 架构

```
xhs-track-analysis/
├── SKILL.md                       # 入口（工作流 + 输出契约 + 诚实边界）
├── references/
│   ├── methodology.md             # 完整方法论（四分组、四排序、合并规则、达人路径、四行为）
│   ├── case-study.md              # 熟龄抗老赛道真实测试案例与数据
│   ├── table-template.md          # 赛道分析主表字段定义与样例
│   └── data-sources.md            # 真实数据获取路径、采集字段模板与质检清单
├── scripts/
│   ├── scaffold_table.py          # 一键生成空主表骨架（Markdown）
│   ├── collector/                 # 受监督有界采集器原型（B 方案）
│   └── integrations/              # 官方/第三方数据源接入骨架（A 方案）
└── README.md
```

## 工作流（Pass-by-Pass）

- **Step 0 定义问题**：三问——最想看懂什么？品牌要做什么选择？结论交给谁？
- **Step 1 关键词四分组**：人群与阶段 / 问题与效果 / 产品与选择 / 达人关联
- **Step 2 多排序采集**：每个关键词切 最新 / 最多点赞 / 最多收藏 / 最多评论 四种排序
- **Step 3 多轮合并去重**：同一笔记只留一份，但保留全部出现过的关键词与排序
- **Step 4 内容+达人分析**：区分"达人本人讲"与"第三方解读"，判断可信问题边界
- **Step 5 评论分析**：向往状态 / 追问选择 / 确认效果与风险 / 比较产品
- **Step 6 品牌建议 + 决策收敛**：GO / NO-GO / 条件GO + 找谁讲 + 讲什么角度

## 快速开始

```
# 生成空主表骨架
python3 scripts/scaffold_table.py "熟龄抗老" 赛道分析主表.md

# 发起分析
做一份小红书赛道分析：熟龄抗老
分析XX品类在小红书的内容生态，我们要进这个赛道
```

## 数据获取（真实数据从哪来）

本 Skill 是「分析方法 + 输出框架」，不含自动化采集器。真实数据通过以下路径注入：

- **浏览器插件 / 人工**：网页端按关键词 + 排序边看边采（仅公开页面）
- **第三方数据平台**：千瓜 / 新红 / 蝉妈妈 / 灰豚
- **官方商业平台**：蒲公英（达人/笔记/报价）、聚光（搜索词/行业大盘）

## 诚实边界

- 基于公开内容抽样，不代表全量用户；样本量与关键词覆盖决定结论上限
- 排序/重合观察不能反推平台算法
- 工具与流程不替代品牌策略判断
- 赛道分析有保质期：采集时间距分析 > 90 天的内容须标"需复核"
- 案例数据（熟龄抗老 + 董洁）为单品类测试（n=1），不可直接外推

## 来源

- 品牌归属：擎漫网络 | Qomob.AI

---

## License

MIT License

Copyright (c) 2026 擎漫网络 | Qomob.AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# 加入群聊

<div align="center">
  <img src="https://qomob.ai/xskill.jpg" width="600" alt="XSkill">
</div>
