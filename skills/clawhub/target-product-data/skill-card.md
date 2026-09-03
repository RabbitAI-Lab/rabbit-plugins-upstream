## Description:

Search Target.com, browse a category, read product detail by TCIN and pull reviews with the rating breakdown as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to retrieve Target product search results, category listings, TCIN-level product details, store-aware price and availability data, and review summaries through the Scavio API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Target product lookup requests through Scavio as an intermediary service.

Mitigation: Use the skill only where Scavio is an acceptable processor for the requested product lookup workflow.

Risk: SCAVIO_API_KEY is required for all calls and could be exposed if embedded in source or prompts.

Mitigation: Store the key in the environment or a secret store and avoid hard-coding it in shared files.

Risk: API calls consume credits and exhausted balances return billing-related errors.

Mitigation: Monitor credits_used and credits_remaining in responses and plan top-ups or usage limits before high-volume runs.

Risk: Target prices and availability are store-dependent and may be inaccurate for a user's intended location if no store_id is supplied.

Mitigation: Pass the relevant store_id and include product URLs so users can verify important pricing or availability decisions.

Risk: Target category and review calls can be slow, and broad parallel fan-out may hit concurrency limits.

Mitigation: Use long client timeouts, background execution for interactive workflows, and conservative concurrency.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/target-product-data)
- [Scavio Target Search Documentation](https://scavio.dev/docs/target-search)
- [Scavio Target Category Documentation](https://scavio.dev/docs/target-category)
- [Scavio Target Product Documentation](https://scavio.dev/docs/target-product)
- [Scavio Target Reviews Documentation](https://scavio.dev/docs/target-reviews)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline shell and Python examples for JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses use the envelope data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
