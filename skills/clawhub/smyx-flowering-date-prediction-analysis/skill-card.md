## Description:

Analyzes flower-bud images or videos through a remote service to report estimated flowering dates and retrieve cloud report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, greenhouse operators, and botanical gardens can submit flower-bud media to estimate flowering dates for planning pollination, harvests, or visits, and can review prior cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted plant media or URLs are sent to configured lifeemergence.com services.

Mitigation: Review the publisher's data handling before submitting sensitive or proprietary footage.

Risk: Cloud history is queried, and an account may be created or reused with tokens stored in a local workspace database.

Mitigation: Confirm the account model and protect the workspace database before enabling analysis or history queries.

Risk: Flowering-date estimates may be inaccurate for production scheduling.

Mitigation: Check predictions against on-site observations and historical experience before committing to a schedule.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-flowering-date-prediction-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [JSON or concise text for analysis; Markdown table for cloud report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and optionally save results to a file.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
