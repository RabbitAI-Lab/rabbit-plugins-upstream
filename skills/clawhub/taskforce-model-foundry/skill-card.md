## Description:

Train, evaluate, resume, and export local models with Taskforce Model Foundry. Use for tmf CLI jobs, HF/PEFT fine-tuning, independent quality gates, and OpenClaw or Hermes model-customization workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ML engineers use this skill to plan and operate local model training, evaluation, recovery, and export jobs with explicit data, compute, and quality boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review evidence is incomplete because three references could not be matched to bundled files.

Mitigation: Review the referenced material and confirm it fits the intended use before running commands from it.

Risk: Training with private data, paid compute, remote hosts, production changes, or publishing can exceed the intended scope or expose data.

Mitigation: Record the job scope and obtain task-specific authorization for those activities; keep data and compute within the approved boundaries.

Risk: Measured single-GPU or pilot results may be mistaken for support of distributed training, production use, or broader benchmarks.

Mitigation: Report measured results separately from unsupported capabilities and evaluate against a disjoint holdout with predeclared quality gates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-model-foundry)
- [Capability and host boundaries](artifact/references/boundaries.md)
- [Executable and command reference](artifact/references/commands.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational steps and verification criteria; no model artifact is produced by the skill instructions alone.]

## Skill Version(s):

0.2.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
