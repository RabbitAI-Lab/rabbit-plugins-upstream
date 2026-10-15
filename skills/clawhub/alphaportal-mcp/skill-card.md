## Description:

Guides authorized users through accessing AlphaPortal student transportation data with shell commands instead of running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized parents, guardians, and developers use this skill to retrieve student stops, bus locations, and arrival notifications through the AlphaPortal API without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copying a browser refresh token can expose account access.

Mitigation: Use only accounts you are authorized to access; treat tokens like passwords and keep them out of shared terminals, shell history, logs, and printed scripts.

Risk: Student locations and transportation details are sensitive.

Mitigation: Limit access to authorized students and avoid logging or sharing returned student data.

Risk: Write examples can change transportation settings without confirmation.

Mitigation: Run write commands only with explicit permission and an independent review step.

## Reference(s):

- [AlphaPortal endpoint recipes](references/endpoints.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [AlphaPortal MCP skill release](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may expose account tokens or sensitive student transportation data.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
