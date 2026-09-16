## Description:

Databox helps an agent operate Databox through OOMOL's oo CLI to manage accounts, data sources, datasets, and dataset ingestion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Databox from an OOMOL-connected account: list accounts, create or delete data sources and datasets, push JSON records, and check ingestion status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends remote installer scripts for the oo CLI, which may be unsafe if run without verification.

Mitigation: Review the oo CLI installation path, prefer verified packages or releases with checksum or signature validation, and avoid running remote installers from an elevated shell.

Risk: Write and destructive Databox actions can create or delete data sources and datasets or push records into a dataset.

Mitigation: Confirm the exact account, target dataset or data source, payload, and expected effect before allowing write or destructive commands.

## Reference(s):

- [ClawHub Databox skill page](https://clawhub.ai/oomol/skills/oo-databox)
- [Databox homepage](https://databox.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confirmation guidance for write and destructive Databox actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
