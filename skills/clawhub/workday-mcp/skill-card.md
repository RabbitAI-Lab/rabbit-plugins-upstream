## Description:

workday-mcp lets agents read Workday HR data through an MCP server that reuses the user's signed-in Workday browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and other authorized users use this skill to query Workday org charts, worker profiles, compensation, benefits, performance information, tasks, and cards through MCP from their own signed-in session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose highly sensitive HR data through a live signed-in Workday browser session.

Mitigation: Use only with an employer-approved Workday account and only for records the user is authorized to access.

Risk: The setup relies on an npm MCP package and a browser extension connected to the user's signed-in Workday session.

Mitigation: Review the package and extension before installing, follow employer policy, and disable the integration when it is no longer needed.

Risk: The security summary says the skill's scoping and privacy warnings are weaker than the access it describes.

Mitigation: Treat outputs as sensitive HR data and review requests before using the skill for compensation, benefits, performance, or other employee profile information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [fetchproxy extension setup reference](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell commands; MCP tool responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday access through a signed-in browser session; selected deep-read tools support compact and full response views.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
