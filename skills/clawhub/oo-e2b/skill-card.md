## Description:

E2B (e2b.dev). Use this skill for ANY E2B request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage E2B sandboxes through an OOMOL-connected account, including listing, retrieving, creating, and deleting sandboxes after checking the connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the installer before use, prefer an official verifiable package when available, and do not let an agent run curl-to-bash or Invoke-Expression installer commands automatically.

Risk: The skill can create or delete E2B sandboxes.

Mitigation: Confirm the exact payload and effect before create actions, and require explicit approval for delete actions.

## Reference(s):

- [E2B homepage](https://e2b.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-e2b)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions return JSON responses from the oo connector when run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
