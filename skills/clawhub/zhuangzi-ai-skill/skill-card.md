## Description:

莊子哲學與《莊子》文本的三語對談與 JSON 知識整理 skill。用於產生繁體中文、簡體中文及英文並列的莊子對談，分析生平、內篇／外篇／雜篇、核心概念與寓言，並將對談或知識內容整理為可匯入系統的結構化 JSON。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT-0

## Use Case:

External users, educators, students, and developers use this skill to create Zhuangzi-informed trilingual dialogue, structured JSON knowledge records, and evaluation material while keeping historical claims, textual interpretation, and creative imitation clearly separated.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dynamic evaluation can send candidate responses and test prompts through the configured OpenAI-compatible API.

Mitigation: Use dynamic evaluation only with an approved API configuration and review what prompts and responses will be sent before running it.

Risk: Evaluator setup may require Python package installation.

Mitigation: Prefer a virtual environment over privileged package installation before using the optional evaluation tooling.

Risk: Philosophical dialogue about grief, medical decisions, or crisis topics could be mistaken for professional support.

Mitigation: Preserve the skill's safety boundaries: use Zhuangzi-style reflection as a supplement and direct users to qualified, emergency, medical, or crisis support when appropriate.

## Reference(s):

- [ClawHub Skill Page: 莊子 AI](https://clawhub.ai/xuan905/skills/zhuangzi-ai-skill)
- [Zhuangzi Knowledge Base](references/zhuangzi_knowledge.json)
- [Zhuangzi AI Test Cases](references/zhuangzi_ai_test_cases.md)
- [Dazongshi Dynamic Smoke Report](references/dazongshi_dynamic_smoke_report.md)
- [Stanford Encyclopedia of Philosophy: Zhuangzi](https://plato.stanford.edu/entries/zhuangzi/)
- [Chinese Text Project: Zhuangzi](https://ctext.org/zhuangzi)
- [Chinese Text Project: Shiji Laozi-Han Fei Lie Zhuan](https://ctext.org/shiji/lao-zi-han-fei-lie-zhuan/zh)
- [Internet Encyclopedia of Philosophy: Zhuangzi](https://iep.utm.edu/zhuangzi-chuang-tzu-chinese-philosopher/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance and structured JSON with zh-Hant, zh-Hans, and en fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include import-ready dialogue records, source notes, classification tags, evaluation instructions, and optional evaluator command lines.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
