## Description:

Validate an incoming dataset for a stated use, investigate defects and missing coverage, and recommend acceptance, restricted use, correction or rejection. Use for delivery QA and fitness-for-use decisions; use a measurement-specific workflow for a standalone metric calculation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redrookai](https://clawhub.ai/user/redrookai)

### License/Terms of Use:

MIT-0

## Use Case:

Data QA analysts and delivery owners use this skill to assess whether a delivered dataset supports a stated decision, investigate defects and coverage gaps, and recommend acceptance, restricted use, correction, or rejection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profiling output can contain identifying key values.

Mitigation: Handle reports with the same care as the source data and restrict access to people authorized to inspect it.

Risk: A structurally valid profile could be mistaken for evidence of factual accuracy, eligibility, freshness, or coverage.

Mitigation: Use independent evidence appropriate to the intended use and date; report structural checks separately from semantic and coverage checks.

## Reference(s):

- [Worked example: an affiliation delivery](references/example.md)
- [Practice: assess this delivery](references/practice.md)
- [ClawHub release page](https://clawhub.ai/redrookai/skills/dataset-validation)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, JSON]

**Output Format:** [Concise text or Markdown validation brief; optional JSON structural profile]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observations, inferences, and unverified conditions; reports a recommendation and recheck actions.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
