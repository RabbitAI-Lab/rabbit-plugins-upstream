## Description:

Mem0 adds an adaptive memory layer for Clawdbot using semantic search and automatic storage of user preferences, patterns, and conversation context across interactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abhayjb](https://clawhub.ai/user/abhayjb)

### License/Terms of Use:

ISC

## Use Case:

Developers and agents use this skill to add semantic memory retrieval and controlled memory storage to Clawdbot conversations, especially for remembering explicit user requests, preferences, and recurring context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory text, conversation snippets, and search queries may be processed by OpenAI and retained locally.

Mitigation: Use this skill only in trusted single-user setups, avoid storing secrets or sensitive personal data, and confirm user intent before adding memories.

Risk: Broad memory listing, user selection, and delete-all controls can expose or remove stored memories with limited safeguards.

Mitigation: Restrict who can run the scripts, avoid exposing broad --user and --all deletion commands to general agents, and require explicit confirmation before deletion.

## Reference(s):

- [Mem0 Integration Patterns](references/integration-patterns.md)
- [ClawHub Skill Page](https://clawhub.ai/abhayjb/skills/mem0)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional JSON command output is available when JSON_OUTPUT is set.]

## Skill Version(s):

1.0.0 (source: package.json and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
