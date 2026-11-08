## Description:

Read Workday HR data, including org charts, worker profiles, pay, benefits, compensation, and performance, through an MCP server using the user's signed-in session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and managers use the skill to retrieve Workday people, compensation, benefits, and performance information through their signed-in session, and to handle supported HR requests and benefit elections. Access should be approved by the employer, and write previews should be reviewed before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This skill claims to be read-only but also documents tools that submit HR requests and electronically sign benefit elections authorizing payroll deductions.

Mitigation: Have the employer approve access to sensitive employee data, disable write tools when only reading is needed, and review every submission preview, especially benefit signatures and payroll deductions.

Risk: The bundled files do not establish that the external server and extension enforce their claimed safeguards.

Mitigation: Use reviewed, pinned versions.

## Reference(s):

- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [JSON, Configuration instructions, Guidance]

**Output Format:** [Structured JSON and Markdown setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workday information is returned as structured JSON; setup guidance includes MCP configuration and installation commands.]

## Skill Version(s):

1.4.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
