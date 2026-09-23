## Description:

Personal Health Manager provides Chinese-language wellness support across nutrition, fitness planning, sleep, weight management, health-metric tracking, physical-exam interpretation, medication reminders, and chronic-condition management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to organize personal wellness information, estimate nutrition and training needs, review common physical-exam indicators at a non-diagnostic level, and prepare lifestyle changes or follow-up questions for clinicians.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local persistent learning can store sensitive health-adjacent preferences or notes and influence future behavior without enough user control.

Mitigation: Make memory opt-in, avoid storing health details, isolate data per user, and provide deletion and retention controls.

Risk: The skill provides health and physical-exam guidance that could be mistaken for diagnosis or treatment advice.

Mitigation: Keep outputs informational, avoid prescription-drug advice, identify urgent warning signs, and direct users to qualified medical professionals for health decisions.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with optional shell commands for local learning records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local persistent learning records for capability usage, errors, preferences, and optimization notes when the learning script is invoked.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
