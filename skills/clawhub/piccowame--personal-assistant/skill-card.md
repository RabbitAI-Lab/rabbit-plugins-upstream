## Description:

Helps manage personal tasks, wellness reminders, document drafts, and routine administrative work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[piccowame](https://clawhub.ai/user/piccowame)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and administrative teams use this skill to track commitments, schedule task and wellness reminders, manage document drafting, and prepare routine administrative work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatically recording commitments and drafts may persist sensitive personal or business information.

Mitigation: Review the skill before installation and deliberately configure and protect its local data directory.

Risk: Recurring wellness and deadline reminders may be unwanted or fire at the wrong local time.

Mitigation: Confirm the timezone and reminder schedule, and review recurring jobs before enabling them.

Risk: Broad autonomous admin duties can affect sensitive business, finance, HR, compliance, inbox, filing, or deletion workflows.

Mitigation: Require user confirmation before carrying out sensitive or consequential admin actions.

## Reference(s):

- [Admin playbook](references/admin-playbook.md)
- [Admin duty catalog](references/admin-catalog.json)
- [ClawHub skill listing](https://clawhub.ai/piccowame/skills/personal-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Plain text and Markdown, including reminders, calendars, work orders, and document drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains local task and document records and schedules recurring reminders.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
