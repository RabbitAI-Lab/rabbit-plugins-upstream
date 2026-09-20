## Description:

Работа со СберБизнес API: пошаговый онбординг со ссылками, Zero-Knowledge Vault (AES-256-GCM), выбор канала уведомлений (Telegram/MAX/Discord/Slack/Webhook), остатки, платежки, ссылка на подпись, выгрузка PDF со штампом банка.

This skill is ready for commercial/non-commercial use.

## Publisher:

[synthet1x](https://clawhub.ai/user/synthet1x)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business users use this skill to connect an agent to SberBusiness API workflows for onboarding, balance checks, payment draft creation, signed payment links, statement downloads, and transaction notifications.

### Deployment Geography for Use:

Russia

## Known Risks and Mitigations:

Risk: The skill handles banking credentials, mTLS certificates, access tokens, payment drafts, and account data.

Mitigation: Install and run it only on a trusted machine, keep the .p12 file and Client Secret out of chat, and complete credential setup through local masked input.

Risk: Plaintext credential fallback or mishandled local secrets could expose bank-grade credentials.

Mitigation: Avoid plaintext .env credential fallback and rely on the local encrypted vault workflow described by the skill.

Risk: Transaction notifications can expose sensitive financial data through Telegram, Slack, Discord, MAX, or custom webhooks.

Mitigation: Enable notification channels only when they are private, controlled, and approved for sensitive financial data; otherwise prefer on-demand or minimized notifications.

Risk: Persistent polling and payment draft workflows can affect financial operations if configured incorrectly.

Mitigation: Review configuration before deployment and require human review/signature in SberBusiness before payments are executed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/synthet1x/skills/sber-business)
- [SberBusiness Portal](https://sbi.sberbank.ru)
- [Gosuslugi Trusted Certificates](https://www.gosuslugi.ru/crt)
- [Human Walkthrough](references/HUMAN_GUIDE.md)
- [Notification Channels](references/NOTIFICATION_CHANNELS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration; supporting scripts can return text, JSON data, and PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local setup guidance, polling configuration, payment draft links, balance summaries, notification messages, and bank-stamped PDF downloads.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
