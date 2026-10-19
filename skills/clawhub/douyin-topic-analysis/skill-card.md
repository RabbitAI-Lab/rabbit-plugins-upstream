## Description:

帮助内容运营、品牌调研人员和创作者检索抖音内容与热榜，并整理可追溯的短视频选题角度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content teams, brand researchers, and creators use this skill to find Douyin examples and trending topics, compare content angles, and plan short-form video ideas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the latest SocialDataX npm package can introduce unreviewed updates.

Mitigation: Review the package source and pin a trusted version before execution.

Risk: Douyin queries use a SocialDataX API key.

Mitigation: Provide the key through the SOCIALDATAX_API_KEY environment variable and do not include it in shared outputs.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/douyin-topic-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observed content from recommendations and retains useful titles, creators, links, or IDs for traceability.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
