## Description:

Reads Workday HR data through MCP using the user's signed-in Workday browser session and returns read-only structured data about org charts, worker profiles, pay, benefits, compensation, performance, and task or data cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and authorized operators use this skill to query Workday pages and profile data from their own authenticated session for HR lookup, org navigation, and task-card inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable third-party install commands can run unpinned code in an authenticated HR-data context.

Mitigation: Review and pin exact versions or commits for both workday-mcp and fetchproxy before installation.

Risk: The workflow can expose sensitive Workday HR data from the user's active SSO session.

Mitigation: Use a dedicated browser profile and limited environment, and confirm the employer's acceptable-use policy before use.

Risk: Raw Workday page reads and user-supplied GraphQL documents can return more sensitive data than intended.

Mitigation: Prefer typed read-only tools, minimize requested data, avoid GraphQL mutations, and review returned content before sharing.

## Reference(s):

- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [workday-mcp source repository](https://github.com/chrischall/workday-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command snippets; MCP tool responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday data access through the user's active browser session; selected deep reads default to compact media-stripped output.]

## Skill Version(s):

0.6.3 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
