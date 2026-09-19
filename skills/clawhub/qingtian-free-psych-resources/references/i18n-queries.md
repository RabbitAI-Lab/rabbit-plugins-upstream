# 多语言支持：识别、搜索词、时区

## 1. 语言识别与回复规则

1. 检测用户输入语言（字符集/语种特征），映射到支持语言。
2. **回复语言 = 用户语言**；不确定时默认简体中文（可询问确认）。
3. **搜索语言 = 用户语言 + 目标国官方语言** 双轨并行。
4. 资源名展示：`原名（本地文字） + 当前语言翻译`，如「いのちの電話（生命热线）」。
5. RTL 语言（阿拉伯语、希伯来语）：注意文本方向与排版镜像。

**支持语言（≥12 种）**：简体中文、繁體中文、English、Español、日本語、한국어、Français、Deutsch、Português、Русский、العربية、Italiano、हिन्दी

## 2. 各国"免费心理支持"本地搜索词表

| 语言 | 搜索词 |
|---|---|
| 中文 | 免费心理咨询 / 免费倾诉 / 心理援助热线 / 免费树洞 / 危机干预热线 |
| English | free therapy / free counseling / mental health helpline / talk to someone free / crisis line |
| Español | terapia gratuita / línea de ayuda emocional / psicólogo gratis / hablar con alguien |
| 日本語 | 無料 こころの相談 / 無料カウンセリング / いのちの電話 / 悩み相談 |
| 한국어 | 무료 심리상담 / 무료 상담 / 자살예방 핫라인 / 마음건강 지원 |
| Français | psychologue gratuit / ligne d'écoute gratuite / soutien psychologique |
| Deutsch | kostenlose psychologische Beratung / Telefonseelsorge / Seelsorge |
| Português | terapia gratuita / linha de apoio emocional / apoio psicológico |
| Русский | бесплатная психологическая помощь / горячая линия доверия |
| العربية | استشارة نفسية مجانية / خط المساعدة النفسية |
| Italiano | terapia gratuita / linea di ascolto / sostegno psicologico |
| हिन्दी | मुफ्त मानसिक परामर्श / सहायता हेल्पलाइन |

## 3. 危机信号多语词表（危机判断用）

| 语言 | 触发词 |
|---|---|
| 中文 | 想死、结束生命、自杀、伤害自己、活不下去、坚持不住、已经计划好 |
| English | suicide, kill myself, end my life, self-harm, don't want to live |
| 日本語 | 死にたい、自殺、自分を傷つけたい、消えたい |
| 한국어 | 자살, 죽고 싶다, 자해 |
| Español | suicidio, quiero morir, hacerme daño |
| Français | suicide, veux mourir, me faire du mal |
| Deutsch | Suizid, will sterben, mir etwas antun |

规则：命中任一强信号 → 立即走危机优先协议；仅低落无信号 → 常规路径。命中后做温和确认（"听起来你现在很艰难……"），不做诊断式追问。

## 4. 时区与本地格式

1. 服务时段一律标注时区：`24/7（Asia/Shanghai）`、`每日 16:00–21:00（JST）`。
2. 用户所在地与资源时区不同时，换算并标注双方时间。
3. 号码保留本地拨号格式（如 `116 123`、`1-800-...`），跨境资源注明"仅限当地拨打/可能按国际长途计费"。
4. 日期格式跟随用户语言习惯（中：YYYY-MM-DD；美：MM/DD/YYYY；欧：DD/MM/YYYY）。

## 5. 多语言搜索命中

关键词匹配同时查 `name / nameLocal / nameTranslated / operator` 四个字段，保证中英日韩西语关键词都能命中同一条资源。
