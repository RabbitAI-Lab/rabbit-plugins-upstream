## Description:

Guides agents through using shell commands to read Microsoft Teams chats, channels, messages, unread items, inline images, and the Activity feed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Teams users can use the guidance to inspect their own chats and channels, find unread messages, review Activity feed items, and retrieve inline images from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helpers described as read-only can also change data, and requests can send the saved sign-in token to additional destinations.

Mitigation: Prefer a version that enforces GET requests and one validated destination without arbitrary curl options; require explicit confirmation for each Teams change; protect the cached token and revoke the browser grant when finished.

Risk: Separately downloaded dependencies have not been audited.

Mitigation: Review the separately downloaded dependencies before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Teams chat-service recipes](artifact/references/chatsvc-recipes.md)
- [Teams shell helpers](artifact/references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions operate on the signed-in user's Teams account and may retrieve private chat content.]

## Skill Version(s):

0.8.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
