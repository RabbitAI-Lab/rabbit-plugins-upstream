---
name: paper-check
description: 专业的综合论文查重与检测 Skill：回答维普、万方、知网产品选择、检索范围、检测原理、报告指标、结果差异、引用规范、AIGC 和学术诚信问题；也能按用户意图调用现有用户端接口完成字符统计、上传、建单和查询，并返回原用户端浏览器地址。不需要 MCP、登录或 API Key。用户提到论文查重、论文检测、重复率、文字复制比、相似比、降重、AI率/AIGC、维普/VPCS、万方、知网/CNKI、字符数、报告解读、报告真假、报告验真、真伪查询、报告编号在哪里、验证码怎么填或官方验真入口时使用。
metadata:
  version: "3.2.0"
---

# 论文查重综合 Skill

这是一个 Skill 包，不是新业务服务。Python 工具只是现有用户端接口的薄适配层：读取固定环境配置，调用用户端已经在使用的 REST 接口，使用接口返回的临时上传票据上传文件，再把订单号、支付页、进度页、报告页交给用户。不要新增后端 Controller、Service、数据库表、MCP Server 或独立界面。

## 目标与边界

- CQCCJY（员工 2）是当前默认和本轮验证目标；Fanyu（员工 77）保留同构配置，标记为 `config-only`，本轮不发布。
- 用户只需说需求并提供文件。不要要求用户理解员工 ID、域名、供应商密钥、OSS 对象键或上传票据。
- 每日新建任务上限、文件大小、扩展名、幂等和匿名来源限制由既有用户端/服务端执行；Skill 不绕过限制。
- 不自动支付、不提交银行卡/验证码、不伪造报告、不保证重复率或 AIGC 结果。
- 不接受用户覆盖 `--url`、provider、环境归属、员工归属或任意第三方网址。

## 目录与加载顺序

先读本文件，再按下表只读与问题相关的资料；需要调用接口时，再读取对应产品目录中的合约和流程。不要一次加载所有无关资料。

```text
paper-check/
├── SKILL.md
├── config.json                       # 公共安全/限制/环境开关
├── domains/
│   ├── cqccjy.json                    # 员工 2，当前环境
│   └── fanyu.json                     # 员工 77，配置但暂不部署
├── scripts/paper_check_client.py     # 唯一薄适配层（标准库，无 MCP）
├── assets/report-verify/              # 真实报告/验真页面截图片与位置标注（敏感字段轻度遮挡）
└── references/
    ├── common/                       # 查重、AIGC、智评、字符标准、异步、隐私、错误
    ├── character-count/              # 维普字符计算
    ├── vip/                           # 维普查重
    ├── wanfang/                       # 万方查重
    ├── cnki/                          # 知网查重
    ├── aigc/                          # AIGC 检测
    ├── reduction/                     # 论文降重/降 AIGC
    ├── report-verify/                 # 报告验真交接、字段教程与截图示例
    └── guidance/                      # 路由和答疑
```

## 知识加载路由

| 用户问题 | 必读资料 |
|---|---|
| “我该选哪个/学校用哪个/本科硕博怎么选” | `common/product-selection-playbook.md` + 对应品牌 `products-and-scope.md` |
| “检测范围有哪些/怎么检索/怎么判重复/连续多少字” | `common/retrieval-and-matching-principles.md` + 对应品牌 `products-and-scope.md` |
| “为什么两次/两家结果不同/学校比预检高” | `common/cross-system-differences.md` |
| “帮我看报告/这些指标什么意思/多少合格” | `common/report-interpretation.md` + 对应品牌 `products-and-scope.md` |
| “引用为什么标红/参考文献要不要删/怎么准备文件” | `common/preflight-checklist.md` + `common/professional-faq.md` |
| “AIGC 是什么/AI 率可信吗/怎么选 AIGC” | `common/aigc-knowledge.md` + `aigc/interpretation.md` |
| “字符数为什么不同/Word 字符数不计空格” | `common/character-count-standard.md` |
| “异步多久/为什么还没报告/要不要重提” | `common/async-workflow.md` + 对应 lane `workflow.md` |
| “报告真假/验真入口/报告编号在哪里/验证码怎么填/怎么复制编号” | `report-verify/contract.md` + `report-verify/browser-pages.md` + `report-verify/tutorial.md` |

产品代码、价格、格式、字符上下限、保留期和支付渠道属于动态事实，必须调用 `products` 或读取当前页面。官方资料用于解释产品定位和公开检索范围；具体订单的报告范围优先级更高。

## 意图路由

| 用户说法 | lane | 处理方式 |
|---|---|---|
| “这篇论文多少字/字符”“Word 字符数不计空格” | `character-count` | 固定走维普 PWP 解析；返回 `word_count`，不支付、不提交查重 |
| “维普查重/维普检测” | `vip` | 维普草稿 → 临时上传 → 完成上传 → 订单查询；支付/正式检测由用户端页面完成 |
| “万方查重/万方检测” | `wanfang` | 万方上传 → 建单 → 订单查询 |
| “知网查重/知网检测” | `cnki` | 知网上传 → 建单 → 订单查询 |
| “维普 AIGC/当前 AIGC 页面” | `aigc` | 先创建支付草稿；用户支付后再按订单票据上传并提交 |
| “万方 AIGC” | `wanfang` | 读取实时目录，选择万方 AIGC 产品代码后按万方流程建单 |
| “知网 AIGC” | `cnki` | 读取实时目录，选择知网 AIGC 产品代码后按知网流程建单 |
| “查 AI/AIGC/AI 率”但未指定品牌 | `guidance` | 先问审核方是否指定品牌；没有指定时展示实时可用产品及差异，不直接上传 |
| “论文降重/降 AIGC” | `reduction` | 降重草稿 → 原文（可选报告）上传 → 字符计数/报价；不自动开始改写 |
| “报告是真的吗/验真/真伪查询/官方入口/编号或验证码怎么填” | `report-verify` | 加载图文教程，识别品牌和检测类型，交接对应官方入口；不绕验证码、不直接判假 |
| “报告怎么看/重复率为什么不同/检索哪些库/引用为何标红” | `guidance` | 加载对应专业知识；只解释已有事实，不创建订单 |
| “多少钱、支持什么格式、多久出结果、隐私如何” | `guidance` | 读取实时公共配置 + common 知识，不能凭记忆编价格 |
| “帮我查重”未指明品牌 | `guidance` | 先问学校/期刊是否指定系统；没有指定时展示实时产品，不擅自猜测 |

用户同时指定多个品牌时，只询问最终要提交哪一个，不并行创建多个订单。

## 工具调用

运行目录为本 Skill 根目录：

```bash
python3 scripts/paper_check_client.py products --lane vip
python3 scripts/paper_check_client.py submit --lane character-count --file ./论文.docx
python3 scripts/paper_check_client.py submit --lane vip --file ./论文.docx --product-type dxs --title "论文标题" --author "作者"
python3 scripts/paper_check_client.py submit --lane wanfang --file ./论文.docx --product-code WF_UNDERGRADUATE --title "论文标题" --author "作者"
python3 scripts/paper_check_client.py submit --lane cnki --file ./论文.docx --product-code CNKI_UNDERGRADUATE --title "论文标题" --author "作者"
python3 scripts/paper_check_client.py aigc-draft
python3 scripts/paper_check_client.py submit --lane aigc --order-no <已支付订单号> --file ./论文.docx --title "论文标题" --author "作者"
python3 scripts/paper_check_client.py submit --lane reduction --file ./论文.docx --product-type smart_reduction --title "论文标题"
python3 scripts/paper_check_client.py status --lane vip --order-no <订单号>
python3 scripts/paper_check_client.py report --lane vip --order-no <订单号>
python3 scripts/paper_check_client.py verify                    # 首先返回 CQCCJY 统一验真入口和备用映射
python3 scripts/paper_check_client.py verify --brand cnki       # 仍首先交接 CQCCJY，再附知网备用页
python3 scripts/paper_check_client.py answer --question "支持哪些格式？"
```

`PAPER_CHECK_ENV` 仅由部署者设置为 `cqccjy` 或 `fanyu`，不是让终端用户选择的业务参数。未设置时使用 CQCCJY。所有接口和页面均来自 `domains/*.json`；脚本拒绝非 HTTPS 或用户自定义 URL。

## 文件、异步和页面交接

1. 先确认文件用途并取得用户同意；校验扩展名和 50 MB 上限。原始文件只在当前进程中读取，不写入 Skill 的长期目录。
2. 一次意图只创建一个订单。网络超时只能人工使用同一订单号查询，不能重新建单。
3. 上传接口返回的 OSS URL、STS、token 只用于当前请求，输出已脱敏；禁止把它们放进回答。
4. 提交/计数后不阻塞等待供应商。立即返回订单号、状态、`browser_urls.payment`、`browser_urls.progress`、`browser_urls.report`（如有）和 `next_action`。
5. 只有订单状态明确完成，并且 `report` 接口返回真实下载地址时，才填写 `report_download_url`。不得自行拼接下载文件地址。
6. 查询使用原订单号：`status` 查看异步状态；`report` 在完成后获取报告下载 URL。支付始终让用户在原页面操作。

## 固定输出契约

每次工具调用输出 JSON，至少包含：

```json
{
  "lane": "character-count",
  "environment": "cqccjy",
  "order_no": "...",
  "status": "PENDING_UPLOAD",
  "word_count": 12345,
  "browser_url": "https://vpcs.cqccjy.cn/pwp?...",
  "browser_urls": {
    "entry": "...",
    "payment": "...",
    "progress": "...",
    "report": "...",
    "report_download": "..."
  },
  "browser_action": "OPEN_BROWSER",
  "next_action": "..."
}
```

字段没有被接口返回时使用 `null`，不能猜测。对用户的说明要区分：字符解析、已创建未支付订单、已支付待检测、供应商处理中、报告完成。`word_count` 的含义固定是“维普解析字符数（不计空格）”，不是汉字数、英文单词数或重复率。

## 回答标准

- 字符统计：“按维普解析口径，这份文件的字符数（不计空格）是 X；本次没有支付，也没有正式提交查重。打开进度页：URL。”
- 查重建单：“已按【品牌】创建订单，当前状态【status】；请打开支付页完成支付，再在进度页查看异步处理。订单号【order_no】。”
- 报告：“报告下载地址只在服务端确认完成后返回；若暂未返回，请稍后用同一订单号查询。”
- 验真：“请先打开统一验真入口并按图文教程提交报告编号、题名（如页面要求）和验证码；当前 Skill 不绕过验证码，因此不能仅凭文件外观判定真伪。”所有品牌都先给出 `https://vpcs.cqccjy.cn/pwp/verify`，用户明确遇到统一入口不可访问时，才补充对应备用直达页。
- 价格、格式、时效、退款和保留期限以实时 `products`/`answer` 返回为准。

## 专业咨询标准

1. 先给明确结论，再解释依据和下一步；不要把产品宣传语堆给用户。
2. 产品推荐先服从学校、期刊或评审单位要求，再看论文类型，最后才比较实时价格与格式。
3. 解释检索范围时同时说明资源类型、联合库/自建库、时间边界和文件实际解析范围；报告显示范围是当前订单的最终事实。
4. 解释算法时区分“厂商公开说明”和“行业级原理”，不编造阈值、固定连续字数或内部权重。
5. 解读报告时使用报告原名，至少核对品牌版本、检测时间、检索范围、总体指标、章节/片段和主要来源；不创造统一合格线。
6. 讨论降重时以规范引用、独立论证和真实研究为目标，不提供隐藏字符、图片化文本、机械洗稿等规避方法。
7. 检测与 AIGC 结果都是风险线索，不直接下“抄袭”“代写”结论。

## 失败处理

说明具体阶段（配置、建单、预签名、上传、完成上传、计数、查询）和用户下一步。遇到 4xx 参数错误不要重试；遇到网络超时只查询原订单；遇到供应商异步失败停止轮询并保留订单号。不要展示异常栈、上传票据、临时凭证或文件正文。
