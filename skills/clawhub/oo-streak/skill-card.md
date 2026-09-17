## Description:

Streak helps agents read Streak CRM data through an OOMOL-connected Streak connector and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect schemas and read Streak boxes, pipelines, and the authenticated current user from a connected Streak account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running an unverified internet installer directly in a shell.

Mitigation: Review the oo CLI installation process first, prefer official versioned instructions with checksum or signature verification, and avoid running the installer from an elevated shell.

Risk: The connected Streak account may expose more CRM data than intended.

Mitigation: Connect only the intended Streak account and scopes before using the skill.

## Reference(s):

- [ClawHub Streak Skill](https://clawhub.ai/oomol/skills/oo-streak)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Streak Homepage](https://www.streak.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Streak Icon](https://static.oomol.com/logo/third-party/streak.png)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
