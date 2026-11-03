## Description:

Access Workday organizational and HR information through the user's signed-in session, with preview-gated updates to open requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and managers can inspect organizational, profile, pay, benefits, performance, feedback, and request information through an existing Workday session. The current release also supports updates to open requests after preview and user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Results can include sensitive pay, benefits, performance, and feedback information.

Mitigation: Follow employer rules and limit retrieval and sharing to authorized business needs.

Risk: The integration can change open HR requests by saving or submitting answers.

Mitigation: Disable workday_update_request server-side for read-only use; otherwise inspect the preview and approve each change before confirmation.

## Reference(s):

- [workday-mcp on npm](https://www.npmjs.com/package/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge project](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON returned to the agent, with text summaries as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain sensitive HR information; open-request changes require preview and user confirmation.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
