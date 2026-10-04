## Description:

Add entries to a renewal schedule.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal and account teams use this skill to add dated agreement obligations to a local renewal schedule and receive a schedule receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill appends renewal rows to a local CSV in the chosen output directory.

Mitigation: Choose a dedicated output directory and review the effect receipt path after each run.

Risk: A local schedule receipt may be mistaken for an external renewal action.

Mitigation: Treat the receipt as confirmation of a local CSV update only; verify any external follow-up separately.

## Reference(s):

- [Renewal Schedule Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/agreement-renewal-schedule-workbench)

## Skill Output:

**Output Type(s):** [Structured data, Files]

**Output Format:** [JSON schedule receipt and locally appended CSV rows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes schedule ID, rows, and a local file-effect receipt.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
