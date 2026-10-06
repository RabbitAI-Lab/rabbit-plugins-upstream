## Description:

Resolve imported field values using source-agreement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to reconcile imported field values against source-agreement guidance, record a local resolution, and optionally submit it to a configured delivery target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can send resolved data off-host without a separate approval step.

Mitigation: Keep CLAWHUB_DELIVERY_ENDPOINT and delivery API-key variables unset for local use; require explicit approval and prefer a separate delivery step for external submission.

## Reference(s):

- [Source Resolution Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/source-assurance-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, CSV files]

**Output Format:** [JSON source-resolution object and local CSV record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes field, disposition, selected value, and agreement count; may include a delivery receipt when configured.]

## Skill Version(s):

1.1.1 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
