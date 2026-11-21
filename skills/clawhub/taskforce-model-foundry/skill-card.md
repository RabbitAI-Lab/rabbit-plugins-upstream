## Description:

Train, evaluate, resume, and export local models with Taskforce Model Foundry. Use for tmf CLI jobs, HF/PEFT fine-tuning, independent quality gates, and OpenClaw or Hermes model-customization workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ML engineers use the skill to plan and manage local model training jobs, evaluate tuned models against independent quality gates, and export passing results with recorded scope and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security analysis was partial because three referenced local paths were unresolved.

Mitigation: Review the available skill information and decide whether the missing-path uncertainty is acceptable before installing.

Risk: Private data, remote transfers, paid compute, or production changes could exceed the agreed job scope.

Mitigation: Record the job scope and obtain task-specific authorization before using private data, remote hosts, paid compute, or production systems.

## Reference(s):

- [Executable and command reference](artifact/references/commands.md)
- [Capability and host boundaries](artifact/references/boundaries.md)
- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-model-foundry)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell command examples and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Job-specific results and generated files depend on the local project, model, and backend.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
