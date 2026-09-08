## Description:

Enterprise Service Assistant helps campus operations teams manage daily work, tenant service, and follow-up items using local SQLite queries, local cache files, and scheduled Tencent Docs synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[perrykono-debug](https://clawhub.ai/user/perrykono-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Campus operations employees use this skill to triage daily service work, review tenant records, follow fees, renewals, repairs, inventory, and service requests, and prepare reminders or reports from configured business data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad business-record access and local persistence could expose tenant, financial, and operational data.

Mitigation: Review and narrow enabled features before installation, protect Tencent Docs credentials, and restrict access to local SQLite, cache, and tracking files.

Risk: Outbound WeCom notifications and scheduled pushes may send sensitive or incorrect content.

Mitigation: Disable scheduled pushes until recipients and message contents are approved, and require human confirmation for customer-facing financial or legal messages.

Risk: Financial, equity-warrant, and legal-escalation workflows could be mistaken for autonomous decisions.

Mitigation: Use the skill as an operational aid only and require human approval for fee, legal, compensation, equity, or customer-notice decisions.

Risk: Contradictory source-write and privacy statements may create uncertainty about whether Tencent Docs data is read-only or writable.

Mitigation: Confirm intended Tencent Docs permissions before connecting production records, and test synchronization behavior with non-production data first.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/perrykono-debug/skills/enterprise-service-assistant)
- [README](artifact/README.md)
- [Installation guide](artifact/knowledge/INSTALL.md)
- [Onboarding guide](artifact/knowledge/ONBOARDING.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with tables, task lists, code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local SQLite, cache, and tracking-file updates, plus WeCom webhook message content when configured.]

## Skill Version(s):

3.6.0 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
