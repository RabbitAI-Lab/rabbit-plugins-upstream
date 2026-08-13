## Description:

Search Target.com, browse a category, read product detail by TCIN and pull reviews with the rating breakdown as structured JSON. 4 endpoints, 1 credit each, store-aware pricing via store_id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Target.com product data, browse categories, inspect product details, and retrieve review summaries through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target searches and product lookups are sent to Scavio using SCAVIO_API_KEY and consume Scavio credits.

Mitigation: Use the credential only in trusted environments, disclose external API use to users, and limit calls to the product data needed for the task.

Risk: Store-specific requests can reveal the store context used for pricing or availability.

Mitigation: Send store_id only when store-level price or availability is needed, and state when results are tied to a specific or default store.

Risk: Long-running Target endpoints can hold API slots and delay interactive workflows.

Mitigation: Use a client timeout of at least 120 seconds, prefer background execution for slow calls, and avoid broad parallel fanout.

## Reference(s):

- [Scavio Target Search Documentation](https://scavio.dev/docs/target-search)
- [Scavio Target Category Documentation](https://scavio.dev/docs/target-category)
- [Scavio Target Product Documentation](https://scavio.dev/docs/target-product)
- [Scavio Target Reviews Documentation](https://scavio.dev/docs/target-reviews)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with JSON and inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns structured Target product, category, pricing, availability, and review data.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
