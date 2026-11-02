## Description:

通过 SocialDataX 获取抖音视频或图文作品详情及互动指标，用于内容调研与分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use the skill to retrieve structured details and interaction metrics for a Douyin work by ID or content URL, supporting content research and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detail requests use SocialDataX API credits.

Mitigation: Use a dedicated SocialDataX API key and account for API credit charges.

Risk: Optional media downloads write files locally.

Mitigation: Choose the intended output folder explicitly.

Risk: The external CLI package code was not bundled and publisher provenance could not be independently verified.

Mitigation: Prefer a reviewed, pinned CLI version.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-detail)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON detail response; optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detail requests require SOCIALDATAX_API_KEY; optional media downloads are saved to the requested local output path.]

## Skill Version(s):

0.1.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
