## Description:

Guides agents through reading authorized HoneyBook client-portal data from the shell by capturing a signed-in browser session with fpx and then using curl against HoneyBook API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve HoneyBook contracts, invoices, proposals, payment methods, and workspace status from accounts they own or are authorized to access. It is intended for shell-based workflows where the HoneyBook MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles live HoneyBook session credentials that can expose private client records and payment-related data.

Mitigation: Use the skill only with accounts you own or are authorized to access, keep captured tokens out of shared or world-readable storage, and treat session values like passwords.

Risk: The artifact examples write captured session and response data to files under /tmp, which may be inappropriate on shared machines.

Mitigation: Prefer shell variables or a protected working directory for sensitive captures, remove temporary files after use, and avoid running the workflow on shared systems.

Risk: The skill relies on captured browser session state instead of an official server-side authentication flow.

Mitigation: Prefer the supported HoneyBook MCP or an official authentication path when available, and re-capture sessions only when authorized.

## Reference(s):

- [HoneyBook requests for fpx + curl](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup steps, request patterns, error handling guidance, and notes for handling captured session credentials.]

## Skill Version(s):

0.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
