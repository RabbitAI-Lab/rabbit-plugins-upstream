## Description:

Supports insurance underwriting staff with health review, medical risk assessment, underwriting conclusion explanation, follow-up planning, and double-recording quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance underwriting employees use this skill as an internal reference workflow to draft health risk reviews, medical underwriting assessments, underwriting conclusion explanations, follow-up plans, and double-recording QA reports for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes customer calling and message-sending workflow language that may conflict with its no-automation claims.

Mitigation: Install only inside a controlled insurance underwriting environment and do not grant CRM, notification, call, or message-sending tool access unless outreach steps require explicit per-action human approval and remove automatic execution language.

Risk: The workflow may involve customer, health, medical, financial, or other sensitive personal data.

Mitigation: Redact customer and health data before use, follow data minimization, and keep any required records only in approved institutional systems.

Risk: Draft underwriting conclusions, premium adjustments, exclusions, deferrals, or refusal rationales could be treated as final business decisions.

Mitigation: Require qualified underwriting personnel to review source materials, institutional rules, and all generated outputs before any business action or customer communication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/gechengling/skills/underwriting-expert-digital-employee)
- [ClawHub publisher profile](https://clawhub.ai/user/gechengling)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown reports, checklists, risk assessments, suggested wording, and follow-up guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are internal drafts that require human review before use with customers or business systems.]

## Skill Version(s):

2.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
