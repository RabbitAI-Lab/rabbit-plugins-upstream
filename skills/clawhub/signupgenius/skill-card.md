## Description:

Read sign-up sheets, slot reports, and groups on SignUpGenius, and add members to your groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect SignUpGenius profiles, groups, sign-up sheets, slots, and reports, and to perform limited account-scoped updates such as adding group members or managing RSVP and slot participation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform account-scoped write actions including RSVP changes, slot claims, slot releases, and group-member changes.

Mitigation: Require explicit user confirmation before any RSVP, slot claim, slot release, or group-member change.

Risk: Cookie-extension mode handles live session cookies through unpinned third-party components.

Mitigation: Prefer a pinned, audited package version and avoid cookie-extension mode unless the session-cookie risk is acceptable.

Risk: Authenticated use can expose or modify SignUpGenius data tied to the signed-in account.

Mitigation: Use the lowest-privilege SignUpGenius account practical for the intended workflow.

## Reference(s):

- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [signupgenius-mcp source repository](https://github.com/chrischall/signupgenius-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and tool recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP setup and tool use for account-scoped SignUpGenius reads and limited write actions.]

## Skill Version(s):

1.8.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
