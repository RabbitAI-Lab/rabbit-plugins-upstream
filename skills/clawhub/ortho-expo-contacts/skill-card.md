## Description:

Compliance-first orthopedic expo contact lookup covering AAOS 2026, OMTEC 2025, DKOU 2026, AAHKS 2025, AOSSM 2025, and SOFCOT 2025 records, with real-name registration, anti-harassment pledge, quotas, collision alerts, a do-not-contact list, and hash-chained audit logging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External business users and operators use this skill to look up orthopedic expo exhibitors or attendees for compliant, purpose-limited commercial outreach. It supports finding suppliers, country-specific exhibitors, product categories, OMTEC attendees, and structured expo contact lists while enforcing registration, pledge, quota, blocklist, and audit controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized processing or sharing of expo and contact data.

Mitigation: Install and use the skill only when authorized to process the contact data; keep contacts.db, registry files, and audit logs out of shared storage and published packages.

Risk: Use for bulk outreach, harassment, or contact after refusal.

Mitigation: Use the built-in registration, anti-harassment pledge, quotas, do-not-contact list, and audit trail; stop contact after refusal and avoid any batch-export workaround.

Risk: Exposure of private L3 contact lists if a user explicitly includes them.

Mitigation: Keep L3 data excluded by default, use --include-l3 only for private local lists, and do not publish or share indexes built with private contact data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/ortho-expo-contacts)
- [Publisher Profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Data Sources](references/DATA_SOURCES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured command output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results are purpose-limited and may be masked unless a reveal action is permitted by the skill's gating controls.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
