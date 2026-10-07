## Description:

Maps candidate skills to role-focused interview topics and creates an interview agenda, with optional configured delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters and interview coordinators use this skill to match a candidate's skills to role requirements and prepare a shareable interview agenda.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured HTTP destination can receive candidate-related agenda data using supplied credentials.

Mitigation: Use a trusted, explicit delivery configuration; clear unrelated delivery endpoint and API key variables before running.

Risk: Interview agendas can contain sensitive recruiting information.

Mitigation: Treat generated agendas as sensitive candidate data and restrict access to the output and delivery destination.

## Reference(s):

- [Candidate Skills Mapper on ClawHub](https://clawhub.ai/wxt-ai/skills/candidate-interview-agenda-complete)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Local Markdown interview agenda and JSON results with effect and delivery receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Delivery is optional; without configuration, the agenda remains local.]

## Skill Version(s):

1.2.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
