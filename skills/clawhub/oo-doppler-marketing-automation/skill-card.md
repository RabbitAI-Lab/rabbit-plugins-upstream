## Description:

Doppler Marketing Automation helps agents read, create, update, and delete Doppler Email Marketing lists and subscribers through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Doppler Email Marketing subscriber lists and subscribers through an OOMOL-connected account, including read, write, and destructive list membership actions after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use the official installation guide, verify signatures or checksums when available, and avoid piping remote scripts directly into a shell.

Risk: Write and destructive actions can change or remove Doppler list and subscriber associations.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-doppler-marketing-automation)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Doppler Marketing Automation homepage](https://www.fromdoppler.com/en/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
