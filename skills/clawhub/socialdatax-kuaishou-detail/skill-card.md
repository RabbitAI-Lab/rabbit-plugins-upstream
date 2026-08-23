## Description:

用于快手数据分析、快手作品详情、作品数据、互动指标、内容调研和内容分析，覆盖 Kuaishou / Kwai work details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve structured Kuaishou work details by photo ID or URL for content research, interaction metrics, and media summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCIALDATAX_API_KEY for SocialDataX-backed detail lookups.

Mitigation: Provide the API key only through the intended environment variable and confirm the requester is comfortable sharing it with SocialDataX-backed commands.

Risk: The preferred direct CLI runs the socialdatax-skills npm package through npx.

Mitigation: Install or run the package only in an environment where executing npm packages is approved.

Risk: Optional media download can write files locally.

Mitigation: Provide an output path only when local saving is intended, and use a specific output directory.

## Reference(s):

- [SocialDataX API access and documentation](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-detail)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY for detail lookups; optional local media saving writes only to a user-specified output path.]

## Skill Version(s):

0.1.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
