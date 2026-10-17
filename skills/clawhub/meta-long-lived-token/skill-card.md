## Description:

Helps gateway owners exchange and check Meta user access tokens, save the renewed token in gateway settings, and monitor its expiration without changing ads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thinhbuiii](https://clawhub.ai/user/thinhbuiii)

### License/Terms of Use:

MIT-0

## Use Case:

Gateway owners and administrators use this skill to exchange a Meta user token, check its validity and expiration, update gateway settings, and arrange renewal reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App secrets and access tokens may be exposed through messages or logs.

Mitigation: Avoid sharing long-lived secrets in chat when possible; never display or log token values.

Risk: An unauthorized request or incorrect gateway update could compromise access or disrupt existing settings.

Mitigation: Confirm the requester is the owner and review the exact gateway environment update before saving.

Risk: Automated reminder scheduling may run without the owner's intent.

Mitigation: Require explicit approval before adding a daily token-check reminder.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thinhbuiii/skills/meta-long-lived-token)
- [Meta Graph API Explorer](https://developers.facebook.com/tools/explorer)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell examples and expiration status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports token validity and expiry without displaying token values.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
