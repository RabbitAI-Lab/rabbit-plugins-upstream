## Description:

Validate an incoming dataset for a stated use, investigate defects and missing coverage, and recommend acceptance, restricted use, correction or rejection. Use for delivery QA and fitness-for-use decisions; use a measurement-specific workflow for a standalone metric calculation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redrookai](https://clawhub.ai/user/redrookai)

### License/Terms of Use:

MIT-0

## Use Case:

Data quality analysts, data stewards, and dataset recipients use this skill to assess whether a delivered dataset supports a stated business or operational decision. It organizes structural and semantic checks, coverage and uncertainty findings, and a recommendation to accept, limit, correct, or reject the delivery for that use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profiler output can expose identifying key values.

Mitigation: Use it only on datasets intended for inspection and review its output before sharing.

Risk: Profiling a large CSV can consume substantial memory.

Mitigation: Use the helper only when the file fits the available memory for the profiling task.

Risk: Structural checks alone cannot establish factual accuracy or population coverage.

Mitigation: Verify material facts against appropriate independent evidence and report coverage and unresolved uncertainty separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redrookai/skills/dataset-validation)
- [Worked example](references/example.md)
- [Practice exercise](references/practice.md)
- [CSV structural profiler](scripts/profile_csv.py)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [A concise validation brief in Markdown; the optional CSV profiler emits a structural profile in JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observations, inferences, and unverified conditions; the optional profiler is read-only and structural.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
