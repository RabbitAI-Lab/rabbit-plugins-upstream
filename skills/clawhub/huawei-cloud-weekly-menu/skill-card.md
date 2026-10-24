## Description:

Generates a reproducible weekly meal plan in Markdown, plain text, or JSON from a bundled dish library, without using Huawei Cloud services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals planning meals and developers automating meal-plan generation can create a one-week menu from the supplied dish library, customize the days and meal slots, and reproduce results with a seed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using --output overwrites the selected file.

Mitigation: Choose and verify the output path before running the generator; omit --output to print the menu instead.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-weekly-menu)
- [Usage guide](references/usage-guide.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Weekly meal-plan output in Markdown, plain text, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can be seeded for reproducibility; dish repetition within a meal slot is avoided when the dish pool permits.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
