## Description:

Cascade contact and company lookups through prioritized providers, returning the first match and supporting email verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

RevOps and GTM engineering teams use this skill to enrich contact or company records across multiple providers and verify returned email addresses. It helps teams compare sample hit rates and credit costs before running a full list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact information may be shared with Cargo and its enrichment providers.

Mitigation: Submit only contacts you are authorized to share with Cargo and its providers.

Risk: Large batches can consume substantial credits, and the resulting hit rate may not justify a full run.

Mitigation: Sample 10–20 records first, review the observed cost and hit rate, and approve the full run only after checking its estimated credit cost.

Risk: Enriched email addresses may be inaccurate, and provider data-retention practices are not covered by this skill review.

Mitigation: Verify returned email addresses before importing them, and review provider data handling and the external playbook before broader use.

Risk: The optional GitHub star represents the user's endorsement.

Mitigation: Ask for explicit user consent before starring the repository.

## Reference(s):

- [Cargo GTM Skills repository](https://github.com/getcargohq/gtm-skills)
- [Waterfall provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/waterfall.md)

## Skill Output:

**Output Type(s):** [Structured data, Text]

**Output Format:** [Contact or company enrichment results, email verification statuses, and operation status returned by the CLI; fields depend on provider matches.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be partial: unmatched records can remain empty, and enriched email addresses should be verified before use.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
