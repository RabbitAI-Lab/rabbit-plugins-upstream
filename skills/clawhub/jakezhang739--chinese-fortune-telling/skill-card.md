## Description:

Provides Chinese-language BaZi, Liu Yao, and Tarot workflows that run local calculation scripts and produce reflective divination readings with practical guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jakezhang739](https://clawhub.ai/user/jakezhang739)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask for reflective Chinese fortune-telling readings about birth charts, specific decisions, or tarot-style situations. The agent collects the required context, runs local scripts for charting or card data, and returns a concise Markdown interpretation with advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may provide birth details, gender, city, and personal divination questions.

Mitigation: Install only where the agent is permitted to process that user-provided personal context for local calculation and interpretation.

Risk: Divination readings could be mistaken for medical, legal, financial, or life-critical advice.

Mitigation: Present results as reflective or entertainment guidance and redirect high-stakes decisions to qualified professionals.

Risk: The skill produces primarily Chinese-language interpretations, which may limit reviewability for non-Chinese-speaking users or operators.

Mitigation: Have outputs reviewed by someone who can evaluate Chinese-language guidance and cultural context before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jakezhang739/skills/chinese-fortune-telling)
- [Persona and Style](artifact/references/persona-and-style.md)
- [BaZi Interpretation Framework](artifact/references/bazi-interpretation.md)
- [Liu Yao Interpretation Framework](artifact/references/liuyao-interpretation.md)
- [Tarot Interpretation Framework](artifact/references/tarot-interpretation.md)
- [Vendored lunar-javascript license](artifact/scripts/lib/lunar-LICENSE.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with local script outputs summarized into human-facing prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily Chinese-language output; local scripts may emit JSON for chart, hexagram, or tarot card data before interpretation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
