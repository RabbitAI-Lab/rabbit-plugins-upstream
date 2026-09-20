## Description:

Weights & Biases connector skill for reading, creating, and updating W&B data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ML practitioners use this skill to inspect W&B projects, runs, artifacts, registries, automations, integrations, documentation, and Weave traces through an OOMOL-connected account. It also supports report creation and analysis logging when the user confirms write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands for the oo CLI.

Mitigation: Do not let an agent run the remote installer automatically; install the CLI through a trusted, verified method before using the skill.

Risk: Some W&B actions can create reports or log analysis results back to W&B.

Mitigation: Confirm the exact write-action payload and expected effect with the user before execution.

## Reference(s):

- [Weights & Biases homepage](https://wandb.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include W&B connector action names, schema inspection commands, JSON request payloads, and confirmation guidance for write actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
