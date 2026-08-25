## Description:

Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts. | 通过食槽视频估算每日采食量变化，异常时预警。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External livestock operators and farm-management teams use this skill to estimate feed intake trends from feeder-area videos or URLs and review anomaly alerts and cloud report history. It supports visual trend analysis only and does not provide feed-ration or nutrition recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends feeder videos, video URLs, and identity-linked report requests to the lifeemergence cloud service.

Mitigation: Install and run it only when users are comfortable sharing feeder media with that service, and avoid submitting media that includes unnecessary people, identifiers, or unrelated sensitive farm information.

Risk: The skill can create or reuse a persistent local identity and store returned service tokens in a workspace SQLite database.

Mitigation: Review workspace data storage before deployment, restrict filesystem access to trusted users, and rotate or remove stored tokens when the workspace is shared or retired.

Risk: The security verdict is suspicious because of persistent identity handling and external service token use.

Mitigation: Review the skill before installation and scan future versions before deployment; treat cloud report history and token handling as security-sensitive behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance]

**Output Format:** [Markdown or JSON-like structured analysis text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include feed-intake estimates, trend or anomaly labels, report links, and cloud report-history listings.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
