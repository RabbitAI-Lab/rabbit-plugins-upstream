## Description:

Create, update, classify, and archive Obsidian documentation documents following structured vault conventions and templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to keep an Obsidian vault organized with consistent templates, frontmatter, wikilinks, tags, and archival practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create, update, or move Markdown documents in an Obsidian vault.

Mitigation: Use it only with vaults where agent-driven documentation changes are acceptable, and review proposed archive or move actions before applying them.

Risk: The workflow assumes English-primary documentation and may translate or summarize non-English content into English.

Mitigation: Adjust the language convention before use if the target vault should preserve a different primary language.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/ehsanghaffar/skills/tree/main/skills/obsidian-doc-workflow)
- [ClawHub skill page](https://clawhub.ai/ehsanghaffar/skills/obsidian-doc-workflow)
- [ClawHub metadata homepage](https://clawhub.ai/agent/obsidian-doc-workflow)
- [Archive Rules](references/archive-rules.md)
- [Classification: Project vs Shared Knowledge](references/classification-guide.md)
- [Document Types and Templates](references/document-types.md)
- [Linking Conventions](references/linking-conventions.md)
- [Tagging Conventions](references/tagging-conventions.md)
- [Vault Structure and Purposes](references/vault-structure.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Configuration instructions, Guidance, Shell commands]

**Output Format:** [Markdown documents, frontmatter conventions, wikilinks, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or perform Obsidian vault document creation, updates, classification, linking, tagging, and archive moves when the agent has vault access.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
