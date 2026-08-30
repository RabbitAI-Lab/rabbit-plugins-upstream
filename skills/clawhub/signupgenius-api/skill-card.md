## Description:

Provides curl-based guidance for signing in to SignUpGenius session mode and calling profile, group, sign-up listing, public lookup, RSVP, slot claim, and release endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to prepare SignUpGenius curl requests for authorized sign-ups, groups, RSVPs, and slot actions without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles SignUpGenius account credentials, session cookies, and bearer tokens.

Mitigation: Avoid storing secrets in shell profiles, logs, screenshots, or shared terminals; delete temporary cookie and header files after use.

Risk: RSVP, slot claim, release, and group-member calls can change SignUpGenius account or sign-up state.

Mitigation: Confirm the target account, sign-up, slot, RSVP, release, or group-member change before running write commands.

Risk: Some calls can expose public participant or sign-up data.

Mitigation: Use the skill only for SignUpGenius accounts and sign-ups the user is authorized to access or modify.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](artifact/references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes authenticated and unauthenticated SignUpGenius request patterns; users must supply their own authorized credentials, tokens, cookies, and endpoint parameters.]

## Skill Version(s):

1.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
