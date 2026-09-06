## Description:

Search Target.com, browse categories, retrieve product detail by TCIN, and pull reviews with rating breakdowns as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up Target product search results, category listings, product details, store-aware prices and availability, and limited review data through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-directed Target product queries to Scavio as an external provider and may spend API credits.

Mitigation: Use it only when Scavio is an acceptable provider for the task and monitor credit usage for repeated or automated calls.

Risk: SCAVIO_API_KEY is required for all endpoint calls.

Mitigation: Keep the key in an environment variable or secret store and do not commit it to source control.

Risk: Prices and availability can vary by Target store.

Mitigation: Pass the intended store_id when store-specific results matter and state when default-store results are used.

Risk: Some Target calls have high latency and can hold concurrency slots for tens of seconds.

Mitigation: Use a client timeout of at least 120 seconds and prefer background or asynchronous execution for interactive workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/target-product-data)
- [Scavio Target Search Documentation](https://scavio.dev/docs/target-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Scavio Target Category Documentation](https://scavio.dev/docs/target-category?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Scavio Target Product Documentation](https://scavio.dev/docs/target-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Scavio Target Reviews Documentation](https://scavio.dev/docs/target-reviews?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON API responses and code or shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Target responses are store-aware when store_id is supplied.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
