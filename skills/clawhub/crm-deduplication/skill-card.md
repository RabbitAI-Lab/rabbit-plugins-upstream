## Description:

Guides RevOps and GTM engineers through auditing CRM account and contact duplicates, configuring guarded merges, and routing uncertain matches for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

RevOps and GTM engineers use this skill to audit duplicate CRM companies or people, adapt separate deduplication plays, and pilot approved merges with human review for uncertain matches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect match could merge distinct CRM accounts or contacts.

Mitigation: Approve audits and matching policies, keep plays disabled and pilots limited, and verify surviving and absorbed records after merges.

Risk: Review details sent to Slack may expose CRM data to unintended recipients.

Mitigation: Approve the review channel and data-sharing expectations before enabling Human Review.

Risk: An unpinned external installation may change the workflow unexpectedly.

Mitigation: Consider pinning the external cargo-cdk install command before deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/crm-deduplication)
- [Project homepage (listed in skill metadata)](https://github.com/getcargohq/gtm-skills/tree/main/crm-deduplication)
- [Audit guide](references/audit.md)
- [Configuration guide](references/configure.md)
- [Pilot and verification guide](references/run.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with TypeScript examples and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separate account and contact paths; CRM writes require an approved pilot.]

## Skill Version(s):

0.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
