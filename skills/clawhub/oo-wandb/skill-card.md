## Description:

Weights & Biases (wandb.ai). Use this skill for Weights & Biases requests involving reading, creating, and updating data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ML practitioners use this skill to inspect and manage W&B projects, runs, artifacts, registries, automations, reports, and Weave traces through the oo CLI. It also supports report creation and analysis logging when the user confirms the exact payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands, which evidence.security identifies as a high-impact supply-chain risk.

Mitigation: Review and independently verify the oo CLI installer source before running curl-piped shell or PowerShell installer commands.

Risk: Some actions can change Weights & Biases state by creating reports or logging analysis results.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Weights & Biases homepage](https://wandb.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wandb)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; read actions can return JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
