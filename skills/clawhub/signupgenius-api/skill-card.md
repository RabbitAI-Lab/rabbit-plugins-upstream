## Description:

Access SignUpGenius (sign-ups, groups, RSVPs) from a shell with curl instead of running the signupgenius-mcp server - server-side email/password login to a JWT + cfid/cftoken cookies, then curl the v3 API and legacy /SUGboxAPI.cfm dispatcher directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access SignUpGenius profile, group, sign-up, slot, participant, and RSVP workflows from shell sessions or scripts without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles SignUpGenius passwords, JWTs, and cfid/cftoken cookies as full account credentials.

Mitigation: Use only authorized SignUpGenius accounts, keep credentials in environment variables or a secret manager, avoid logging tokens, and remove temporary cookie or header files after use.

Risk: The skill includes unauthenticated participant-name lookup and guidance for write or withdraw actions.

Mitigation: Use participant lookup only for sign-ups the user is authorized to access, confirm before write actions, and verify a withdrawal belongs to the signed-in member before submitting it.

Risk: Session expiry can return redirects or HTML instead of clear API errors, which can make failed operations look successful.

Mitigation: Check redirect destinations and response bodies for login markers, re-read affected slots after writes or withdrawals, and renew or re-login before retrying.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, curl examples, JSON request bodies, and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill provides command patterns and endpoint guidance; it does not emit standalone executable files.]

## Skill Version(s):

1.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
