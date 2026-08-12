## Description:

Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External livestock operators and developers use this skill to estimate feed intake from fixed feeder-trough images or videos, review daily intake trends, and identify abnormal intake patterns. The skill also supports querying prior cloud-hosted analysis reports for the current managed identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feeder videos, images, or URLs may be sent to lifeemergence.com services for analysis.

Mitigation: Install and run the skill only when that external data flow is acceptable; avoid submitting sensitive footage unless the service use is approved.

Risk: The skill creates or reuses a managed identity and stores service tokens and report history in local workspace data.

Mitigation: Run the skill in an isolated workspace when evaluating it, and review or clear the workspace data directory before and after use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Feed Intake Estimation API Reference](references/api_doc.md)
- [SMYX Analysis API Reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown and JSON analysis reports, with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes feed-intake estimates, trend status, anomaly alerts, historical report tables, and report links when returned by the service.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
