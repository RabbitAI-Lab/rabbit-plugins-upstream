# 输入信息清单

## 使用原则

分析前先读取 `user-profile.md`。首次使用或当前上下文没有可用画像时，必须主动要求用户完成最小建档；不能把“用户可以补充”当成可选提醒。

信息越完整，判断越稳定；但不要因为缺少次要字段而拒绝分析。

当用户只提供链接时：

1. 识别链接是工作页、客户页还是用户自己的 Freelancer 主页；
2. 尝试读取链接；
3. 若工作页无法读取，请用户复制整页文本或上传连续截图，优先索取“工作页 + 客户历史 + Activity on this job”三块内容；
4. 若 Freelancer 主页无法读取，请用户复制 Profile、Skills、Portfolio、Work History 与评价，或上传连续截图；
5. 若当前上下文没有用户画像，优先从 Freelancer 主页、复制内容、截图、文字或口述建立画像；只有用户不方便提供时才展示模板；
6. 从现有内容生成画像草稿，并通过每轮最多 3 个问题确认核心技能、同类成果和最低报价。

## A. 工作本身

尽量提取：

- Job title
- Job description / Summary
- Scope、deliverables、deadline
- Required skills / preferred qualifications
- Experience level
- Fixed-price budget 或 hourly range
- Project length
- Hours per week
- Contract-to-hire / ongoing work
- Location、language、native speaker 要求
- Attachments
- Screening questions
- 所需 Connects
- 发布时间
- 计划雇佣人数
- 是否已显示 hired

## B. 客户基本信息与历史

尽量提取：

- Payment method verified
- Phone number verified
- Rating
- Reviews count
- Freelancer 留下的评论原文
- Jobs posted
- Hire rate
- Total hires
- Active hires
- Total spent
- Total hours
- Average hourly rate paid
- Member since
- Country / local time
- Company size / industry
- 过去相似岗位的预算、最终成交价格、评价
- 是否频繁重复发布同一工作
- 是否有大量未完成、低价或争议记录

## C. 当前竞争态势

尽量提取：

- Proposals：Less than 5 / 5–10 / 10–15 / 15–20 / 20–50 / 50+
- Interviewing
- Invites sent
- Unanswered invites
- Last viewed by client
- 已雇佣人数
- Boosted proposal 当前档位（若可见）
- 用户查看页面的当前时间

## D. 用户自身信息

这是个性化评分的必要输入，不是普通可选字段。首次使用必须主动收集；已有画像时可以复用。信息来源可以是用户的 Upwork Freelancer 主页、页面复制、截图、文字描述、语音口述或已保存画像。

先提取已有内容，不要求重复填写；不足部分用问答补齐。至少了解：

- 最相关的 3–5 项技能
- 是否有同类 Upwork 评价或项目
- 是否有可展示 Portfolio
- 可接受的最低净收入
- 可投入时间与时区
- 是否接受 Hourly Time Tracker
- 英语或目标语言沟通能力
- 本次目标：快速收入、长期客户、建立历史、提高单价或其他
- 对该工作“想接”的主观程度

## 用户画像不足时

- 没有画像但工作已触发诈骗、违法、站外付款、免费核心交付等硬性风险：可以直接避开，但个人匹配必须写“未评分”。
- 没有画像且个人能力可能反转结论：先完成最小建档，再给最终建议。
- 不得根据职位内容或用户语言猜测其能力。
- 不得给猜测性的个人匹配分；总分改为已知维度 `__/75` 或不计算。

## 缺失信息的处理

### 可以直接判断

以下信息即使不全，也可以直接避开：

- 要求先交钱、押金、保证金；
- 要求换汇、代收代付；
- 要求合同前站外付款；
- 要求免费完成核心工作；
- 明显违法、欺骗、账号租借或虚假身份；
- 已经明确 hired 且只招一人；
- 工作长期无人查看且竞争极高。

### 应追问的高价值字段

优先追问会改变结论的数据：

1. 发布时间 + last viewed
2. proposal / interview / invite
3. payment verified + hire rate + total spent
4. 预算 + 用户最低报价
5. 用户是否有同类案例

不要一次索取十几个字段。最多先问三个。
