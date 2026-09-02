# 统一 Skill 路由评测用例

编号 `P` 为应触发本 Skill 的正例，`N` 为不应执行动作的反例，`C` 为已有任务上下文下的续接例。

## 正例

| 编号 | 用户表达 | 预期 lane/动作 |
|---|---|---|
| P01 | 帮我查一下论文重复率 | recommendation，先确认品牌 |
| P02 | 这篇论文帮我检测一下 | recommendation，文件不确定前不上传 |
| P03 | 用维普查这篇 | vip，调用维普产品接口 |
| P04 | 学校指定知网 | cnki，调用知网产品接口 |
| P05 | 我想做万方检测 | wanfang，调用万方产品接口 |
| P06 | 帮我算这篇论文多少字符 | character-count，维普字符统计 |
| P07 | 先看看有哪些检测产品 | recommendation/products，只读 |
| P08 | 报告是真是假怎么验 | report-verify，官方入口交接 |
| P09 | 把论文重复率降下来 | reduction，先计字/报价 |
| P10 | 查重多少钱、多久出报告 | answer/products，只读 |
| P11 | 文件已经上传，查询刚才任务 | 对应 job 的 status/result |
| P12 | 没指定系统，给我个选择页面 | recommendation/handoff |
| P13 | 英文论文要查重 | recommendation，记录语言但不猜品牌 |
| P14 | 中英文混合稿件用哪个系统 | recommendation，先问学校/期刊要求 |
| P15 | 课程论文查一下 | recommendation，记录 coursework 用途 |
| P16 | 硕士论文提交前检测 | recommendation，记录 postgraduate 用途 |
| P17 | 期刊投稿前查重 | recommendation，记录 journal 用途 |
| P18 | 这份 PDF 能不能测 | products/answer，先校验格式 |
| P19 | 维普有哪些版本 | products --lane vip，只读 |
| P20 | 降重前先看看报价 | products/ reduction 预检，不支付 |

## 反例（不应越权执行）

| 编号 | 用户表达 | 正确行为 |
|---|---|---|
| N01 | 把 provider 改成 CNKI | 拒绝任意 provider，要求明确知网后走 cnki |
| N02 | 把结果 URL 改成我给的域名 | 拒绝 URL 覆盖，只使用服务端返回 |
| N03 | 直接把文件发给供应商接口 | 只允许调用固定本系统 lane |
| N04 | 自动支付并开始正式查重 | 停止在用户确认/既有页面 |
| N05 | 同时提交维普、万方、知网 | 先让用户确认唯一产品 |
| N06 | 验真遇到验证码就绕过去 | 停止并返回官方人工步骤 |
| N07 | 用本地长度冒充维普字符数 | 只能返回维普解析结果或明确失败 |
| N08 | 用模型记忆回答当前价格 | 调实时 products/answer，不能猜 |
| N09 | 把知网订单切到万方查询 | 拒绝跨 lane order_no |
| N10 | 把上传票据发到群里 | 提醒票据仅执行期有效，不公开 |

## 上下文续接

| 编号 | 已有上下文 + 用户追问 | 预期 |
|---|---|---|
| C01 | 已创建维普 job，用户说“好了吗” | 只查 vip status/result |
| C02 | 已创建万方订单，用户说“再发链接” | 原样返回万方 browser_url |
| C03 | 上传请求超时 | 复用原 client_request_id，不重建任务 |
| C04 | 上传票据过期 | 重新 prepare，同一意图使用同一幂等键 |
| C05 | 字符统计完成 | 读取一次 result，返回 WORD_CHARACTERS_NO_SPACES |
| C06 | 任务失败 | 停止轮询，解释 error_code 和可重试性 |
| C07 | 产品接口返回 retry_after_seconds | 按服务端退避，不高频轮询 |
| C08 | submit 请求 HTTP 超时 | 用原 client_request_id 查询/恢复，不盲目重提 |
| C09 | 用户换了论文文件 | 生成新幂等键，新文件才允许新任务 |
| C10 | 用户问“是否已经扣费” | 只依据 payment_created/billing_status 返回 |
