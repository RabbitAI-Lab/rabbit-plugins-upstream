## Description:

Memory Manager helps AI agents create, index, retrieve, and maintain local Markdown-based long-term memory under the user's home directory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to organize project histories, contacts, decisions, knowledge, and collections as local Markdown files with index-based navigation and keyword search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and update persistent files under $HOME/memory.

Mitigation: Install only when local long-term memory is desired, review the planned file paths before execution, and keep the agent's file-system permissions scoped to intended directories.

Risk: The artifact claims local-only storage but also includes callback_url and network/API troubleshooting references.

Mitigation: Confirm those references are removed or clearly scoped before installation, and do not store credentials or highly sensitive personal data in the memory directory.

Risk: Broad activation language may cause the skill to handle conversations beyond memory-management tasks.

Mitigation: Use the skill only for explicit memory creation, retrieval, indexing, sync, or maintenance requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files and concise text responses with local file paths and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates local files under $HOME/memory when the agent has file-system access.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
