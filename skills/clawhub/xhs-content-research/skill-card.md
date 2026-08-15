## Description:

面向内容运营、品牌调研和创作者的小红书内容研究辅助技能。适用于 RedNote / XHS / Xiaohongshu（小红书）内容研究、选题分析、关键词观察、趋势判断、竞品内容对比和素材整理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operations teams, brand researchers, and creators use this skill to search XHS / RedNote content, compare topics or competitors, identify content angles, and organize cited samples for follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCIALDATAX_API_KEY to access SocialDataX through an npm CLI.

Mitigation: Configure the key only in the local environment, avoid embedding it in files or reports, and install the skill only where that third-party API use is acceptable.

Risk: Returned XHS note URLs can include xsec_token values that function as sensitive-ish working links.

Mitigation: Preserve full URLs when they are required for reproducibility, but limit sharing and storage of tokenized links and redact them in broader logs or reports.

Risk: The skill provides research samples from current XHS search results, which may be partial or change over time.

Mitigation: Separate visible evidence from interpretation, keep returned note IDs and URLs with cited findings, and avoid presenting a limited result page as complete platform coverage.

## Reference(s):

- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-content-research)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with XHS sample listings, analysis notes, and CLI or MCP call guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only XHS research output may include note URLs, note IDs, pagination tokens, and suggested follow-up questions.]

## Skill Version(s):

0.1.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
