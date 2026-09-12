## Description:

Access AlphaPortal school-bus data, including students, stops, live bus GPS location, and arrival notifications, from a shell using curl commands instead of running the alphaportal-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical AlphaPortal users use this skill to mint access tokens from their own signed-in browser session and run curl commands against AlphaPortal data. It is intended for shell workflows and scripts where the MCP server is not installed or not desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches direct reuse of AlphaPortal refresh tokens that can expose sensitive student transportation information.

Mitigation: Install only when you control the AlphaPortal account, keep tokens out of shared shells and terminal history, and prefer an official supported authentication flow or the safer MCP path with confirmations.

Risk: Documented write commands can permanently change transportation records without a dry-run.

Mitigation: Do not run write commands unless you intend to change records; verify the studentId and request body before execution.

Risk: The optional fpx browser bridge can expose browser-stored session data to an additional tool.

Mitigation: Avoid the fpx option unless it has been audited and pinned for the deployment environment.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl and jq recipes for authenticated AlphaPortal API calls.]

## Skill Version(s):

0.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
