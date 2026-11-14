## Description:

Turns a conversation or user-provided content into a structured infographic plan, validates its layout and numerical consistency, and renders a self-contained static HTML infographic in six supported layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can turn supplied text or notes into a single-page infographic when they explicitly request one. The structured plan can be validated and revised before rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A passed numerical check may not show that an infographic figure is supported by its source.

Mitigation: Review numerical claims in the generated infographic against the supplied source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/text-to-infographic)
- [Infographic plan schema](artifact/schemas/infographic-plan.schema.json)
- [Validation rules specification](artifact/docs/校验规则规格-v0.1.md)

## Skill Output:

**Output Type(s):** [JSON, HTML]

**Output Format:** [Structured infographic plan in JSON and self-contained static HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-page infographic; six layouts are supported; rendered HTML has no JavaScript or external requests.]

## Skill Version(s):

1.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
