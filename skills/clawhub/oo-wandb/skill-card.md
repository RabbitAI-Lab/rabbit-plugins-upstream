## Description:

Weights & Biases helps agents operate W&B through OOMOL's `oo` CLI for reading, creating, and updating W&B data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect W&B schemas, query projects, runs, artifacts, registries, automations, reports, and Weave traces, and create reports or logged analysis after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the OOMOL CLI.

Mitigation: Prefer a pinned, signed, or package-manager installation path and review the installer before use.

Risk: `log_analysis` can create a W&B run and change workspace state.

Mitigation: Treat `log_analysis` as a write action and confirm the exact payload and effect before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-wandb)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Weights & Biases Homepage](https://wandb.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing W&B actions require explicit confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
