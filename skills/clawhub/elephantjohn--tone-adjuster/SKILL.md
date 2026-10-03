---
name: tone-adjuster
display_name: 语气调节器
display_name_zh: 语气调节器
display_name_en: Tone Adjuster
description: This skill should be used when the user wants the same message rephrased in different tones — including phrases like "改委婉点", "说得不那么冲", "对上级该怎么说", "换个说法", "这话太生硬了", "make it sound nicer", "rephrase this more politely". It outputs five tone variants while keeping the underlying facts unchanged.
description_en: This skill should be used when the user wants the same message rephrased in different tones — including phrases like "make it more polite", "say it less harshly", "how should I tell my boss", "rephrase this", "this sounds too blunt", "soften the tone". It outputs five tone variants while keeping the underlying facts unchanged.
description_zh: 当用户要把同一段话换不同语气表达时使用，包括「改委婉点」「说得不那么冲」「对上级该怎么说」「换个说法」「这话太生硬了」等表达。本技能给同一件事的 5 档语气版本，事实不变只改包装。
version: "1.0.0"
category: 写作与沟通
agent_created: true
---

# 语气调节器

同一件事，**5 档语气**，你挑。

## 何时使用

- 「改委婉点 / 不那么冲 / 柔和一些」
- 「对上级该怎么说 / 对客户怎么说 / 对朋友怎么说」
- 「换个说法 / 帮我润色一下 / 这话太生硬了」

## 不适用场景

- 用户要的是内容改写（增删信息）→ 这是编辑，不是调语气
- 用户要翻译

## 核心方法

### 一个铁律

**事实、请求、底线三样不能变，只改包装。**

切完语气后，对方接收到的「实际信息」必须和原文一致。如果调整后把「我不同意」变成了「可能还有另一种考虑」，那就是篡改，不是调语气。

### 固定 5 档

| 档位 | 特征 | 适用 |
|---|---|---|
| 1 直白 | 最短，不加缓冲 | 熟人、内部、紧急 |
| 2 委婉 | 加缓冲词，先扬后抑 | 一般同事、初次沟通 |
| 3 正式 | 书面、完整、有称呼 | 邮件、对上级、对外 |
| 4 亲密 | 口语、有情绪、带玩笑 | 朋友、家人 |
| 5 幽默 | 用比喻或反讽化解 | 尴尬场合、破冰 |

### 每档必须标注

- 这档适合发给谁
- 这档可能踩的雷（哪个词可能冒犯人）

## 输出模板

```
【原文】xxx

1️⃣ 直白版：[内容]
   适合：xxx ｜ 风险：xxx

2️⃣ 委婉版：[内容]
   适合：xxx ｜ 风险：xxx

3️⃣ 正式版：[内容]
   适合：xxx ｜ 风险：xxx

4️⃣ 亲密版：[内容]
   适合：xxx ｜ 风险：xxx

5️⃣ 幽默版：[内容]
   适合：xxx ｜ 风险：xxx

【一句话】无论哪档，「[对方必须知道的核心信息]」都保留着。
```

## Few-shot 范例

### 例 1：原文「这个方案不行」

```
【原文】这个方案不行

1️⃣ 直白版：这个方案我不同意。
   适合：内部快速沟通 ｜ 风险：显得不合作

2️⃣ 委婉版：方向我理解，但有几个地方我担心落地会卡住，想再聊聊。
   适合：跨部门同事 ｜ 风险：对方可能觉得你在拖

3️⃣ 正式版：关于该方案，我认真评估后，认为在成本与工期两方面存在较大不确定性，建议进一步论证后再推进。
   适合：邮件、对上级 ｜ 风险：偏长，紧急场合不合适

4️⃣ 亲密版：兄弟，这方案我看了想哭，咱再想想？
   适合：好朋友 ｜ 风险：对不熟的人就是冒犯

5️⃣ 幽默版：这方案要是能成，我把键盘吃了。要不咱们先小范围试一把？
   适合：气氛紧张时破冰 ｜ 风险：对方可能觉得你不严肃

【一句话】无论哪档，「我认为这个方案不应按现状推进」这个核心信息都保留着。
```

## 兜底话术

- 如果原文本身含有侮辱、歧视性表达 → 不要调语气，直接指出：「这句话本身有问题，不是语气问题，我建议改成……」
- 如果用户没给原文，只给了场景 → 先问一句：「你想说的原话是什么？」不要凭空编。
- 如果用户说「越客气越好」→ 仍然给 5 档，但把第 3 档（正式）标为推荐档，并说明「再客气会显得疏远」。
