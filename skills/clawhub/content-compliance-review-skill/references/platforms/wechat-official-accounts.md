---
platform: wechat-official-accounts
display_name: 微信公众号
jurisdiction: mainland-china
official_policy_url: unknown
last_checked: 2026-08-10
status: partial
---

# 微信公众号内容规则摘要

## Source status

- Ingested from: user-supplied aggregate `wechat_official_account_rules.md` in `content-compliance-docs.zip`
- Claimed sources: 微信公众平台运营规范及运营中心、微信珊瑚安全、微信互选广告规范和公开治理公告
- Verification status: The revised archive adds several candidate first-party URLs. They could not be retrieved during this update, so their live text and mapping to individual claims remain unverified. Dates, case names, governance counts, qualification lists, penalties and recovery times are not treated as authoritative.

## WXOA-001: 违法有害、色情暴力与不良导向

- Authority: unknown
- Status: unknown
- Surfaces: account, article, title, text, image, video, audio, link, comment
- Risk default: prohibited
- Source: revised user-supplied candidate official URL `https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncement&key=11599305742Z0Q0a`; live text unavailable
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止违法有害、淫秽色情低俗、暴力恐怖迷信、侵权盗版、违反公序良俗及严重污染社会风气的内容。
- Notes: 资料包所称“三条一键永久封禁红线”及具体处罚需要官方原文核验；审查应指出具体内容和规则风险，不保证固定处罚。

## WXOA-002: 低创作度、搬运、抄袭和虚构依据

- Authority: unknown
- Status: unknown
- Surfaces: article, title, text, image, citation, data, source
- Risk default: high
- Source: revised user-supplied candidate official URL `https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncement&key=11697600328G0Tbo`; live text unavailable
- Published or observed: unknown
- Verified: unknown
- Summary: 高频同质化、重复翻炒、轻微改写搬运、洗稿重组、机械拼接、图文失配和引用不存在的数据案例，可能被认定为低创作度或低价值内容。
- Notes: 增加真实分析不等于获得原作授权；分别检查原创性、版权、事实依据和引用标注。

## WXOA-003: AI辅助、自动化生产与事实核验

- Authority: unknown
- Status: unknown
- Surfaces: article, text, image, audio, video, synthetic-media, publishing, account
- Risk default: high
- Source: user-supplied aggregate citing a 2025 微信AI自动化创作治理声明; exact official URL unknown
- Published or observed: 2025-04-01
- Verified: unknown
- Summary: AI生成、改写、拼接、搬运和脚本批量发布若脱离真实创作者表达、缺少披露或制造事实错误和虚构数据，可能被治理。
- Notes: 不把“使用AI”本身等同违规。应保留人工编辑与事实核验，按平台要求声明AI辅助，并同时适用 `../laws/china-advertising.md` 的 CN-AD-008。

## WXOA-004: 原创声明不得用于搬运或洗稿

- Authority: unknown
- Status: unknown
- Surfaces: article, text, image, originality-label, citation
- Risk default: high
- Source: user-supplied aggregate citing 微信公众平台原创声明规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 未经授权搬运、大篇幅整合、抄袭和以同义词替换或调序方式洗稿的内容，不得滥用原创声明。
- Notes: 资料包中的月度治理数量未核验；引用应必要、适量、明确标注且符合法律和授权要求。

## WXOA-005: 知识产权、名誉、商誉与隐私

- Authority: unknown
- Status: unknown
- Surfaces: article, title, text, image, video, audio, link, personal-data
- Risk default: high
- Source: user-supplied aggregate citing 微信公众平台治理公告; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止盗版传播和未经授权提供影视资源，禁止捏造或混杂未经证实信息损害个人或企业名誉商誉，并禁止泄露姓名、肖像、联系方式等隐私和个人信息。
- Notes: 负面报道应有可靠信源、公共利益和必要限度；涉及个人信息先取得适当授权并最小化展示。

## WXOA-006: 外部导流和交易安全

- Authority: unknown
- Status: unknown
- Surfaces: article, profile, menu, auto-reply, message, link, qr-code, contact, mini-program
- Risk default: high
- Source: user-supplied aggregate citing 微信公众平台导流规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 以不完整内容、二维码、联系方式、外链或多重跳转为主要目的，引导用户到私人账号、第三方平台或不透明交易场景，可能构成违规导流并增加骚扰和交易风险。
- Notes: 区分平台允许的正常功能与规避监管的引流。不得要求用户提供验证码、付款密码、身份证照片或开启远程控制。

## WXOA-007: 诱导分享、点赞和关注

- Authority: unknown
- Status: unknown
- Surfaces: article, image, menu, auto-reply, message, link, interaction, reward
- Risk default: high
- Source: revised user-supplied candidate Tencent support URL `https://kf.qq.com/faq/161221VJBFbq161221bMfmim.html`; live text unavailable
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止用实物、积分、信息或其他奖励强制或诱导用户分享朋友圈、点赞或关注公众号，并不得通过菜单、自动回复和外链变相实施。
- Notes: 正常提醒关注或分享是否允许取决于文案、强制性、奖励和功能场景；发布前核查平台最新产品规范。

## WXOA-008: 纯营销、隐形广告与真实性

- Authority: unknown
- Status: unknown
- Surfaces: article, title, text, image, video, link, promotion, ad, sponsorship, affiliate
- Risk default: high
- Source: user-supplied aggregate citing 微信推荐与互选广告规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 缺少实际信息价值的纯营销、虚假宣传和隐瞒商业关系的推广具有高风险；折扣、价格、效果、资质和用户评价必须真实可证。
- Notes: 出现委托、赞助、佣金或购买路径时同时读取 `../laws/china-advertising.md`，核对广告可识别性和审查要求。

## WXOA-009: 金融欺诈、不实承诺和无资质营销

- Authority: unknown
- Status: unknown
- Surfaces: account, article, title, text, image, video, link, contact, financial-product
- Risk default: prohibited
- Source: user-supplied aggregate citing 关于金融类违规营销内容的规范; exact official URL unknown
- Published or observed: 2022-07-13
- Verified: unknown
- Summary: 禁止高收益理财欺诈、有偿荐股、虚拟币等致富骗局，禁止明示暗示保本无风险或保证收益，禁止借监管审核备案暗示政府背书，金融业务名称和营销可能要求相应资质。
- Notes: 资料包中的产品禁投清单和资质材料未由官方原文核验。不得替用户操作资金、收集账户密码、验证码或私钥。

## WXOA-010: 医疗、药品和器械广告资质

- Authority: unknown
- Status: unknown
- Surfaces: account, article, text, image, video, link, product, medical, ad
- Risk default: prohibited
- Source: user-supplied aggregate citing 微信互选广告规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 医疗机构、药品、医疗器械、保健食品等广告可能要求法定广告审查文件、产品注册备案和平台行业资质，未经审查或超出审查内容不得发布。
- Notes: 平台材料清单可能变化；法律底线以 `../laws/china-advertising.md` 的 CN-AD-005 与 CN-AD-007 为准，只通过官方入口提交证件。

## WXOA-011: 普通产品医疗用语与医护形象

- Authority: unknown
- Status: unknown
- Surfaces: article, title, text, image, video, product, testimonial, ad
- Risk default: prohibited
- Source: user-supplied aggregate citing 微信互选广告审核规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 非医疗产品或服务不得用治疗治愈、疗程、医学证明等表述制造医疗混淆，也不得冒用医生护士身份、医护服饰或医疗机构形象进行权威背书。
- Notes: 不用资料包的词表机械判违规；结合产品类别、广告属性、完整语义和证据判断，科研场景授权也不能支持虚假功效。

## WXOA-012: 护肤彩妆资质和功效承诺

- Authority: unknown
- Status: unknown
- Surfaces: article, text, image, video, product, before-after, testimonial, ad
- Risk default: high
- Source: user-supplied aggregate citing 微信互选广告审核规范; exact official URL unknown
- Published or observed: unknown
- Verified: unknown
- Summary: 化妆品推广可能要求注册备案材料；对祛斑、去皱、去眼袋等不可逆问题作“消除、根治、不反弹”等保证性承诺或伪造前后对比具有高风险。
- Notes: 核对产品实际类别、功效评价、备案宣称、对比条件和个体差异；普通化妆品不得宣称疾病治疗。

## WXOA-013: 广告流量作弊和诱导点击

- Authority: unknown
- Status: unknown
- Surfaces: account, article, layout, ad-slot, click, traffic, monetization
- Risk default: prohibited
- Source: revised user-supplied candidate official URL `https://ad.weixin.qq.com/guide/1194`; live text unavailable
- Published or observed: unknown
- Verified: unknown
- Summary: 禁止技术或人工制造虚假曝光点击、委托第三方刷量、恶意诱导点击、遮挡或改造广告位、空白文和以违规导流获取广告收入。
- Notes: 资料包中的一级二级三级处罚和资金扣除口径未核验；不要使用未知刷量服务，也不要向第三方交出公众号管理员权限或支付账户。

## WXOA-014: 虚假摆拍、伪科学和低俗引流

- Authority: unknown
- Status: unknown
- Surfaces: title, article, text, image, video, audio, synthetic-media, marketing
- Risk default: high
- Source: user-supplied aggregate citing 2025治理公告; exact official URL unknown
- Published or observed: 2025-01-01
- Verified: unknown
- Summary: 禁止以悲惨或职业人设虚假摆拍卖货，用换脸换声等方式伪造新闻，以科普名义传播医学经济等专业谣言，或以低俗搭讪、软色情、迷信和快速致富话术诱导互动交易。
- Notes: 剧情标识不能修复冒充、诽谤、欺诈和违法营销；专业内容需可靠信源与资质边界。

## WXOA-015: 敏感词与处罚不得机械推断

- Authority: unknown
- Status: unknown
- Surfaces: title, article, text, image-text, account, enforcement
- Risk default: verify
- Source: user-supplied aggregate containing a sensitive-word list and penalty ladder; exact official URL unknown
- Published or observed: 2026-08-10
- Verified: unknown
- Summary: “最、第一、国家级、治疗、收益”等词只能作为触发人工复核的线索，不能脱离广告属性、行业、语境、事实依据和平台版本直接判定违规；处罚也不能按固定天数推断。
- Notes: 资料包所称“平均恢复20+天”无可核验官方依据，已排除。绝对化广告用语按 `../laws/china-advertising.md` 的 CN-AD-003 审查。
