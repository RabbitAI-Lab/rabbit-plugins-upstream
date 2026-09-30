## Description:

Guides revenue operations teams through contact and company enrichment across multiple providers, with email verification and cost checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and go-to-market engineers use this skill to enrich batches of contacts or companies through fallback providers, verify returned email addresses, and estimate costs before a larger run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact and company records may be shared with Cargo and its providers.

Mitigation: Submit only data authorized for those services.

Risk: Bulk enrichment consumes credits proportional to the number of records.

Mitigation: Sample 10–20 records, disclose observed cost and hit rate, and obtain approval before a full run.

Risk: The skill includes session attribution, local agent-configuration inspection, and an optional unpinned broader install outside the enrichment task.

Mitigation: Review these steps before execution and skip the optional install unless the source is trusted.

Risk: The optional GitHub starring step acts through the user's account.

Mitigation: Never star without the user's explicit consent.

## Reference(s):

- [Waterfall Enrichment on ClawHub](https://clawhub.ai/cargo-ai/skills/waterfall-enrichment)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo waterfall provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/waterfall.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Markdown]

**Output Format:** [Markdown with shell commands and optional results table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results may report matches, email verification, unmatched records, and credits used.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
