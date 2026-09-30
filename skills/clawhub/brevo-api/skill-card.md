## Description:

Guides agents in using Brevo through Maton to manage contacts and campaigns and send transactional email or SMS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Brevo account users can use this skill to retrieve account data, manage contacts and lists, prepare campaigns, and send messages through an authorized Maton connection. It also describes optional automations using hosted functions and supported event or schedule triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account or granting excessive access may expose Brevo data.

Mitigation: Confirm the new connection with the user and review requested authorization scopes.

Risk: Contact changes, deletions, campaign sends, and hosted functions can have lasting effects.

Mitigation: Confirm the target and intended effect with the user before each write or send.

Risk: Trigger destinations may forward events persistently, and raw API keys can be exposed.

Mitigation: Approve destination hosts and payloads separately; prefer CLI-managed credentials over raw MATON_API_KEY use.

## Reference(s):

- [Brevo skill on ClawHub](https://clawhub.ai/byungkyu/skills/brevo-api)
- [Maton](https://maton.ai)
- [Brevo API documentation](https://developers.brevo.com/)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON]

**Output Format:** [Markdown with CLI examples, API requests, and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Brevo connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
