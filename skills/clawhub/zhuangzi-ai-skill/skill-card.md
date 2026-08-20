## Description:

莊子 AI helps agents create trilingual Traditional Chinese, Simplified Chinese, and English Zhuangzi philosophy dialogues, textual analyses, and import-ready JSON knowledge records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to build Zhuangzi-inspired dialogue, study aids, structured knowledge records, and evaluation workflows while preserving distinctions between historical evidence, textual tradition, interpretation, and creative imitation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dynamic evaluation can send confidential prompts or candidate outputs to the configured OpenAI-compatible judging provider.

Mitigation: Use dynamic evaluation only with approved providers and non-confidential inputs, or keep evaluation to reviewed local/static artifacts.

Risk: A risky sudo pip install suggestion could modify the host Python environment.

Mitigation: Install dependencies in an isolated virtual environment or other controlled runtime without sudo.

Risk: Philosophical reflection on medical, legal, financial, grief, or crisis topics could be mistaken for professional advice.

Mitigation: Treat Zhuangzi-style responses as supplemental reflection and defer high-risk decisions to qualified professionals or emergency support.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xuan905/skills/zhuangzi-ai-skill)
- [zhuangzi_knowledge.json](artifact/references/zhuangzi_knowledge.json)
- [zhuangzi_ai_test_cases.json](artifact/references/zhuangzi_ai_test_cases.json)
- [dazongshi_dynamic_smoke_report.json](artifact/references/dazongshi_dynamic_smoke_report.json)
- [Stanford Encyclopedia of Philosophy: Zhuangzi](https://plato.stanford.edu/entries/zhuangzi/)
- [Chinese Text Project: Zhuangzi](https://ctext.org/zhuangzi)
- [Internet Encyclopedia of Philosophy: Zhuangzi](https://iep.utm.edu/zhuangzi-chuang-tzu-chinese-philosopher/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance]

**Output Format:** [Plain text, Markdown, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include trilingual zh-Hant, zh-Hans, and en fields, classification tags, source notes, and evaluation reports.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
