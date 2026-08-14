## Description:

Analyze BrainNode protobuf recordings from this autonomous-driving project against a natural-language problem description, identify the most likely faulty module, and produce an evidence-based module analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[narol1024](https://clawhub.ai/user/narol1024)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect autonomous-driving PB recordings, compare module evidence across the pipeline, and identify the most likely faulty module behind a reported symptom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous-driving PB logs may contain location, sensor, or operational data.

Mitigation: Install and run the skill only in repositories where the agent is allowed to inspect those logs, and provide exact PB file or directory paths plus an output path when possible.

Risk: A module attribution can be misleading when the recording lacks upstream or execution buffers.

Mitigation: Treat unsupported conclusions as hypotheses, preserve confidence boundaries, and perform the minimum next validation checks listed in the report.

## Reference(s):

- [BrainNode PB Module Signals](references/module-signals.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis report, with optional JSON report from the triage script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default final report is in Chinese unless the user requests another language; conclusions use high, medium, or low confidence rather than measured probabilities.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
