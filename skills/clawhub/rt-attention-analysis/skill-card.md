## Description:

Processes reaction-time and accuracy data from continuous-performance and sustained-attention tasks, computing trailing-average RT windows, cumulative mean and standard deviation, fast/slow triggering thresholds, lapse detection, RT variability, bootstrap and effect-size statistics, and optional RT time-series plots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guigui855](https://clawhub.ai/user/guigui855)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to inspect trial-level reaction-time datasets, detect attentional lapses, run fast/slow trigger labeling, and summarize sustained-attention performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The analysis scripts can overwrite files at caller-selected output paths.

Mitigation: Run the skill with a dedicated output directory for each dataset or analysis run.

Risk: Results depend on user-provided reaction-time data quality and chosen cleaning thresholds.

Mitigation: Review input columns, document exclusions, and inspect generated summaries before using the results in decisions or reports.

## Reference(s):

- [Methods Background - RT-Based Lapse Detection and Real-Time Triggering](references/methods.md)
- [ClawHub skill page](https://clawhub.ai/guigui855/skills/rt-attention-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus generated CSV, text summary, and optional PNG report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Python scripts read user-provided CSV data and write analysis outputs to caller-selected paths.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
