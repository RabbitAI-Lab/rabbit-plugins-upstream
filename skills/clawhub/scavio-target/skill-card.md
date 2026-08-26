## Description:

Search Target.com, browse a category, read product detail by TCIN and pull reviews with the rating breakdown as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to retrieve Target product search results, category listings, product details, store-aware pricing and availability, and review summaries through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target search terms, TCINs, category IDs, optional store IDs, and endpoint requests are sent to Scavio, and each endpoint call consumes one Scavio credit.

Mitigation: Use SCAVIO_API_KEY from an environment variable or secret store, avoid sending sensitive search terms, and make credit use clear before running calls.

Risk: Target calls can be slow, and concurrency is plan-limited and shared across Scavio services.

Mitigation: Use long client timeouts, prefer background or async execution for user-facing workflows, throttle fan-out, and retry transient 502 or 503 responses once after a short delay.

Risk: Product data is store-dependent, and the reviews endpoint returns at most eight review bodies rather than the full review corpus.

Mitigation: Pass store_id when store-specific data matters, state when default-store data is used, include product URLs for verification, and do not present returned review bodies as exhaustive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-target)
- [Scavio Target search documentation](https://scavio.dev/docs/target-search)
- [Scavio Target category documentation](https://scavio.dev/docs/target-category)
- [Scavio Target product documentation](https://scavio.dev/docs/target-product)
- [Scavio Target reviews documentation](https://scavio.dev/docs/target-reviews)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell and Python examples; API responses use JSON envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Target endpoint calls consume one Scavio credit each and may require long client timeouts.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
