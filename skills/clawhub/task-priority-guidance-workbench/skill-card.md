## Description:

Build an operations task schedule from supplied service-class guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to order tasks and select a start slot from service-class guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive the schedule and local artifact path.

Mitigation: Review delivery settings and leave endpoint and API-key variables unset unless external submission is intended.

Risk: The schedule is saved locally.

Mitigation: Use a dedicated output directory and review its contents before sharing.

## Reference(s):

- [Operations Schedule Builder on ClawHub](https://clawhub.ai/wxt-ai/skills/task-priority-guidance-workbench)

## Skill Output:

**Output Type(s):** [Structured data, Files]

**Output Format:** [JSON task schedule and local CSV artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ordered task IDs, the selected task and start slot, and an effect receipt; includes a delivery receipt when configured.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
