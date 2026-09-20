## Description:

Planhat (planhat.com). Use this skill for ANY Planhat request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read, create, list, and update Planhat company and end-user records through an OOMOL-connected Planhat account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute downloaded scripts.

Mitigation: Review the installer path before use, prefer a verified release or official package process, check signatures or hashes when available, and avoid elevated shells.

Risk: Write actions can change Planhat business data.

Mitigation: Inspect the live connector schema, confirm the exact payload and effect with the user, and execute only after confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-planhat)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Planhat Homepage](https://www.planhat.com)
- [Planhat Icon](https://static.oomol.com/logo/third-party/planhat.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live schema inspection commands and confirmation steps before write actions.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
