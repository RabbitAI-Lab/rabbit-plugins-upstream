## Description:

Businessmap (businessmap.io). Use this skill for ANY Businessmap request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Businessmap workspaces, boards, and cards, then create or update Businessmap records through the OOMOL CLI after reviewing write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, archive, or delete Businessmap data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: The first-time setup path may require installing or updating the remote oo CLI.

Mitigation: Review installer commands against the official install guide before running them.

Risk: The connected Businessmap account grants access to workspace, board, and card data visible to its API key.

Mitigation: Confirm the user trusts OOMOL and the connected Businessmap account scope before using the skill.

## Reference(s):

- [Businessmap homepage](https://businessmap.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to return JSON responses from Businessmap actions.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
