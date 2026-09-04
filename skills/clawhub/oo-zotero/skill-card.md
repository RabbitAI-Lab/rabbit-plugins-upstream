## Description:

Enables an agent to read, search, create, update, and delete Zotero items, collections, and groups through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Zotero libraries through an agent after connecting their Zotero account to OOMOL. It supports bibliographic search, item and collection retrieval, group listing, and guarded write or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Zotero data through write actions.

Mitigation: Confirm the exact payload and expected effect with the user before create or update actions.

Risk: The skill can delete Zotero items or collections.

Mitigation: Require explicit approval for the target and known version before destructive actions.

Risk: Connected Zotero library data may be exposed to agent workflows.

Mitigation: Install and use the skill only when the user intends to grant access through their connected OOMOL Zotero account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zotero)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Zotero](https://www.zotero.org)
- [OOMOL Zotero Connection](https://console.oomol.com/app-connections?provider=zotero)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector command output in JSON.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
