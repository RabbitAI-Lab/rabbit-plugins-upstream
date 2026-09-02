## Description:

Read SignUpGenius sign-up sheets, slot reports, and groups, and help add members or make supported RSVP and slot changes for the signed-in user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect SignUpGenius commitments, group membership, public slot availability, and owner-scoped reports. It can also support carefully confirmed account-changing actions such as adding group members, RSVPing, claiming slots, or releasing slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform account-changing actions such as RSVPs, slot claims or releases, and group-member changes.

Mitigation: Require explicit user confirmation before any write action and show the target sign-up, slot, group, and identity before proceeding.

Risk: The skill may use SignUpGenius credentials, a Pro API key, or browser-session cookies.

Mitigation: Treat MCP configuration as sensitive, use scoped configuration or secrets handling, and avoid session reuse when browser-cookie access is not intended.

Risk: The authoritative security review flags the release as suspicious because credential/session handling and account-changing actions are understated.

Mitigation: Review the skill carefully before installing and allow it only in contexts where this account access and write behavior are acceptable.

## Reference(s):

- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with JSON configuration snippets and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require SignUpGenius account credentials, browser-session access, or a Pro API key depending on the selected authentication mode and requested report.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
