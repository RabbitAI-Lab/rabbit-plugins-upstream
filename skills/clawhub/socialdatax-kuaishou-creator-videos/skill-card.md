## Description:

用于快手达人数据、快手达人作品、作品列表、近期发布、内容调研和创作者内容分析。覆盖 Kuaishou / Kwai creator works，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can review Kuaishou creator video lists, recent publishing activity, content style, creator benchmarks, and account history using a known creator ID or profile link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unbounded pagination can increase provider usage charges.

Mitigation: Set page or item limits when appropriate and consult the provider documentation for billing details.

Risk: Exposure of SOCIALDATAX_API_KEY could allow unintended API use.

Mitigation: Keep the key in a protected environment variable and out of prompts, logs, and generated reports.

Risk: The external npm package is a dependency outside the bundled skill artifact.

Mitigation: Use a trusted package publisher and pin a reviewed package version where practical.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX API documentation](https://socialdatax.com/docs)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [Structured JSON data with concise text or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creator video or series items may include titles or descriptions, summaries, publish times, interaction counts, media links, content types, and pagination metadata when available.]

## Skill Version(s):

0.1.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
