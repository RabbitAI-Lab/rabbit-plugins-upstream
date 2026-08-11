# Examples

## 使用说明

本文件仅保存真实、脱敏并经过人工确认的路由案例。

## 案例一：单 Skill 即可解决

输入：

检查一份报价是否完整。

预期：

只推荐 QUOTE()。

## 案例二：客户意思不清并需要回复

预期路径：

INTENT_DECODE() → CLARIFY() → REPLY()

## 案例三：陌生产品询价

预期路径：

PRODUCT_BRIEF() → CLARIFY() → RFQ()

根据结果再决定是否进入 PRICE() 和 QUOTE()。

## 案例四：客诉退款

预期路径：

COMPLAINT() → RESPONSIBILITY() → RMA() → SOLUTION() → REPLY()

## 案例五：信息不足，应停止

当产品型号和需求范围均不明确时，应先停在 CLARIFY()，不得继续 PRICE() 或 QUOTE()。

## 案例六：避免过度编排

简单付款提醒只使用 PAYMENT()，不增加 KEYPOINT()、REPORT() 或 REPLY()。

## 案例七：明确周期性汇报

输入：

整理本月业务复盘和下月重点。

预期：

只推荐 MONTHLY_REPORT()，不增加 REPORT()。

## 案例八：汇报类型不明

输入：

帮我写个给领导看的汇报。

预期：

先推荐 REPORT() 做汇报类型、对象、目的和周期识别，不直接进入 DAILY_REPORT()、WEEKLY_REPORT()、MONTHLY_REPORT()、MIDYEAR_REPORT() 或 ANNUAL_REPORT()。

## 案例九：跨部门协同后对外回复

输入：

客户希望提前上线，销售想今天回复客户，但设计和技术都还没有确认。

预期：

先推荐 CROSS_FUNCTIONAL_COLLABORATION() 整理内部事实、待确认事项、过早承诺风险和协同文本；只有内部确认后，再进入 REPLY() 生成对外客户回复。

## 案例十：信息明确的请假申请

输入：

下周四和周五请假两天，工作已经安排同事覆盖，需要给直属主管发一条企业微信。

预期：

只推荐 UPWARD_COMMUNICATION()，不增加 REQUEST()、DECISION() 或 ESCALATE()。

## 案例十一：需要领导选择方案

输入：

项目发现两个高风险问题，可以按期上线并承担风险，也可以延期一周修复。需要经理决定并生成会议沟通提纲。

预期路径：

DECISION() → UPWARD_COMMUNICATION()

DECISION() 负责比较方案与风险，UPWARD_COMMUNICATION() 负责生成面向经理的最终沟通内容。

## 案例十二：重大问题升级后沟通老板

输入：

系统故障影响全部用户，已回滚但服务仍不稳定，需要老板协调供应商和客服资源。

预期路径：

ESCALATE() → UPWARD_COMMUNICATION()

不得编造根因、恢复时间或责任人。

## 案例十三：平级内部请求

输入：

请财务同事今天下班前提供上月付款记录。

预期：

只推荐 REQUEST()。沟通对象是平级职能部门且请求明确，不使用 UPWARD_COMMUNICATION()。

## 案例十四：潜在客户公开调查与匹配

输入：调查一家德国潜在客户的公开背景、合作风险和匹配程度。

预期路径：COMPANY_RESEARCH() → BUSINESS_RISK() → COMPANY_FIT()。只有用户还要求判断投入价值时，才继续 QUALIFY()。

## 案例十五：竞争市场到选品

输入：研究德国服务器备件市场，比较主要对手，并评估三个候选产品。

预期路径：MARKET_RESEARCH() → COMPETITOR_ANALYSIS() → PRODUCT_SELECTION()。

## 案例十六：主体冲突应停止

输入：调查 ABC Ltd，但未提供国家、域名或注册号，搜索结果存在多个同名主体。

预期：停在 COMPANY_RESEARCH()，请求主体识别线索，不进入 BUSINESS_RISK()。

## 案例十七：已有候选产品直接评估

输入：已有市场资料和三个候选产品，希望结合供应、资金、物流和售后能力决定先验证哪个。

预期：只推荐 PRODUCT_SELECTION()，不重复调用 MARKET_RESEARCH()。

## 案例十八：单独扫描重点客户动态

输入：对比上周以来客户官网和 LinkedIn 的变化，分类信号并更新监测状态，不需要写客户消息。

预期：只推荐 ACCOUNT_WATCH()。不得增加 OPPORTUNITY()、FOLLOWUP() 或 REPLY()。

## 案例十九：客户动态形成潜在商机并跟进

输入：客户官网公布新建数据中心项目，希望判断是否形成机会、安排跟进并准备客户消息。

预期路径：ACCOUNT_WATCH() → OPPORTUNITY() → FOLLOWUP() → REPLY()。ACCOUNT_WATCH() 只传递已确认项目、时间、来源、我方关联和信息缺口。

## 案例二十：缺少历史基线

输入：第一次检查客户最近有什么新动态，没有上次检查时间或历史记录。

预期：ACCOUNT_WATCH() 只执行基线或近期扫描，不得称为新增动态。

## 案例二十一：招聘和参展弱线索

输入：客户招聘采购经理并宣布参展，立即判断会采购并写销售消息。

预期：只使用 ACCOUNT_WATCH() 核验、分类和评估；不得直接进入 OPPORTUNITY() 或 REPLY()，除非出现明确项目、需求和合理联系窗口。

## 案例二十二：先判断 AI 实现方式

输入：我每天都要整理不同格式的客户资料，想做一个 Skill 或自动化，但不知道哪种更合适。

预期：先使用 AI_TASK_DIAGNOSIS() 澄清目标、变化频率、数据证据和最终责任。只有诊断为 WorkFn Skill 且需要编排多个现有 Skill 时，才继续 ROUTE()。

## 案例二十三：明确的一次性简单任务

输入：把这三条会议记录整理成待办。

预期：直接使用 MINUTES() 或普通对话，不增加 AI_TASK_DIAGNOSIS()。

## 案例二十四：从目标市场到人工搜索

输入：我们已有产品、供应能力和历史订单，希望判断先开发哪些市场，再形成目标客户画像和人工搜索词。

预期路径：MARKET_OPPORTUNITY() → TARGET_CUSTOMER_PROFILE() → SEARCH_STRATEGY()。生成搜索策略后停止，等待人工搜索结果，不直接进入 COMPANY_SCREENING()。

## 案例二十五：筛选候选公司并规划联系路径

输入：我已经人工整理了 20 家候选公司的名称、域名和 LinkedIn 链接，请先筛选；确认后再告诉我优先找哪个部门。

预期：先使用 COMPANY_SCREENING()。只有用户人工确认目标公司后，才进入 CONTACT_STRATEGY()；不得猜邮箱或自动发送外联。
