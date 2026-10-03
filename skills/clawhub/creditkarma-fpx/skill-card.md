## Description:

Guides agents in retrieving Credit Karma transactions with shell commands using a signed-in browser session, without running the Credit Karma MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and account holders use this skill to retrieve and paginate their Credit Karma transactions in shell-based workflows without the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell tooling and the browser bridge can access live Credit Karma session cookies and refresh tokens.

Mitigation: Use only on a machine you control; treat CKAT, CKTRKID, ACCESS, and REFRESH like passwords, and avoid shared terminals and logs.

Risk: Captured transaction history or credentials may remain in temporary or output files.

Mitigation: Keep sensitive values out of files where possible; protect or remove any temporary and output files containing account data or tokens.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/creditkarma-fpx)
- [Credit Karma request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transaction results may contain sensitive financial data.]

## Skill Version(s):

3.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
