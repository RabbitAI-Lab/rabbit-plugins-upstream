## Description:

A unified Tradebee Website Builder Open API skill for managing blogs, FAQs, custom pages, news, navigation, products, inquiries, visitor analytics, keyword rankings, and tenant HTML rules, with update actions that read and locally back up the current record before mutation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tradebee](https://clawhub.ai/user/tradebee)

### License/Terms of Use:

MIT-0

## Use Case:

External Tradebee site operators and their agents use this skill to read, create, update, or delete website content and to inspect inquiry, visitor, and keyword-ranking data through explicit Tradebee actions. Developers and operators can also use it to fetch tenant HTML generation rules before producing supported HTML fragments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change public site and business content.

Mitigation: Install it only where the agent is authorized to administer Tradebee content, and require explicit object type, target ID or confirmed ID list, and payload review before create, update, or delete actions.

Risk: Update actions create local backup JSON files that may contain sensitive business or personal data.

Mitigation: Store backups in a controlled environment, restrict access to the installed skill directory, and define retention and deletion procedures for backup files.

Risk: Inquiry and visitor actions can expose customer messages or visitor telemetry.

Mitigation: Limit access to users who need that data and retrieve only the minimum records needed for the stated Tradebee task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tradebee/skills/tradebee)
- [Tradebee Open API Homepage](https://open.tradew.com)
- [Artifact README](artifact/README.md)
- [Artifact Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Files, Guidance]

**Output Format:** [Structured JSON API responses and local backup JSON files, with concise Markdown or text guidance for routing, confirmations, and errors.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BEE_API_KEY. Update actions may write local backup JSON files under backups/<action>/ before mutating Tradebee records.]

## Skill Version(s):

26.8.24 (source: server release metadata, package.json, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
