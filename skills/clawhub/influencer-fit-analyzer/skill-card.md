## Description:

Build an 8-12 person influencer shortlist from campaign requirements or known creator accounts, using optional public creator lookups or pasted profile and post evidence to summarize followers, recent play, interaction, content pillars, and a talk-or-not call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, creator partnership leads, and agencies use this skill to turn campaign requirements or known creator accounts into an 8-12 person influencer shortlist. The memo supports creator research and approach decisions with attributed follower counts, recent play when available, interaction read, content pillars, and a talk-or-not recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad shared Beatra device credentials.

Mitigation: Review the Beatra authorization scopes before installation and avoid use in environments where shared local credentials are not acceptable.

Risk: The bundled client silently self-updates package code by default.

Mitigation: Use the documented update controls to disable automatic updates when package-managed updates are not acceptable.

Risk: Optional creator lookups are paid and can create duplicate charges if replayed with changed arguments.

Mitigation: Confirm each lookup and its current price before execution, then reuse the same client_request_id only for byte-identical recovery attempts.

## Reference(s):

- [Looking up creators](references/creator-lookup.md)
- [Writing the shortlist](references/shortlist.md)
- [Shortlist workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown memo with optional inline shell commands and JSON task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes task ID, terminal status, and billing.net_charged_credits when an optional paid lookup runs.]

## Skill Version(s):

0.1.3 (source: server release metadata and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
