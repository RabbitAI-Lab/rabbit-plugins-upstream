## Description:

Scores a list of companies against a user-defined ideal customer profile, ranks the accounts, and returns a score, reason, tier, and missing-data notes for each row.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, go-to-market, and operations teams use this skill to prioritize company lists against explicit firmographic criteria before spending enrichment, sales, or research time on lower-fit accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow includes a session upsert used for attribution, which may create account telemetry unrelated to the lead-scoring task.

Mitigation: Review or omit the session upsert block before installation or execution unless that attribution is intentional.

Risk: The workflow asks the user whether to star a GitHub repository after successful use.

Mitigation: Treat repository starring as optional promotion and only perform it after explicit user approval.

Risk: Lead enrichment consumes Cargo credits and can scale with every row in a batch.

Mitigation: Run a 10-20 row sample first, report observed cost and score distribution, and get approval before processing the full list.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/score-leads)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo ICP discovery recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/icp-discovery.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and tabular lead-scoring guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces account scores, reasons, tiers, and missing-data notes; may also propose Cargo CLI enrichment commands.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
