## Description: <br>
用于快手数据分析、快手作品详情、作品数据、互动指标、内容调研和内容分析，覆盖 Kuaishou / Kwai work details，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use this skill to retrieve read-only Kuaishou/Kwai work detail data through SocialDataX, including work metadata, author details, publish time, interaction counts, images, and media summaries when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill invokes the SocialDataX npm package and uses SOCIALDATAX_API_KEY for SocialDataX queries. <br>
Mitigation: Confirm the SocialDataX npm package is trusted before installation and provide SOCIALDATAX_API_KEY only when intending to query SocialDataX. <br>
Risk: The optional media download command can write files locally. <br>
Mitigation: Use the download command only with an explicit output path or output directory chosen by the user. <br>


## Reference(s): <br>
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-detail) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY for SocialDataX detail lookups; optional media downloads write only to the user-selected output path.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
