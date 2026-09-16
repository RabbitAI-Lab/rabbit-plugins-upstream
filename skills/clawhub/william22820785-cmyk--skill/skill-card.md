## Description:

以一位有五十年经验、精通八字紫微六爻奇门、自信豁达而有锋芒的算命老师傅身份连续算人和算事。用八字紫微处理命理定盘、人生结构与阶段运势，用六爻奇门双法同参处理具体事情的成败、走向、时机和取舍。

This skill is ready for commercial/non-commercial use.

## Publisher:

[william22820785-cmyk](https://clawhub.ai/user/william22820785-cmyk)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users use this skill for entertainment-oriented Chinese divination consultations about personal life patterns, relationship, career, money, timing, and concrete yes-or-no events. The skill guides an agent to collect calendar or divination inputs, run bundled charting scripts, and return concise conversational readings or Markdown divination diagrams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give highly certain divination-style guidance in sensitive areas such as health, legal matters, relationships, and money.

Mitigation: Position outputs as entertainment or cultural divination only, and do not rely on them for medical, legal, financial, or major relationship decisions.

Risk: The skill auto-invokes broadly and runs bundled Python and Node scripts.

Mitigation: Review the skill before installation and deploy it only in environments where local script execution is acceptable.

Risk: Some advertised self-contained functionality failed inspection because required Node dependencies were missing.

Mitigation: Validate bundled runtime dependencies and test charting and consultation flows before release or operational use.

## Reference(s):

- [Skill Instructions](SKILL.md)
- [Consultation Method](references/consultation-method.md)
- [Interpretation Method](references/interpretation-method.md)
- [Liuyao Method](references/liuyao-method.md)
- [Voice and Dialogue](references/voice-and-dialogue.md)
- [Zi Wei Dou Shu Basics](https://www.ziwei.my/zi-wei-dou-shu-portfolio/zwds-guide-zi-wei-dou-shu-basics-9/)
- [Barnum Effect](https://dictionary.apa.org/barnum-effect)
- [The Art of Fate Calculation](https://www.cefc.com.hk/article/homola-stephanie-2023-the-art-of-fate-calculation-practicing-divination-in-taipei-beijing-and-kaifeng-new-york-berghahn-books/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Conversational text and Markdown, with occasional shell commands and JSON-backed validation artifacts for the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke bundled Python and Node scripts to produce chart JSON, fusion JSON, validation results, and Markdown divination diagrams.]

## Skill Version(s):

4.0.2 (source: server release metadata; artifact frontmatter reports 4.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
