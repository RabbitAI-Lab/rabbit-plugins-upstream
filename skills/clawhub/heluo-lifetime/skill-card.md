## Description:

根据出生年月日时推算河洛理数本命卦、后天卦、大运和流年，并生成逐岁运势批断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[leahlu0124-creator](https://clawhub.ai/user/leahlu0124-creator)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill to request a Heluo-style life reading from birth information, including bazi or birth date, birthplace, and sex/gender. The agent uses bundled reference material and local scripts to calculate hexagram structures and present the result as a Markdown reading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for sensitive birth details, birthplace, and sex/gender.

Mitigation: Use only when the user intentionally requests this type of reading, collect another person's details only with consent, and avoid retaining or sharing the submitted personal details.

Risk: The generated readings can appear deterministic or gender-biased.

Mitigation: Frame outputs as historical fortune-telling or entertainment text rather than factual advice, and avoid presenting gendered predictions as objective truth.

Risk: The server security verdict is suspicious because of privacy and consent concerns, not because malicious behavior was found.

Mitigation: Review before installing and keep the skill limited to users who understand the nature of Heluo-style readings and the data they are providing.

## Reference(s):

- [河洛理数 · 本命卦完整算法](artifact/references/heluo-algorithm.md)
- [河洛理数 · 大运与流年算法](artifact/references/dayun-liunian.md)
- [河洛理数 · 先天换后天变换法](artifact/references/xiantian-houtian.md)
- [河洛理数 raw 文件索引](artifact/references/raw-index.md)
- [卷四索引数据](artifact/references/juan4_index.json)
- [爻辞数据](artifact/references/yaoci.json)
- [ClawHub skill page](https://clawhub.ai/leahlu0124-creator/skills/heluo-lifetime)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown life-reading with quoted source passages, plus JSON from local calculation scripts when run directly]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires birth time, birthplace, sex/gender, and either four-pillar bazi or a birth date; interpretation responses include an AI-generated entertainment disclaimer.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
