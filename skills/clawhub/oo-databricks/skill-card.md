## Description:

This skill lets agents inspect schemas and run OOMOL Databricks connector actions for clusters, jobs, runs, repos, secrets, and workspace objects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data engineers, and operators use this skill to manage Databricks resources through an OOMOL-connected account. It supports read, write, and destructive administration workflows with confirmation expected before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes running a remote oo CLI installer script without an artifact-level verification step.

Mitigation: Review the installer before running it and prefer a verified package or checksum-backed install path when available.

Risk: Write and destructive Databricks actions can create, modify, overwrite, or delete workspace resources.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running any action marked write or destructive.

## Reference(s):

- [Databricks homepage](https://www.databricks.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-databricks)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and metadata, including an execution ID when actions run.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
