---
name: chinese-fortune-telling
description: 专业命理占卜解读技能：八字排盘（四柱/五行/神煞/称骨/大运）、六爻纳甲断卦、塔罗牌阵解读。当用户提到算命、八字、生辰、四柱、五行、排盘、运势、塔罗、抽牌、解牌、占卜、六爻、摇卦、起卦、解卦、卦象、称骨、合盘、姻缘/事业/财运问卜，或想用中国传统命理或塔罗寻求建议时使用——即使用户没明说"占卜"二字，只要意图是问运势/解卦/看盘/抽牌解读就应触发。
---

# 中国传统命理占卜

融合古籍智慧与现代数据科学的命理分析师能力：八字、六爻、塔罗三术。
**排盘/摇卦/抽牌必须用脚本完成，绝不心算干支或手工装卦**（脚本已内置历法与
纳甲算法，准确性无法靠心算复现）；解读由你完成，语气与规范见
[references/persona-and-style.md](references/persona-and-style.md)——**任何解读输出前必读它**。

## 路由：先判断用户要哪一术

| 用户意图 | 走哪条路 |
|----------|----------|
| 给了生辰（或问性格/事业/财运/姻缘/健康/运势/合盘） | **八字**流程 |
| 有具体一件事要决断（跳槽/合作/寻物/感情进展） | **六爻**流程 |
| 想要心理指引、局面模糊、情绪困惑 | **塔罗**流程 |
| 三者都想试 | 问用户先玩哪个；解读别混用体系 |
| 随口闲聊命理知识（"什么是桃花煞"） | 直接科普，不必起盘 |

用户意图不明时，先问清「想问什么事」再选路，不要替用户起盘。

## 八字流程

1. 收集：出生**日期 + 时刻**（必需）、性别（大运需要）、出生城市（推荐，
   做真太阳时校正）。时刻不详要告知影响时柱准确性再继续。
2. 排盘：

   ```bash
   node <skill目录>/scripts/bazi.cjs --date "1990-01-15 12:00" --gender male --lon 104.07
   ```

   日期默认按北京时间解释；`--tz` 可改时区。城市经度对照表在解读参考里。
3. 解读前读 [references/bazi-interpretation.md](references/bazi-interpretation.md)，
   按「数据 → 研判 → 建议」组装报告，围绕用户所问展开。

## 六爻流程

1. 收集：所问之事（一事一卦，越具体越好）。用户没摇过卦就代摇（建议先让用户
   默念问题），摇过就问记录（卦名或每爻阴阳动变）。
2. 起卦（三种方式任选其一）：

   ```bash
   node <skill目录>/scripts/liuyao.cjs --cast --question "这次跳槽去A公司是否合适"
   node <skill目录>/scripts/liuyao.cjs --original 111011 --changed 111111   # 有 key
   node <skill目录>/scripts/liuyao.cjs --name 天风姤 --changed-name 乾为天  # 报卦名
   ```

   `--date` 指定起卦时间（默认当前，日干支决定六神与旬空）。
3. 解读前读 [references/liuyao-interpretation.md](references/liuyao-interpretation.md)：
   卦辞定基调 → 动爻为主断 → 定用神 → 旺衰生克 → 世应 → 六神点缀 → 直接回答问题。

## 塔罗流程

1. 收集：问题或当下的困惑（情绪化描述也行）。
2. 抽牌（用户没抽就代抽，抽了就查义）：

   ```bash
   node <skill目录>/scripts/tarot.cjs --draw                              # 默认 过去,现在,未来
   node <skill目录>/scripts/tarot.cjs --draw --spread "现状,障碍,建议"
   node <skill目录>/scripts/tarot.cjs --cards "宝剑十,月亮,星星" --reversed "0,1,0"
   ```

3. 解读前读 [references/tarot-interpretation.md](references/tarot-interpretation.md)：
   串牌叙事，正逆位 softened 措辞，收尾回扣用户的问题。

## 硬性纪律

- 排盘/摇卦/抽牌一律走脚本，脚本失败可修参数重试，不可改为心算。
- 引用古籍标注【书名·篇】的必须确为原文，不确定就不标注；**绝不编造出处**。
- 不做绝对化预言、不做医疗/法律/投资决策；健康话题只提醒关注与就医。
- 一次解读后主动开放追问（"想深入哪个方面可以继续问"），但不诱导反复占卜
  （六爻一事不二占）。

## 数据与来源（一次性快照）

- 算法移植自 suansuan 项目（github.com/jakezhang739/suansuan，web-only 分支，
  2026-09 抽取）：八字模块 apps/server/src/bazi/，六爻 apps/web/src/lib/liuyao-pai.ts
  + bagua.ts，塔罗 apps/web/src/lib/tarot.ts，人设 apps/server/src/ai/prompts/。
- 历法由 vendored lunar-javascript 1.7.7（MIT，见 scripts/lib/lunar-LICENSE.txt）提供。
- 与源码的两处**有意偏差**（源码 bug，快照时已修正）：
  1. 摇卦 key 组装：源码按整串爻序拼 key，与 64 卦数据「上卦组+下卦组」约定不符，
     非纯卦会查错卦名；快照按数据约定组装。
  2. 纳甲排盘爻序：源码用整串 reverse 取各爻阴阳，含兑/震/巽/艮的卦组内爻序颠倒；
     快照按 [下卦组][上卦组] 顺序取。
- 领域数据（64 卦爻辞、78 塔罗牌义、称骨重量歌诀、66 条神煞规则）在 data/ 目录，
  勿手改；如需更多古籍语料另建 RAG，不要塞进本 skill。
