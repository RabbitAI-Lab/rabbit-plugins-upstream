## Description:

Operates Weights & Biases through an OOMOL-connected account to read, create, update, compare, diagnose, and search W&B data using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ML engineers, and external users use this skill to inspect W&B entities, projects, runs, artifacts, registries, automations, integrations, and documentation. They can also perform controlled write workflows such as creating reports or logging analysis results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad invocation can route many W&B-related requests through this skill.

Mitigation: Review requested W&B entity, project, run, artifact, or registry targets before executing connector actions.

Risk: Some actions create reports, log analysis results, or otherwise change W&B state, including log_analysis.

Mitigation: Require explicit user approval for state-changing actions and confirm the exact payload and expected effect before execution.

## Reference(s):

- [Weights & Biases homepage](https://wandb.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector command output and JSON responses; state-changing actions should be confirmed before execution.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
