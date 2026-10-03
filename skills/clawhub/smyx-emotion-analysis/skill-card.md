## Description:

Analyzes facial video files or URLs through a remote service and returns emotion-analysis reports and report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers submit facial videos for emotion-analysis reports and retrieve previous reports. Interpret inferred emotions cautiously rather than treating them as certain evidence of someone's inner state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial videos or their URLs are sent to external lifeemergence.com services.

Mitigation: Obtain consent from everyone depicted and share media only when external processing is acceptable.

Risk: The skill silently creates and reuses account identifiers and tokens in a local workspace database, enabling access to report history.

Mitigation: Avoid shared or sensitive workspaces, restrict access to the workspace, and remove retained identity data when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured emotion-analysis report or Markdown report list, with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis results to a file]

## Skill Version(s):

1.0.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
