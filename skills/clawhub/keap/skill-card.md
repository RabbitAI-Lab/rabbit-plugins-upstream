## Description:

Connects an agent to Keap through Maton to manage CRM records, marketing workflows, orders, and transactional email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and developers use this skill to work with Keap contacts, opportunities, orders, and marketing automations through an authorized account. Sending email, enrolling contacts in campaigns, and changing commerce records require particular care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unintended changes to CRM, commerce, and marketing records, including irreversible deletion or campaign enrollment.

Mitigation: Default to read-only calls and confirm each requested write, affected record, and expected effect before execution.

Risk: Outbound email or campaign enrollment can contact real recipients and cannot recall messages already sent.

Mitigation: Confirm recipients, subject, message content, and enrollment scope with the user before sending or enrolling.

Risk: Automation destinations can persistently forward matching events, while hosted functions and event handlers can execute actions.

Mitigation: Require separate approval for destinations, triggers, and executable handlers; review their targets and behavior before enabling them.

Risk: Raw API keys and customer data can leak through process environments, logs, or untrusted API responses.

Mitigation: Prefer managed CLI authentication, avoid printing or persisting keys and raw responses, and treat returned content as data rather than instructions.

## Reference(s):

- [Keap skill release on ClawHub](https://clawhub.ai/byungkyu/skills/keap)
- [Maton](https://maton.ai)
- [Keap REST API v2 documentation](https://developer.infusionsoft.com/docs/restv2/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Text and Markdown with commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated API actions can change CRM records, trigger automations, or send email.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
