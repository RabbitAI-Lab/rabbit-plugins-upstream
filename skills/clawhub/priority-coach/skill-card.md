## Description:

Priority Coach Clawhub is a gentle personal-growth coaching skill that uses five questions to help a user clarify three current priorities, one small action for today, and what to leave aside for now.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for personal priority coaching, daily planning, morning and evening check-ins, and gentle habit support. It is intended to reduce planning overload by turning broad stressors into a short prioritized plan and one small next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved priority records may contain sensitive reflections about stressors, regrets, plans, or raw answers in a local history file.

Mitigation: Save only after explicit user confirmation, avoid saving raw answers unless needed, and use the bundled delete command when the user wants local history removed.

Risk: Personal coaching guidance could be over-relied on for major life decisions.

Mitigation: Keep outputs focused on clarification, small next actions, and what to postpone; avoid making final life decisions for the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [Cold-start questions and summarization rules](artifact/references/cold-start.md)
- [Daily flow details](artifact/references/daily-flows.md)
- [Copy tone guidance](artifact/references/copy-tone.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown conversation output with optional inline shell commands for local record management]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write, list, export, or delete local JSON planning records through the bundled record.py script when the user asks or confirms saving.]

## Skill Version(s):

0.1.2 (source: ClawHub server evidence, released 2026-08-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
