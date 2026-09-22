## Description:

End-to-end encrypted .md documents for agents and humans to collaborate by creating, searching, syncing, updating, and deleting encrypted markdown documents through Fileverse tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vijaykrishnavanshi](https://clawhub.ai/user/vijaykrishnavanshi)

### License/Terms of Use:


## Use Case:

Developers, agents, and human collaborators use this skill to manage encrypted markdown documents across CLI, MCP-enabled clients, and chatbot interfaces. It supports document creation, retrieval, search, updates, deletion, sync status checks, and retrying failed sync events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A custom Fileverse MCP endpoint may receive document plaintext.

Mitigation: Use only endpoints you control or have verified, and require HTTPS before connecting clients or agents.

Risk: Synced document links include key-bearing fragments and can expose access if shared broadly.

Mitigation: Treat full ddoc links as sensitive secrets and share them only with intended collaborators.

Risk: Delete and broad update operations can permanently remove or overwrite encrypted documents.

Mitigation: Require explicit user confirmation before deletion or broad update actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vijaykrishnavanshi/skills/encrypted-docs)
- [ddocs.new](https://ddocs.new)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration snippets, and JSON tool responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses include document identifiers, sync status, metadata, and key-bearing links when documents are synced.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
