## Description:

Knack (knack.com) handles reading, creating, updating, and deleting records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents serving OOMOL-connected Knack users use this skill to inspect connector schemas and run record create, retrieve, list, update, and delete workflows through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe scripts directly into a shell or PowerShell.

Mitigation: Prefer a verified official oo CLI installation method with version and integrity checks before running Knack actions.

Risk: Write and destructive actions can change or delete Knack records.

Mitigation: Fetch the live action schema, review the exact payload and target, and require explicit user approval before writes or deletes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-knack)
- [Knack Homepage](https://www.knack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payload examples, and setup URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema lookup before action payloads; write and delete operations require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
