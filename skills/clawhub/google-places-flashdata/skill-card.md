## Description:

Searches Google Places through FlashData for local businesses, addresses, ratings, and review counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can find and compare local businesses by city or category and build shortlists using available addresses, ratings, and review counts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, location context, and locale settings are shared with FlashData and its upstream data providers.

Mitigation: Avoid including confidential business plans, secrets, or unnecessary personal details in searches.

Risk: Queries spend paid FlashData Credits and a timed-out submission may already have been charged.

Mitigation: Review the budget before searching; check the existing job or billing status instead of automatically retrying a timed-out submission.

Risk: Exposing the FlashData API key could allow unauthorized paid queries.

Mitigation: Store the key in protected settings and never place it in prompts, logs, or committed files.

## Reference(s):

- [FlashData Google Places documentation](https://flashdata.dev/docs/sources/google_places?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Query example](references/query.json)
- [Query input schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Business lists or comparison tables with available place details; structured query results when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Addresses, ratings, and review counts may be missing; results are not a complete business database.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
