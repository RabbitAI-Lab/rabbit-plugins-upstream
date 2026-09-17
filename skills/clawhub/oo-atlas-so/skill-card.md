## Description:

Atlas.so lets an agent use the OOMOL-connected oo CLI to inspect Atlas action schemas and read, create, update, or upsert Atlas customers, accounts, and session recordings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Atlas.so through an OOMOL-connected account, including schema inspection and customer, account, and session workflows. It supports read actions and confirmed write actions for customer and account records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute changing external code.

Mitigation: Review the oo CLI installation path before installing; prefer a signed or package-manager install, or download and inspect or verify the installer before running it.

Risk: Write actions can change Atlas customer or account records.

Mitigation: Approve write actions only after checking the exact action, payload, target record, and expected effect.

## Reference(s):

- [Atlas.so homepage](https://atlas.so)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Atlas.so skill page](https://clawhub.ai/oomol/skills/oo-atlas-so)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas; Atlas write actions require explicit payload and effect confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
