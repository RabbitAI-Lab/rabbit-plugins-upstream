## Description:

PDEBench competition workflow orchestration with expflow, including full, fast, and skip pipeline modes, distributed HPO, pruner integration, and ClearML HyperParameterOptimizer native mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and MLOps engineers use this skill to plan and run PDEBench competition experiment loops with expflow, ClearML workers, Optuna HPO, training, evaluation, and submission workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Experiment submissions can consume paid queue time, GPU hours, and artifact storage.

Mitigation: Require explicit confirmation of the queue, trial count, parallelism, timeout, and expected resource scope before submitting jobs.

Risk: Package-version choices can change behavior between the public package line and development-line features.

Mitigation: Pin or review the expflow-pde package version before installing or using the workflow.

Risk: ClearML, Langfuse, and dataset credentials may be needed for local execution.

Mitigation: Keep credentials in local environment files or config files and out of tracked skill content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/diamond2nv/skills/expflow-pipeline-hpo)
- [expflow Repository](https://github.com/diamond2nv/expflow)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with bash and YAML snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command patterns, configuration guidance, and operational checks for expflow and ClearML workflows.]

## Skill Version(s):

0.7.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
