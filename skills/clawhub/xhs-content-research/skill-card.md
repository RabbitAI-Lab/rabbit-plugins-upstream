## Description:

面向内容运营、品牌调研和创作者的小红书内容研究辅助技能，用于 RedNote / XHS / Xiaohongshu 内容研究、选题分析、关键词观察、趋势判断、竞品内容对比和素材整理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand researchers, creators, and agents use this skill to search public XHS/RedNote content by keyword, inspect sample notes, compare topic angles, and organize follow-up research questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords, pagination tokens, and the SocialDataX API key are sent to SocialDataX through the npm CLI.

Mitigation: Install and run the skill only when that data sharing is acceptable, and keep SOCIALDATAX_API_KEY scoped and protected in the runtime environment.

Risk: Returned XHS note URLs may include xsec_token query parameters that can be sensitive when shared broadly.

Mitigation: Share full returned URLs only with audiences that should receive the complete source link, and avoid unnecessary reposting or persistence of those URLs.

Risk: Returned pages are samples from the requested query and pagination window, not complete coverage of all XHS content.

Mitigation: Separate observed evidence from conclusions, document query parameters, and avoid presenting sampled results as platform-wide exhaustive findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-content-research)
- [SocialDataX API key and product page](https://socialdatax.com/ai?from=clawhub)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI command examples and structured research notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public XHS note URLs, note IDs, pagination tokens, and suggested follow-up analysis angles.]

## Skill Version(s):

0.1.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
