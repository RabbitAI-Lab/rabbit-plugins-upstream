---
platform: douyin
display_name: 抖音内容营销与生成内容补充
jurisdiction: mainland-china
official_policy_url: unknown
last_checked: 2026-08-10
status: partial
---

# 抖音营销与生成内容补充规则

## Source status

- Ingested from: user-supplied aggregate `douyin_rules.md` in `content-compliance-docs.zip`
- Claimed sources: 抖音规则中心、巨量星图帮助中心、抖音黑板报及媒体报道
- Verification status: The archive gives only root domains or source names, not a primary URL for each claim. Treat records as `unknown` until matched to the exact official page. Do not use the archive's governance counts as authoritative evidence.

## DY-MKT-001: 黑话烂梗和变体表达按语境治理

- Authority: unknown
- Status: unknown
- Surfaces: speech, caption, subtitle, image-text, comment, message
- Risk default: high
- Source: user-supplied aggregate citing a 2025-06-12 Douyin notice; exact official URL unknown
- Published or observed: 2025-06-12
- Verified: unknown
- Summary: 谐音、缩写、拆字、符号及图文组合若用于传播色情低俗、不良文化、污言秽语、群体对立或违法引流，可能被治理；正常词语及规范表达不应仅因词形被判违规。
- Notes: 不建立“敏感词即违规”模型。审查完整语义、目标对象、画面和导流目的，并把通过变体规避审核本身列为加重信号。

## DY-MKT-002: 站外交易和第三方软件引导

- Authority: unknown
- Status: unknown
- Surfaces: speech, caption, subtitle, link, qr-code, contact, app, store
- Risk default: high
- Source: user-supplied aggregate citing 巨量星图 content marketing rules; exact official URL unknown
- Published or observed: 2025-03-14
- Verified: unknown
- Summary: 营销内容不得通过联系方式、私下联系、站外平台、指定线下店铺或不明确交易渠道引导用户脱离平台交易，也不得以福利诱导下载或使用第三方软件。
- Notes: 资料包称一般性提及第三方应用与明确行动指令存在区别；具体账户、任务和组件权限发布前须在星图官方页面实时核验。

## DY-MKT-003: 强营销元素和联系方式

- Authority: unknown
- Status: unknown
- Surfaces: image, video, audio, logo, app-interface, link, qr-code, contact
- Risk default: high
- Source: user-supplied aggregate citing 巨量星图 review rules; exact official URL unknown
- Published or observed: 2026-08-10
- Verified: unknown
- Summary: 星图营销素材可能限制联系方式、微信号、二维码、外链、品牌标志、商品和应用界面的强营销露出，并关注营销素材是否破坏内容连续性及体验。
- Notes: 资料包包含“主体展示不超过总时长三分之一”等精确口径，但未给原始页面，因此该数字不得作为已核实规则使用。

## DY-MKT-004: 促销与抽奖真实性

- Authority: unknown
- Status: unknown
- Surfaces: speech, caption, subtitle, promotion, lottery, component
- Risk default: high
- Source: user-supplied aggregate citing 巨量星图 rules; exact official URL unknown
- Published or observed: 2026-08-10
- Verified: unknown
- Summary: 折扣、满减、优惠券、赠品和抽奖等营销信息应真实可核验；站内抽奖应使用允许的官方组件并按要求提交真实性材料，不得使用无法证明的促销和奖品诱导用户。
- Notes: 核对活动期限、库存、资格、奖品、领取条件和组件权限；不得使用虚假稀缺性或把互动作为隐蔽交易入口。

## DY-MKT-005: 效果对比和绝对化营销

- Authority: unknown
- Status: unknown
- Surfaces: speech, caption, image, video, before-after, testimonial, ad
- Risk default: high
- Source: user-supplied aggregate citing 巨量星图 high-frequency issues; exact official URL unknown
- Published or observed: 2026-08-10
- Verified: unknown
- Summary: 禁止或高风险情形包括普通食品宣称减肥或提高免疫力、过度夸张的使用前后对比、暴力测试和以“第一、最佳、国家级”等误导性绝对表达宣传商品。
- Notes: 涉及广告法时同时读取 `../laws/china-advertising.md`，不得把单词表机械当成法律结论。

## DY-MKT-006: 三品一械营销准入与未成年人

- Authority: unknown
- Status: unknown
- Surfaces: ad, product, image, video, live, component, minor
- Risk default: prohibited
- Source: user-supplied aggregate citing 巨量星图 rules; exact official URL unknown
- Published or observed: 2026-08-10
- Verified: unknown
- Summary: 保健食品、特殊医学用途配方食品、药品和医疗器械营销可能需要专项准入或特批，并受产品露出、组件和功效描述限制；未成年人不得参与其推广。
- Notes: 发布前核对产品类别、审查证明、账号行业准入和平台白名单；同时适用中国互联网广告规则。

## DY-MKT-007: 恶意营销号和批量低质生产

- Authority: unknown
- Status: unknown
- Surfaces: account, matrix, speech, image, video, audio, synthetic-media, interaction
- Risk default: prohibited
- Source: user-supplied aggregate citing a 2025 Douyin malicious-marketing campaign; exact official URL unknown
- Published or observed: 2025-04-01
- Verified: unknown
- Summary: 重点风险包括虚假人设、AI仿冒代言、批量诋毁企业、蹭热挑动对立、伪造权威身份、低俗涨粉卖号、虚假福利胁迫互动、虚构事件、工业化低质内容和黑灰产引流。
- Notes: 本条是治理模式汇总。对每项发现仍应引用可验证事实和更具体的核心规则，不能只给“像营销号”的主观结论。

## DY-MKT-008: AI生成内容披露与身份真实性

- Authority: unknown
- Status: unknown
- Surfaces: text, image, video, audio, virtual-person, live, product, metadata
- Risk default: high
- Source: user-supplied aggregate citing Douyin AI rules; exact official URL unknown
- Published or observed: 2025-09-01
- Verified: unknown
- Summary: 生成合成内容应使用平台提供的声明或标识功能；禁止借AI仿冒公众人物、专家或其他真实身份，生成虚假商品展示、测评、使用体验或夸大宣传，并禁止删除篡改标识。
- Notes: 法律层以 `../laws/china-advertising.md` 的 CN-AD-008 为准。资料包中的直播封禁、佣金冻结和治理数量未逐项核验，不作为确定处罚结论。

## DY-MKT-009: 营销处罚和时效

- Authority: unknown
- Status: unknown
- Surfaces: account, content, live, ecommerce, monetization
- Risk default: verify
- Source: user-supplied aggregate; exact official URL unknown
- Published or observed: 2026-08-10
- Verified: unknown
- Summary: 营销违规可能引发删除、限流、投稿或直播限制、健康分或商业权限影响、账号封禁及法律处置。
- Notes: 具体处罚受规则版本、账号类型、任务产品、违规次数和严重程度影响；不得向用户保证某种固定处罚或恢复期限。

## DY-MKT-010: 正常词汇与规避式表达

- Authority: unknown
- Status: unknown
- Surfaces: speech, caption, subtitle, image-text, comment, message
- Risk default: verify
- Source: user-supplied aggregate citing 抖音《规范表达沟通手册》 and `https://www.douyin.com/rule/bulletin`; exact article URL unknown
- Published or observed: 2026-08-10
- Verified: unknown
- Summary: “医院、药、血、胸、价格、微信、福利”等普通词汇不应脱离语境直接判违规；风险来自人身攻击、色情低俗、虚假医疗、违法营销、站外交易等完整含义和目的，也不应以谐音、缩写或符号刻意规避审核。
- Notes: 正常、准确表达优先于“敏感词替换”。“最、第一”等表达仍须先判断广告属性、所指对象、证据和语境，并按中国广告法律基线复核。
