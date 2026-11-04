## Description:

用于快手达人数据、快手达人作品、作品列表、近期发布、内容调研和创作者内容分析。覆盖 Kuaishou / Kwai creator works，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and analysts use this skill to retrieve Kuaishou creator video lists and review recent posts, content styles, and creator benchmarks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API key exposure

Mitigation: Use client-managed secret storage for the environment that runs the CLI, and keep the key out of chat and version control.

Risk: CLI use can consume account credits, and an unreviewed package version may change behavior.

Mitigation: Review and pin a CLI version, and set page or item limits appropriate to the request.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON data, Analysis]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creator video results may include titles or descriptions, publish times, interaction counts, media links, and content types; paginated results may include page and item counts plus a next-page token.]

## Skill Version(s):

0.1.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
