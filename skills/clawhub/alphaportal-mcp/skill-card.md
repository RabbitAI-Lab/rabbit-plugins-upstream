## Description:

Access AlphaPortal (AlphaRoute) school-bus data, including students, stops, live bus GPS location, and arrival notifications, from a shell with curl instead of running the alphaportal-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve AlphaPortal school transportation information through shell commands and REST API calls. It is intended for authorized access to student, route, stop, notification, and live vehicle-location data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refresh tokens and command output can expose sensitive student and school transportation data.

Mitigation: Use only accounts and data you are authorized to access, treat the refresh token like a password, avoid shared shells and logs, and never paste tokens into scripts or commits.

Risk: Write endpoints can permanently change transportation or notification records without a built-in dry run.

Mitigation: Prefer workflows with explicit confirmations for write actions, and verify the student ID, endpoint, and request body before executing any command that changes records.

Risk: Direct shell access bypasses safeguards that may exist in official or MCP-based workflows.

Mitigation: Review each command before execution and use official or confirmation-gated workflows when handling high-impact actions.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return sensitive student and transportation data from AlphaPortal APIs.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
