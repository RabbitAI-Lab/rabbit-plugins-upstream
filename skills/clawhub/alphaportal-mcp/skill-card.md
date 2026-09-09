## Description:

Guides agents to access AlphaPortal school transportation data from a shell by capturing a browser refresh token, minting access tokens, and using curl against AlphaRoute endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized transportation administrators use this skill to inspect AlphaPortal student, stop, vehicle location, notification, and account data from shell workflows. It can also guide scripted access where the MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive school transportation data through direct shell access.

Mitigation: Use it only with explicit authorization for the AlphaPortal account and student transportation data involved.

Risk: Refresh tokens may be exposed through shared machines, recorded terminals, shell history, or logs.

Mitigation: Avoid shared or recorded environments and keep refresh tokens out of shell history, scripts, transcripts, and logs.

Risk: Write examples can change live transportation settings without a dry-run guard.

Mitigation: Review write commands carefully and run them only when the operator understands the live account impact.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, JavaScript, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that access live transportation data or change live notification and walk-zone settings.]

## Skill Version(s):

0.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
