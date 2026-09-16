## Description:

Operate Raisely through the OOMOL-connected oo CLI connector to read, create, update, and delete Raisely data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Raisely connector schemas and run campaign, fundraising profile, and webhook actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run unverified internet installer scripts for the oo CLI.

Mitigation: Review the installer path and prefer a verified, version-pinned, checksum- or signature-checked installation method before use.

Risk: Write and destructive Raisely actions can change or delete webhook configuration.

Mitigation: Confirm the exact payload, action, and target with the user before running write or delete actions.

## Reference(s):

- [ClawHub Raisely Skill](https://clawhub.ai/oomol/skills/oo-raisely)
- [Raisely Homepage](https://raisely.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
