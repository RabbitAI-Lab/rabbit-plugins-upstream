## Description:

Guides agents through SberBusiness API onboarding, local encrypted credential setup, notification channel configuration, balance checks, payment draft creation, signing links, and bank-stamped PDF statement downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[synthet1x](https://clawhub.ai/user/synthet1x)

### License/Terms of Use:

MIT-0

## Use Case:

Business operators, finance staff, and developers use this skill to connect an agent to SberBusiness API workflows for account balance review, transaction alerts, payment draft preparation, signature handoff, and official PDF statement retrieval. The skill is intended for environments where the operator is authorized to connect the machine to SberBusiness and manage banking credentials locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles banking credentials, client certificates, tokens, and account data on the local machine.

Mitigation: Install it only on a machine intended for SberBusiness access, protect ~/.openclaw/secrets, and keep credentials in the encrypted vault workflow described by the artifact.

Risk: Optional notification channels can transmit financial transaction details outside the local environment.

Mitigation: Review each channel before enabling it, use private or internal endpoints, require HTTPS webhooks, and enable privacy masking where appropriate.

Risk: Payment draft creation can prepare banking actions that still require operator judgment.

Mitigation: Review payment details before signing in SberBusiness; the skill returns a signing link rather than completing signature by itself.

## Reference(s):

- [Human Walkthrough](references/HUMAN_GUIDE.md)
- [Notification Channels](references/NOTIFICATION_CHANNELS.md)
- [SberBusiness Portal](https://sbi.sberbank.ru)
- [Trusted Certificates](https://www.gosuslugi.ru/crt)
- [Telegram BotFather](https://t.me/BotFather)
- [MAX Business](https://business.max.ru)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON command responses, notification messages, signing links, and downloaded PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local encrypted vault files, poll state/log files, notification configuration, and bank-stamped PDF exports when invoked.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact README/SKILL heading)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
