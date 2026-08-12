---
platform: wechat-channels
display_name: 微信视频号
jurisdiction: mainland-china
official_policy_url: unknown
last_checked: 2026-08-10
status: partial
---

# 微信视频号内容规则摘要

## Source status

- Ingested from: user-supplied aggregate `wechat_rules.md` in `content-compliance-docs.zip`
- Claimed sources: 微信视频号运营规范、直播行为规范、金融与健康科普准入标准、微信黑板报治理公告
- Verification status: The revised archive adds `https://weixin.qq.com/cgi-bin/readtemplate?t=weixin_agreement&s=video` as a candidate official operating-policy URL, but it could not be retrieved during this update and does not map every specialized claim. Dates, thresholds, qualification details, enforcement counts and penalty ladders remain unverified; every record below stays `unknown` until matched to primary text.

## WXCH-001: 违法有害和危害公共秩序内容

- Authority: unknown
- Status: unknown
- Surfaces: account, speech, text, image, video, audio, live, comment, message
- Risk default: prohibited
- Source: revised user-supplied aggregate citing candidate official URL `https://weixin.qq.com/cgi-bin/readtemplate?t=weixin_agreement&s=video`; live text unavailable
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止传播危害国家安全、泄露国家秘密、破坏统一和民族团结、邪教迷信、淫秽色情、赌博、暴力恐怖、教唆犯罪及扰乱社会秩序等违法有害内容。
- Notes: 涉及新闻事件、宗教、民族及公共安全时核对完整上下文和可靠信源，不用单个关键词替代判断。

## WXCH-002: 知识产权、名誉与隐私

- Authority: unknown
- Status: unknown
- Surfaces: account, profile, text, image, video, audio, live, comment, message, synthetic-media
- Risk default: high
- Source: user-supplied aggregate citing 微信视频号运营规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止冒充身份，或侵犯姓名名称、肖像、名誉商誉、隐私、商业秘密、著作权、商标权和专利权；偷拍、丑化、AI伪造及未经授权搬运同样需要审查。
- Notes: 发布前确认授权范围、素材来源和合理使用依据；身份证号、住址、联系方式、微信号等个人信息应删减或打码。

## WXCH-003: 不实信息、标题党和误导叙事

- Authority: unknown
- Status: unknown
- Surfaces: title, cover, speech, caption, subtitle, image, video, live
- Risk default: high
- Source: user-supplied aggregate citing 微信视频号运营规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止捏造、扭曲、隐瞒关键事实或将未经证实的信息包装为事实，也应避免惊悚极端标题、浮夸煽动、猎奇故事、炫富和快速赚钱叙事误导用户。
- Notes: 检查标题封面是否准确概括内容、素材是否过时、引用是否有可靠出处、剧情是否清楚标识。

## WXCH-004: 未成年人保护

- Authority: unknown
- Status: unknown
- Surfaces: speech, text, image, video, live, comment, message, ad, minor
- Risk default: prohibited
- Source: user-supplied aggregate citing 微信视频号运营规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止侵害或消费未成年人，包括性侵害、虐待体罚、校园霸凌、烟酒毒品、泄露隐私、婚育或厌学辍学宣扬以及利用未成年人进行恶俗表演。
- Notes: 同时检查评论区、直播互动、商业植入和潜在危险模仿；针对未成年人的广告另读 `../laws/china-advertising.md`。

## WXCH-005: 色情低俗和性暗示

- Authority: unknown
- Status: unknown
- Surfaces: speech, text, image, video, audio, live, interaction
- Risk default: prohibited
- Source: user-supplied aggregate citing 微信视频号运营规范及直播行为规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止衣着暴露、疑似裸体、聚焦隐私部位、性暗示话术音效道具、性挑逗动作、低俗游戏及露骨展示情趣用品等内容。
- Notes: 结合镜头距离、持续时长、动作、场景、音效和互动目的判断；医学、艺术或新闻语境也需采用必要且克制的呈现。

## WXCH-006: 卖惨、扮丑、恐怖猎奇与伪科学

- Authority: unknown
- Status: unknown
- Surfaces: title, speech, text, image, video, audio, live, marketing
- Risk default: high
- Source: user-supplied aggregate citing 微信视频号运营规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止或限制利用疾病、贫穷、未成年人或残障人士卖惨营销和道德绑架，刻意扮丑引起不适，以及传播恐怖灵异、风水运势、食物相克等无科学依据内容。
- Notes: 公益求助需要核实身份、事实、资金流向和授权，避免公开敏感个人信息或把打赏转入私人账户。

## WXCH-007: 低质、拼接和过时内容

- Authority: unknown
- Status: unknown
- Surfaces: title, text, image, video, audio, editing
- Risk default: medium
- Source: user-supplied aggregate citing 微信视频号运营规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 轮播大字、简单拼凑、严重模糊、内容残缺、音画无关、混剪杜撰名言和严重过时的信息可能被视为低质内容。
- Notes: 标明素材日期与出处，确保剪辑不改变原意，并为转载和二次创作取得必要授权。

## WXCH-008: AI生成、深度合成和剧情标识

- Authority: unknown
- Status: unknown
- Surfaces: text, image, video, audio, virtual-person, live, synthetic-media, metadata
- Risk default: high
- Source: user-supplied aggregate citing 微信视频号运营规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: AI生成、深度合成、虚拟现实和虚构剧情等非真实内容应按平台要求显著标识；禁止用AI伪造新闻、身份或商品体验，或用虚假摆拍不当营销。
- Notes: 同时适用 `../laws/china-advertising.md` 的 CN-AD-008；标识不能修复虚假、侵权、欺诈或违法广告。

## WXCH-009: 账号滥用、骚扰和垃圾营销

- Authority: unknown
- Status: unknown
- Surfaces: account, profile, post, comment, message, contact, matrix
- Risk default: high
- Source: user-supplied aggregate citing 视频号常见违规概览; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 多次发布违规内容、违规资料或私信骚扰，大量发布营销灌水低俗评论，无资质发布高风险内容和恶意留联系方式，可能导致账号级治理。
- Notes: 不推断固定处罚；结合频率、规模、目的、历史和具体内容记录风险。

## WXCH-010: 虚假营销、促销和效果承诺

- Authority: unknown
- Status: unknown
- Surfaces: speech, caption, subtitle, image, video, live, product, price, promotion, testimonial, ad
- Risk default: prohibited
- Source: user-supplied aggregate citing 视频号营销规则; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止虚构销量排行、权威背书、医护身份、价格、赠品、活动期限和使用效果，或以误导性绝对表达、伪造前后对比和非医疗产品医疗功效诱导交易。
- Notes: 涉商业推广同时读取 `../laws/china-advertising.md`；绝对化表达须结合广告属性和语境，不使用机械敏感词表。

## WXCH-011: 金融内容高风险边界

- Authority: unknown
- Status: unknown
- Surfaces: account, speech, text, image, video, live, product, link, contact
- Risk default: prohibited
- Source: user-supplied aggregate claiming 视频号金融行业公约; exact official URL unknown
- Published or observed: 2026-04-01
- Verified: unknown
- Summary: 资料包称平台限制违法荐股、具体买卖时机或价格建议、保本保收益、虚假内部消息、洗钱集资套现、虚拟币与数字藏品推广，以及以资料为饵导流外部交易。
- Notes: 生效日期和“八类黑名单”未由官方原文核验。发布前实时核查最新金融准入、职业认证和产品范围；不得向用户索取资金、验证码、助记词或远程控制设备。

## WXCH-012: 金融科普直播准入与风险披露

- Authority: unknown
- Status: unknown
- Surfaces: account, certification, live, speech, caption, product, risk-disclosure
- Risk default: high
- Source: user-supplied aggregate citing 视频号金融科普类直播准入标准; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 金融科普直播可能要求事先准入、本人真人出镜、职业或机构认证、真实身份与从业信息展示，并禁止账户出借、具体产品推荐、收益保证、行情定论、收益对比和外部引流。
- Notes: 资料包中的有效期、画面比例、岗位名称和固定提示语均需在官方入口实时核验，不作为已确认阈值。

## WXCH-013: 健康科普直播身份与准入

- Authority: unknown
- Status: unknown
- Surfaces: account, certification, live, speech, caption, medical
- Risk default: high
- Source: user-supplied aggregate citing 视频号健康科普类直播准入标准; exact official URL unknown
- Published or observed: 2025-06-19
- Verified: unknown
- Summary: 医疗健康科普直播可能要求事先准入、本人真人出镜，并显著展示医护人员真实姓名、任职资格或职称、执业证书编号及任职机构；账号不得租借共享。
- Notes: 日期、“四要素”及医院等级职称门槛尚未由官方页面核验。证件只通过平台官方入口提交，公开画面避免额外泄露身份证号、手机号等信息。

## WXCH-014: 健康科普、在线问诊和医疗营销

- Authority: unknown
- Status: unknown
- Surfaces: speech, caption, subtitle, image, video, live, comment, message, product, medical
- Risk default: prohibited
- Source: user-supplied aggregate citing 视频号健康科普类直播准入标准; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止科学性错误、单一症状下诊断、秘方神药和包治表述，禁止在线问诊、危险操作教学、血腥手术展示、医疗引流、普通食品保健品治病宣称，以及虚构人设情节诱导消费。
- Notes: 科普应说明适用条件、证据和就医边界，不收集真实病历或公开个案隐私；涉及具体机构、服务或药械推广时同时读取医疗广告法律规则。

## WXCH-015: 直播着装、动作与场景

- Authority: unknown
- Status: unknown
- Surfaces: image, video, live, clothing, movement, setting, interaction
- Risk default: prohibited
- Source: user-supplied aggregate citing 视频号直播行为规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止冒用制服、暴露透视或情趣化服饰，性挑逗动作、隐私部位互动、低俗游戏，以及利用床、卫生间、酒店等场景刻意营造暧昧性暗示。
- Notes: 资料包中的具体服装和舞种示例只作场景提示；最终根据整体呈现、镜头语言和性暗示目的判断。

## WXCH-016: 微短剧、影视搬运与盗版引流

- Authority: unknown
- Status: unknown
- Surfaces: title, text, image, video, mini-drama, link, qr-code, download
- Risk default: high
- Source: user-supplied aggregate citing 微信黑板报治理公告; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 微短剧不得渲染暴力血腥、低俗、迷信、毒品和违背伦理的不良导向；不得未经授权提供影视内容观看、搬运传播或引流至外部下载盗版资源。
- Notes: 资料包中的下架和账号处置数量未核验，不作为处罚预测；保留版权链和授权期限证据。
