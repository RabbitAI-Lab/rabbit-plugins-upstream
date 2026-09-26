## Description:

五十年阅历的算命老师傅，八字紫微算人、六爻算事

This skill is ready for commercial/non-commercial use.

## Publisher:

[william22820785-cmyk](https://clawhub.ai/user/william22820785-cmyk)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users use this skill for traditional-culture fortune-telling style consultations about personal fate, relationships, career, timing, and specific questions. It guides an agent to collect the required context, run bundled BaZi, Zi Wei, Liuyao, and Qimen calculation tools, and produce concise Chinese consultation responses with stated boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for birth date, birth time, birthplace, gender, and private personal questions.

Mitigation: Avoid providing sensitive details you would not want processed by the host AI platform, and review any generated local files before sharing or retaining them.

Risk: Traditional-culture interpretation could be mistaken for professional advice.

Mitigation: Treat outputs as entertainment or cultural interpretation, not as medical, legal, financial, or investment advice.

Risk: The skill runs local Python and Node scripts and creates local result files and diagram images.

Mitigation: Review and scan the skill before deployment, and inspect created artifacts in the local workspace when handling sensitive consultations.

## Reference(s):

- [Skill page](https://clawhub.ai/william22820785-cmyk/skills/skill)
- [README](README.md)
- [Paid consultation standard](references/paid-consultation-standard.md)
- [Interpretation method](references/interpretation-method.md)
- [Liuyao method](references/liuyao-method.md)
- [Diagram display rules](references/diagram-display.md)
- [mingyu-core upstream](https://github.com/Brhiza/mingyu)
- [@aceworld/liuyao-algorithm upstream](https://github.com/baendlorel/kt-packages/tree/main/packages/liuyao)
- [Barnum effect reference](https://dictionary.apa.org/barnum-effect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown responses with optional local JSON, text, and diagram image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local chart, fusion, validation, notes, and diagram files while preparing a response.]

## Skill Version(s):

4.2.0 (source: frontmatter, changelog, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
