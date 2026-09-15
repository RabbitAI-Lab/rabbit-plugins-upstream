## Description:

Mailercloud (mailercloud.com). Use this skill for ANY Mailercloud request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to operate Mailercloud through an OOMOL-connected account, including creating contacts and lists and managing contact properties. It is intended for Mailercloud workflows that require schema-guided reads, writes, and explicitly confirmed destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the official installer before execution, prefer a signed or package-manager install path when available, and install only when comfortable with OOMOL's CLI and Mailercloud access model.

Risk: Write and destructive actions can create, update, or delete Mailercloud data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Mailercloud homepage](https://www.mailercloud.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailercloud)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and returns JSON responses from oo connector commands when actions run.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
