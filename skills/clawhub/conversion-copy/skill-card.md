## Description:

Combines Amazon product details and review evidence to diagnose buyer decision barriers and recommend evidence-grounded Amazon page conversion copy improvements; it does not predict conversion rates, run ads, or automatically publish page changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and agents use this skill to inspect product-detail and review evidence for a specified ASIN/site, then produce practical listing conversion copy recommendations with stated data limits and cost-confirmation boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can access ARI account and product data.

Mitigation: Use browser authorization or local configuration only, keep the key out of chat and reports, and revoke or recreate the key if authentication fails or exposure is suspected.

Risk: Paid operations and account-changing actions may exceed a narrow conversion-copy workflow.

Mitigation: Keep auto-confirm set to ask when per-charge approval is desired, run quote/check steps first, and require explicit user confirmation before paid operations, monitoring changes, competitor changes, or account-setting updates.

Risk: Persistent schedules, watch settings, and competitor bindings can continue affecting the account after the current conversation.

Mitigation: Treat create, pause, resume, delete, schedule, and competitor actions as durable changes; state the target ASIN/watch ID and cost implications before executing them.

Risk: A custom ARI base URL could redirect key-bearing requests away from the official service.

Mitigation: Avoid ARI_BASE_URL overrides for normal use and require an explicit ARI_ALLOW_CUSTOM_BASE setting only for intentional development or self-hosted environments.

Risk: Interrupted paid analysis may already have consumed credits and produced an archived report.

Mitigation: Check reports or operation status by ASIN/requestId before retrying any confirmed paid operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/conversion-copy)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [Dedicated Operations Workflow](artifact/references/operation-workflow.md)
- [User Guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain-text agent responses with optional CLI commands, report links, and export guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference ARI report URLs and user-requested Markdown, HTML, or CSV exports; outputs should preserve data limits, sample sizes, credit usage, and confirmation status.]

## Skill Version(s):

1.4.8 (source: evidence.release.version, SKILL.md frontmatter, _meta.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
