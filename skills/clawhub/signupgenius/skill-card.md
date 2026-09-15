## Description:

Read sign-up sheets, slot reports, and groups on SignUpGenius, and add members to your groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect SignUpGenius sheets, groups, RSVPs, volunteer slots, and owner-scoped slot reports, and to perform narrow account actions such as adding group members or changing the signed-in user's own RSVP or slot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run external npm and fetchproxy components that may receive SignUpGenius account access.

Mitigation: Install only after reviewing the external package and extension, and prefer a pinned, reviewed package version.

Risk: Credential, API key, or session-cookie based modes can expose account access if stored in shared configuration.

Mitigation: Avoid storing passwords or API keys in shared project config and treat cookie mode like granting account access.

Risk: Write-capable tools can change RSVPs, claim or release slots, or modify group membership.

Mitigation: Require explicit user confirmation before any RSVP, slot claim or release, or group-member change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets, tool names, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP setup commands, account-authentication guidance, and confirmation guidance before write actions.]

## Skill Version(s):

1.8.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
