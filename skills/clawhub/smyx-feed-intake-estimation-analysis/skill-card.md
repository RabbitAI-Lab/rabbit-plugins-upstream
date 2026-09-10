## Description:

Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts. | 通过食槽视频估算每日采食量变化，异常时预警。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and farm operations teams use this skill to estimate livestock feed intake from fixed feeder-area images or videos, review intake trends, and receive anomaly alerts. It supports precision feeding management and feed-cost monitoring, while keeping feeding adjustments and ration formulation outside its scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded farm images or videos are sent to a cloud API and associated with an automatically managed identity.

Mitigation: Use only approved media, confirm data retention and access controls with the publisher, and avoid footage that contains unrelated sensitive information.

Risk: Security evidence reports plaintext HTTP endpoints and local storage of reusable authentication tokens.

Mitigation: Do not install for production use until the publisher moves release endpoints to HTTPS, removes development HTTP addresses, and stores or avoids tokens securely.

Risk: Security guidance flags an unresolved yaml dependency issue.

Mitigation: Require the publisher to correct dependency declarations and re-run release scanning before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Feed intake estimation API documentation](references/api_doc.md)
- [Common AI analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include daily feed-intake estimates, trend and anomaly labels, report links, and historical report lists formatted as Markdown tables.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
