## Description:

面向内容运营、品牌调研和创作者的小红书内容研究辅助技能，适用于 RedNote / XHS / Xiaohongshu（小红书）内容研究、选题分析、关键词观察、趋势判断、竞品内容对比和素材整理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand researchers, and creators use this skill to perform read-only XHS content research from keywords or topic directions. It helps agents collect visible samples, compare content angles, review trends, and organize follow-up questions for topic or competitor analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports can include full XHS note URLs with xsec_token parameters.

Mitigation: Avoid forwarding reports or logs broadly; share sanitized links when traceability is not needed.

Risk: The skill depends on the SocialDataX npm package and an API key in the user's environment.

Mitigation: Install only when comfortable with that package and protect SOCIALDATAX_API_KEY from logs, commits, and shared outputs.

Risk: Search results are sampled from requested pages and filters, not guaranteed complete platform coverage.

Mitigation: State the query, filters, and page limits with conclusions, and broaden or repeat searches before treating findings as comprehensive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-content-research)
- [SocialDataX AI access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and Node.js/npm; generated reports may include full XHS note URLs.]

## Skill Version(s):

0.1.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
