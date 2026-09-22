## Description:

Helps an agent read SignUpGenius sign-up sheets, slot reports, groups, and account-related sign-up information, with limited write actions for group membership, RSVPs, slot claims, and slot releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to connect an agent to their own SignUpGenius account or public sign-up pages so it can answer questions about sign-ups, slots, groups, and reports. It can also support explicitly confirmed changes such as adding group members, RSVPing, claiming slots, or releasing the signed-in user's own slot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access SignUpGenius sessions, credentials, or API keys.

Mitigation: Enable it only for accounts where this access is acceptable, and keep credentials scoped to the intended SignUpGenius account.

Risk: The skill can perform state-changing SignUpGenius actions such as RSVPs, slot claims, slot releases, and group-member additions.

Mitigation: Require explicit user confirmation before any write action and verify the target sign-up, slot, group, and identity before proceeding.

Risk: Public-sheet tools may expose participant names from public sign-up pages.

Mitigation: Retrieve and share participant data only when appropriate for the user's task and privacy expectations.

Risk: The security summary notes that the documentation understates some write actions.

Mitigation: Review the write-capable tools before deployment and communicate clearly which operations can modify SignUpGenius data.

## Reference(s):

- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [signupgenius-mcp project](https://github.com/chrischall/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool names, JSON configuration snippets, and concise operational notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference account credentials, session cookies, API keys, public sign-up data, participant names, and state-changing SignUpGenius actions.]

## Skill Version(s):

2.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
