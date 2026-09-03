## Description:

Helps agents build, train, and inspect Liquid Neural Networks using LTC or CfC models, Neural Circuit Policy wirings, and PyTorch-based ncps workflows for time-series prediction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[promiseyuki](https://clawhub.ai/user/promiseyuki)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to train CfC or LTC recurrent models on synthetic or CSV time-series data, inspect sparse NCP wirings, and generate model artifacts or quick validation metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CSV inputs may contain data the user did not intend to process locally.

Mitigation: Only run --csv against intended local data and review selected --features and --target columns before training.

Risk: Training and wiring inspection can write local artifacts when --save or --draw is used.

Mitigation: Set output paths deliberately and review generated .pt or PNG files before sharing or reuse.

Risk: Unpinned Python dependencies can affect reproducibility across environments.

Mitigation: Pin dependency versions or use an environment lockfile when reproducible builds matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/promiseyuki/skills/lnn)
- [ncps documentation](https://ncps.readthedocs.io/en/latest/)
- [Liquid Neural Networks theory reference](references/lnn_theory.md)
- [ncps API cheatsheet](references/api_cheatsheet.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline Python and bash commands; optional local .pt model files and PNG wiring graphs when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read local CSV files supplied by the user and write user-directed outputs via --save or --draw.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
