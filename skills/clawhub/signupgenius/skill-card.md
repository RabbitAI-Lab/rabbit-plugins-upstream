## Description:

Reads SignUpGenius sign-up sheets, slot reports, and groups, and helps users add members to their own groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query their SignUpGenius account, inspect public sign-up availability, and perform narrow account actions such as RSVP, slot release, slot claim, and group-member additions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run third-party code with SignUpGenius credentials or session access.

Mitigation: Use a pinned, reviewed package version, avoid storing real passwords or API keys in project files, and prefer a dedicated least-privileged account where possible.

Risk: RSVP, slot claim, slot release, and group-member addition operations can change account or event state.

Mitigation: Require explicit user confirmation immediately before any state-changing action.

Risk: Public sign-up slot listings may expose participant information.

Mitigation: Use participant listings only for the user's specific request and avoid bulk collection, profiling, or unrelated reuse.

Risk: The artifact notes that scripted or automated SignUpGenius access may conflict with service terms.

Mitigation: Keep use personal-account and personal-scale, and review applicable SignUpGenius terms before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [signupgenius-mcp source repository](https://github.com/chrischall/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [SignUpGenius](https://www.signupgenius.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets, shell commands, and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated MCP tool use against a user's SignUpGenius account; state-changing actions should require explicit confirmation.]

## Skill Version(s):

1.8.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
