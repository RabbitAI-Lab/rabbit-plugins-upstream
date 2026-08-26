## Description:

AugmentiQ gives agents persistent local memory for recall, reasoning, recording, and consolidation through the AugmentiQ MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upsurge911-lgtm](https://clawhub.ai/user/upsurge911-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect an agent to a local AugmentiQ MCP server and maintain persistent memory in an Obsidian vault across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist selected conversation context and profile entries in a local Obsidian vault.

Mitigation: Use it only when long-term local memory is desired, avoid storing secrets, and periodically review or clear stored memories and profile entries.

Risk: The underlying MCP tools can create, edit, delete, and consolidate vault content when write access is enabled.

Mitigation: Prefer read-only mode or narrow vault access when note mutation is not needed, and keep bearer-token authentication enabled.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upsurge911-lgtm/skills/augmentiq)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON MCP call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide an agent to recall, create, edit, and consolidate local Obsidian vault memories through authenticated MCP calls.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
