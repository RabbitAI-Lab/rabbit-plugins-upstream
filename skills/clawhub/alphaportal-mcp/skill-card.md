## Description:

Guides authorized users through accessing AlphaPortal school transportation data and account settings from a shell without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized AlphaPortal users and developers can retrieve student transportation details, bus locations, and notifications or change account settings using shell commands instead of the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow exposes a reusable browser credential to the shell and can disclose sensitive student transportation and location data.

Mitigation: Use only with authorized account access; keep credentials out of shared terminals, logs, transcripts, and version control.

Risk: Documented write requests change live transportation settings without a preview or confirmation step.

Mitigation: Use write requests only with explicit authority, after independently verifying the student and exact request body.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return sensitive student transportation and location data or make account changes.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
