## Description:

Helps agents manage Mailchimp audiences, subscribers, campaigns, templates, automations, and reports through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and their agents use this skill to inspect and manage Mailchimp email audiences, campaigns, subscribers, and reporting, with approval before account changes or sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account changes and campaign sends may affect subscribers or send email to an entire audience.

Mitigation: Review the target, content, recipient count, and intended effect; obtain explicit approval before each write or send.

Risk: Hosted functions, triggers, and destinations can run unattended or forward event data to other services.

Mitigation: Review each automation and destination separately, including cross-app sources such as Gmail and the data they forward, before approval.

Risk: Connecting a Mailchimp account grants Maton access within the account's authorized scope.

Mitigation: Connect only with the user's consent, grant only needed scopes, and remove connections no longer needed.

## Reference(s):

- [ClawHub Mailchimp skill](https://clawhub.ai/byungkyu/skills/mailchimp)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Mailchimp Marketing API documentation](https://mailchimp.com/developer/marketing/)
- [Mailchimp Marketing API reference](https://mailchimp.com/developer/marketing/api/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require a connected Mailchimp account; changes require user approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
