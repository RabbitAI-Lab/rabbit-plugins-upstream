## Description:

Use fpx and shell helpers to read Microsoft Teams conversations, channels, unread messages, Activity feed entries, and inline images through Teams' chat service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect a signed-in Teams account from shell scripts when they need chat, channel, unread-message, Activity-feed, or inline-image data without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial ClawScan flagged a mismatch between the read-focused description and authenticated change behavior, and possible requests beyond the stated read scope.

Mitigation: Review the scope mismatch and authenticated request behavior before installation; treat the scan as incomplete because some references were unresolved.

Risk: Shell requests use a captured Teams bearer token, and direct write requests can change chats or user state.

Mitigation: Keep the token private, use only intended endpoints, and require explicit approval before any post or reaction; inspect a conversation before retrying a timed-out send.

## Reference(s):

- [Teams chat-service recipes](artifact/references/chatsvc-recipes.md)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused Teams chat-service requests; no shared-file downloads]

## Skill Version(s):

0.8.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
