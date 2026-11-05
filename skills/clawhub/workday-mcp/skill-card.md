## Description:

Reads Workday org charts, worker profiles, compensation, benefits, performance reviews, and task pages through an MCP server connected to the user's signed-in Workday session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and managers use the skill to retrieve authorized Workday people, compensation, benefits, performance, and task data for workplace questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags a mismatch between the read-only description and the documented request-update tool, which can save or submit HR requests.

Mitigation: Resolve whether request writes are available and disable them when only reading; require user approval before every save or submission.

Risk: The skill handles sensitive workplace records, while the server and browser extension safeguards were not bundled for verification.

Mitigation: Limit access to authorized records and review a pinned server version and the extension before enabling it for workplace data.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [Project repository listed in the skill documentation](https://github.com/chrischall/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured JSON results, including text fields and tabular records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free-text Workday content is untrusted; grid results may be partial when Workday returns only a chunk.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
