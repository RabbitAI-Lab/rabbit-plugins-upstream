## Description:

Kuaidi Query helps an agent query KDNiao parcel tracking, manage local shipment subscriptions, detect logistics changes, extract pickup codes, identify carriers, and redact sensitive details in group chats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mochoublog](https://clawhub.ai/user/mochoublog)

### License/Terms of Use:

MIT-0

## Use Case:

External users and OpenClaw agent operators use this skill to check parcel status, subscribe to shipment updates, and receive logistics-change reminders while keeping credentials and sensitive delivery details out of chat where appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: KDNiao API credentials are required and stored locally for tracking queries.

Mitigation: Initialize credentials through the provided setup flow or environment variables, keep the generated files under restricted permissions, and do not paste AppKey values into chat.

Risk: Shipment numbers, optional phone suffixes, and query data are sent to KDNiao.

Mitigation: Use the skill only for intended parcel-tracking workflows and disclose that tracking queries are handled by the KDNiao service.

Risk: Full logistics details can contain sensitive delivery information in group chats.

Mitigation: Keep the default allowlist or redact privacy mode unless a trusted group is explicitly approved for full details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mochoublog/skills/kuaidi-query)
- [Publisher profile](https://clawhub.ai/user/mochoublog)
- [OpenClaw documentation](https://docs.openclaw.ai)
- [KDNiao](https://www.kdniao.com)
- [KDNiao carrier code table](https://www.yuque.com/kdnjishuzhichi/dfcrg1/mza2ln)
- [Carrier code reference](references/companies.md)
- [KDNiao state code reference](references/state_codes.md)
- [Cron scheduling reference](references/CRON_CONFIG.md)
- [Security hardening reference](references/hardening.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-producing helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call KDNiao APIs through local Python scripts and may read or update local credential, privacy, and subscription files.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
