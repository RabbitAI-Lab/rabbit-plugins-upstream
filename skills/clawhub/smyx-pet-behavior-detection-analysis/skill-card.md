## Description:

Identifies common abnormal pet behaviors such as scratching, biting, destructive chewing, jumping, digging, chasing, and separation anxiety to help owners understand their pet's habits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners use the skill to analyze a pet video for common behaviors and review a structured behavior summary and suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private recordings may be sent to a fixed cloud destination even when --api-url is set.

Mitigation: Avoid private recordings until this control is fixed; confirm the destination and privacy terms before uploading.

Risk: The --export-env-only option does not prevent analysis or possible charges.

Mitigation: Do not treat this option as a dry run; confirm billing implications before invoking the skill.

Risk: The skill may automatically register an account and retain profile data and tokens in a shared workspace database.

Mitigation: Use secure credential storage and establish explicit account controls, especially in shared environments.

Risk: Server-side deletion and report authorization were not verified.

Mitigation: Confirm the provider's retention and report-access controls before uploading recordings or querying reports.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured JSON or a Markdown-style behavior report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior summaries, suggestions, history report lists, and report links]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
