# 资源信息模型（Schema）与输出模板

## 0. 四大分类（category）

技能资源按四大类组织，每条资源必填 `category`；原有 10 类作为 `type` 子类保留：

| category | 含义 | 对应 type（子类） |
|---|---|---|
| counseling ① 免费心理咨询 | 专业/准专业咨询（含咨询师详情） | platform_free、ngo、gov_program、school、eap |
| vent ② 免费心理倾诉 | 非专业情绪支持与倾听 | support_helpline、text_chat、peer_support |
| ai ③ 免费心理AI | AI 陪伴/自助工具（标注非专业） | ai_tool |
| assessment ④ 免费心理测评 | 心理量表自评与报告生成 | assessment（模块内 19 量表） |

**type 10 类**：① crisis_helpline 危机热线 ② support_helpline 倾诉热线 ③ text_chat 文字聊天 ④ platform_free 平台免费通道 ⑤ ngo 公益项目 ⑥ gov_program 政府项目 ⑦ school 学校咨询 ⑧ eap 企业 EAP ⑨ peer_support 同伴互助 ⑩ ai_tool AI 工具
（注：crisis_helpline 按内容归入 counseling 或 vent 类，危机性用 crisisCapable 字段表达；评估类资源 category=assessment）

## 1. 资源字段字典（Resource）

| 字段 | 必填 | 说明 | 示例 |
|---|---|---|---|
| id | 是 | 唯一 ID：{地区}-{机构}-{序号} | cn-12356 |
| name | 是 | 中文/当前语言名 | 全国统一心理援助热线 |
| nameLocal | 是 | 本地语言原名 | 12356 |
| category | 是 | counseling / vent / ai / assessment | vent |
| countryRegion | 是 | 国家/地区 | 中国（全国） |
| type | 是 | type 10 类之一（见第 0 节） | crisis_helpline |
| operator | 是 | 运营机构 | 国家卫生健康委 |
| operatorType | 是 | government / ngo / nonprofit / commercial_free | government |
| costPolicy | 是 | 免费范围；潜在收费必须显式 | 免费；市话费自理 |
| paidUpgrade | 否 | 付费升级说明 | 无 |
| durationPerSession | 否 | 单次时长；缺失标"视服务而定" | 约 20–30 分钟 |
| hours | 否 | 服务时段 | 24/7 |
| timezone | 否 | 时区 | Asia/Shanghai |
| languages | 是 | 支持语言数组 | ["zh"] |
| eligibility | 否 | 人群限制；缺失标"无明确限制" | 面向全国居民 |
| methods | 是 | phone/sms/webchat/video/email/in_person | ["phone"] |
| bookingRequired | 否 | 是否需预约 | false |
| bookingUrl | 否 | 预约入口 | null |
| anonymity | 否 | 匿名性说明 | 匿名；不显示来电号码 |
| crisisCapable | 是 | 是否处理危机 | true |
| contact | 是 | tel:/sms:/https: 联系 | tel:12356 |
| source | 是 | 来源 URL（官方优先） | https://www.gov.cn/... |
| verifiedAt | 是 | 核验日期 YYYY-MM-DD | 2026-09-16 |
| status | 是 | verified / pending / expired | verified |

## 2. 咨询师/志愿者字段字典（Counselor）

| 字段 | 必填 | 说明 |
|---|---|---|
| id / name | 是 | 唯一 ID / 姓名或花名 |
| realNameDisclosed | 否 | 是否公开真实姓名（默认 false） |
| qualification | 是 | 资质/受训情况（如"国家二级心理咨询师""受训倾听志愿者"） |
| organization | 是 | 所属机构 |
| methods | 是 | 咨询方式数组 |
| languages | 是 | 语言 |
| availableHours | 否 | 可预约时段（含时区） |
| durationPerSession | 否 | 单次时长 |
| costPolicy | 是 | 费用政策（免费范围必须明确） |
| specialties | 否 | 专长领域数组 |
| bookingUrl | 否 | 预约入口 |
| verifiedAt / status | 是 | 核验日期与状态 |

## 3. 资源卡片输出模板

```
【名称】全国统一心理援助热线（12356）
├ 类型：危机热线 | 地区：中国（全国） | 核验：已核验（2026-09-16）
├ 运营机构：国家卫生健康委（政府）
├ 费用：免费；市话费自理（无付费升级）
├ 单次时长：约 20–30 分钟
├ 时段：24/7（Asia/Shanghai）
├ 语言：中文 | 适用人群：面向全国居民
├ 方式：电话 | 预约：无需预约，直接拨打
├ 匿名性：匿名，不显示来电号码
├ 危机能力：处理自杀预防
├ 联系：tel:12356
└ 来源：https://www.gov.cn/...（核验日期 2026-09-16）
```

## 4. 咨询师卡片输出模板

```
【姓名/花名】小树（志愿者花名）
├ 资质：国家二级心理咨询师 / 受训倾听志愿者
├ 所属机构：XX 公益心理服务中心
├ 咨询方式：文字聊天 / 视频 / 电话 / 面对面
├ 语言：中文、英语
├ 可预约时段：周一至周五 19:00–22:00（Asia/Shanghai）
├ 单次时长：50 分钟（免费）/ 20 分钟（热线）
├ 费用政策：本项目全程免费，无附加收费
├ 专长：焦虑、学业压力、情感困扰、LGBTQ+ 友善
├ 预约入口：https://...（或"见机构官网"）
└ 核验状态：已核验（来源：机构官网，2026-09-16）
```

## 5. 核验状态徽章

- 已核验 verified：来源 URL + 核验日期齐全 → 绿色徽章
- 待核验 pending：有数据无官方来源 → 黄色徽章，注明"请以官方为准"
- 已失效 expired：核验时发现变更/停用 → 红色徽章 + 给出现行替代

## 6. 排序规则

1. 危机状态 → 仅危机资源（T0→T1→T2→T3）
2. 常规状态按综合分降序：地区匹配（用户所在地+30）→ 24/7 可用（+20）→ 语言匹配（+15）→ 免费程度（完全免费+10）→ 核验状态（已核验+10）
3. 用户指定排序（综合/24h/本地/费用）时按指定方式

## 7. 空结果处理

无匹配资源时输出：① 放宽筛选建议（去掉 1-2 个条件）② 就近危机热线兜底 ③ 全球目录链接（Find A Helpline 等）④ 提示可尝试其他语言/方式。
