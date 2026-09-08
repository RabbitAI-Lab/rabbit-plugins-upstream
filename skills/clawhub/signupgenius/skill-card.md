## Description:

Read SignUpGenius sign-up sheets, slot reports, groups, and account profile data, with limited write support for group membership, RSVPs, and slot changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an agent to SignUpGenius through a third-party MCP server, inspect sign-ups, groups, slots, reports, and profile data, and perform selected user-directed write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party MCP server and may access browser-session cookies, a password, or a Pro API key.

Mitigation: Install only after reviewing the server and grant only the account access needed for the task; protect cookies, passwords, and API keys as sensitive credentials.

Risk: The skill can read SignUpGenius profile, group, signup, report, slot, and participant data.

Mitigation: Use it only with accounts and sign-up sheets where that data access is intended, and avoid exposing participant or account details outside the user's authorized context.

Risk: The skill can change group membership, RSVPs, and slot claims or releases.

Mitigation: Require explicit user confirmation before any write action, especially adding group members, changing RSVPs, claiming slots, or releasing slots.

Risk: The security summary says the skill understates write actions and uses broad triggers.

Mitigation: Review the selected tool and intended action before execution, and treat ambiguous SignUpGenius requests as requiring clarification before account changes.

## Reference(s):

- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [signupgenius-mcp repository](https://github.com/chrischall/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands]

**Output Format:** [Markdown with JSON configuration snippets, command examples, and tool-routing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent toward SignUpGenius MCP tools and identifies when confirmation or a Pro API key is required.]

## Skill Version(s):

1.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
