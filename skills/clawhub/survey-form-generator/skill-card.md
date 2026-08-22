## Description:

Generates a structured survey from a user's research goal and renders it as a local HTML form for preview, completion, copying, printing, or export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zenobiazizi](https://clawhub.ai/user/zenobiazizi)

### License/Terms of Use:

MIT-0

## Use Case:

External users, teams, and researchers use this skill to turn a survey goal, audience, and decision context into a usable questionnaire for satisfaction research, NPS, product discovery, market research, internal surveys, or feedback collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill embeds a Dify bearer token.

Mitigation: Remove and rotate the embedded token, then use managed credentials with the narrowest practical access.

Risk: Survey goals may be sent to Dify without a clear per-use consent step.

Mitigation: Show an explicit notice before external transmission and let users choose local generation when they do not want to send the survey goal.

Risk: Users could include confidential business plans, customer details, employee research, or sensitive internal context in the survey goal.

Mitigation: Warn users not to include sensitive context unless they are comfortable sending the survey goal text to Dify.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zenobiazizi/skills/survey-form-generator)
- [Dify workflow API endpoint](https://api.dify.ai/v1/workflows/run)

## Skill Output:

**Output Type(s):** [Files, Code, Guidance]

**Output Format:** [HTML file with embedded survey JSON and brief usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated surveys are intended for preview, trial completion, copying into survey platforms, printing, or local export; the HTML output does not provide multi-user response collection.]

## Skill Version(s):

1.0.0 (source: release evidence and CHANGELOG, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
