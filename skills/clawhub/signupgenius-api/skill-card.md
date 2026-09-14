## Description:

Access SignUpGenius sign-ups, groups, and RSVPs from a shell with curl by logging in with email and password, obtaining session cookies and a JWT, and calling the v3 API and legacy SUGboxAPI dispatcher directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve SignUpGenius account, group, sign-up, slot, participant, and RSVP data from scripts or shells without installing the signupgenius-mcp server. It also documents live account write flows, so users should confirm intent before making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live SignUpGenius account credentials, JWTs, and session cookies in shell commands.

Mitigation: Use a password manager or secret store, avoid shared terminals and logs, store cookies and tokens in a private temporary directory, and delete them after use.

Risk: Unauthenticated participant-data lookups can expose names, identifiers, quantities, and related sign-up details.

Mitigation: Only retrieve participant data when there is a legitimate reason and authorization, and avoid storing or sharing unnecessary personal data.

Risk: Write examples can add members, submit RSVPs, claim slots, or release sign-ups against a live account.

Mitigation: Require explicit user confirmation before running write commands and verify the affected sign-up, member, and slot identifiers before execution.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands, curl examples, jq filters, and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that handle live credentials, session cookies, account data, participant identifiers, and live write actions.]

## Skill Version(s):

1.8.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
