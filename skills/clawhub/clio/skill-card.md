## Description:

Clio API integration with managed OAuth that can read, create, update, and delete legal practice data including matters, contacts, activities, tasks, documents, calendar entries, time entries, and billing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to interact with Clio Manage legal-practice data through Maton-managed OAuth and CLI calls. It supports read/list workflows by default and write workflows only after explicit approval with specific resource identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives agents broad write-capable access to sensitive legal-practice data through a generic API gateway without a technical endpoint allowlist.

Mitigation: Install only if you trust Maton with the connected Clio account, use the narrowest Clio scopes and account permissions available, pin the target connection/profile, review every write or delete before approval, and revoke unused Clio connections promptly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/clio)
- [Maton homepage](https://maton.ai)
- [Clio API Documentation](https://docs.developers.clio.com/api-reference/)
- [Clio Fields Guide](https://docs.developers.clio.com/api-docs/clio-manage/fields/)
- [Clio Rate Limits](https://docs.developers.clio.com/api-docs/clio-manage/rate-limits/)
- [Clio Permissions](https://docs.developers.clio.com/api-docs/permissions/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline CLI commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Clio account; write operations require explicit approval before execution.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
