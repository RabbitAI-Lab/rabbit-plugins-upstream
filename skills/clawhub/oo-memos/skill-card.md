## Description:

This skill enables agents to operate Memos (usememos.com) for reading, creating, updating, and deleting memos and attachments through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Memos account through the OOMOL `oo` CLI, including reading, creating, updating, deleting, and attaching files to Markdown memos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes remote shell and PowerShell installer commands for the oo CLI.

Mitigation: Do not let an agent execute those installers automatically; install the CLI manually from a trusted source or verify the installer before running it.

Risk: Read actions can access Memos content through the connected account.

Mitigation: Use the skill only with an intended account and review requested read scope before exposing memo or attachment content.

Risk: Write and destructive actions can create, update, delete, or overwrite memos and attachments.

Mitigation: Require explicit user approval after checking the exact action target and payload.

## Reference(s):

- [Memos homepage](https://usememos.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-memos)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces `oo connector` command guidance and action payloads for Memos operations.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
