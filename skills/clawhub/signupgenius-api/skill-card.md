## Description:

Guides agents in using shell commands to access SignUpGenius sign-ups, groups, and RSVPs without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other SignUpGenius users can use this skill to prepare shell requests for account data, group membership, public sign-ups, and sign-up actions without installing an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public sign-up endpoints can expose participant names and identifiers, even when names are marked hidden.

Mitigation: Collect participant details only with clear authorization and a legitimate need; avoid sharing or retaining unnecessary personal data.

Risk: Exported passwords, session cookies, header dumps, and tokens can expose an account if leaked.

Mitigation: Use an account you control, protect credentials and session artifacts, and remove temporary files after use.

Risk: Sign-up submissions or withdrawals may change another person's participation if the wrong entry is selected.

Mitigation: Confirm the requested action and account ownership before submitting or withdrawing an entry.

## Reference(s):

- [SignUpGenius API skill release](https://clawhub.ai/chrischall/skills/signupgenius-api)
- [SignUpGenius endpoint reference](references/sug-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may require SignUpGenius account credentials; some requests modify sign-ups.]

## Skill Version(s):

2.1.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
