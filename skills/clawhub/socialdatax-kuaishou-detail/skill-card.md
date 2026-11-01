## Description:

用于快手数据分析、快手作品详情、作品数据、互动指标、内容调研和内容分析。覆盖 Kuaishou / Kwai work details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content researchers, and developers use a Kuaishou work ID or URL to retrieve work details and interaction metrics for research and analysis. They can optionally save returned media to a chosen local directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The examples use an automatically updated CLI package, so a later package release could change behavior.

Mitigation: Review the package and pin a version before repeated or production use.

Risk: SocialDataX detail requests use the configured API key and may consume account credits.

Mitigation: Use the intended API key and account, and check expected credit use before making requests.

Risk: Optional media downloads write files to a local destination.

Mitigation: Choose and check the requested output path or directory before downloading media.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-detail)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown, Files]

**Output Format:** [Structured JSON data with a factual text or Markdown summary; optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detail results may include available content, author, publish time, interaction counts, images, and media information. Optional media downloads are saved to the user-selected path.]

## Skill Version(s):

0.1.20 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
