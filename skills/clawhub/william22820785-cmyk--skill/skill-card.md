## Description:

Provides a Chinese fortune-telling consultation persona for long-term life readings and concrete event questions, using packaged Bazi, Ziwei, Liuyao, and Qimen materials to produce conversational answers and selected Markdown diagrams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[william22820785-cmyk](https://clawhub.ai/user/william22820785-cmyk)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users can use this skill for entertainment-oriented Chinese metaphysics consultations about life direction, relationships, career, wealth, timing, or a single concrete question. Agent operators can use it to deliver a structured conversational persona that collects inputs, produces readings, and validates responses against bundled guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate broadly and presents a strong persona while hiding AI and process framing.

Mitigation: Install only when this interaction style is intentional, and review the implicit invocation setting before deployment.

Risk: Fortune-telling outputs may be mistaken for medical, legal, financial, or relationship authority.

Mitigation: Position outputs as entertainment or cultural interpretation, and avoid relying on them for high-stakes decisions.

Risk: The package may run local Python and Node scripts and write local JSON files.

Mitigation: Review and scan the skill before deployment, and run it with file-system permissions appropriate for local generated artifacts.

Risk: Server security evidence says the advertised lunar and Liuyao support may not be fully supported by the packaged files.

Mitigation: Test the intended calendar and event-question workflows before relying on them in a release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/william22820785-cmyk/skills/skill)
- [命理会谈方法](references/consultation-method.md)
- [内部推断方法（v2 — 双盘解读流水线）](references/interpretation-method.md)
- [六爻问事方法（V2.0 六爻+奇门双法同参）](references/liuyao-method.md)
- [话术语气细则](references/voice-and-dialogue.md)
- [Ling et al., CSCW 2026: GenAI fortune-telling trust and workflow](https://arxiv.org/abs/2603.27784)
- [APA Dictionary: Barnum effect](https://dictionary.apa.org/barnum-effect)
- [Yiqi-BaZi-ZiWei upstream project](https://github.com/fdxuyq/Yiqi-BaZi-ZiWei)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Conversational Chinese prose, Markdown tables for selected diagrams, and local JSON artifacts such as chart or fusion results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run bundled Python and Node scripts and write local chart, fusion, plan, or response files during use.]

## Skill Version(s):

4.0.2 (source: server release metadata; artifact frontmatter states 4.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
