## Description:

Search Target.com, browse a category, read product detail by TCIN and pull reviews with the rating breakdown as structured JSON. 4 endpoints, 1 credit each, store-aware pricing via store_id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search Target.com, browse Target categories, retrieve product details by TCIN, and inspect review summaries through the Scavio API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party Scavio API key and spends Scavio credits for Target lookups.

Mitigation: Confirm credit use before broad or automated requests, keep the API key in an environment variable or secret store, and avoid committing it to source control.

Risk: Target calls can be slow, with category and review requests documented around 37 to 40 seconds and retries potentially taking longer.

Mitigation: Use a client timeout of at least 120 seconds and prefer async or background execution when a user is waiting on results.

Risk: The reviews endpoint returns at most 8 review bodies, so returned review text is not the complete review corpus.

Mitigation: Present returned review bodies as a sample and rely on the rating breakdown for aggregate review coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-target)
- [Scavio Target search documentation](https://scavio.dev/docs/target-search)
- [Scavio Target category documentation](https://scavio.dev/docs/target-category)
- [Scavio Target product documentation](https://scavio.dev/docs/target-product)
- [Scavio Target reviews documentation](https://scavio.dev/docs/target-reviews)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell setup, code examples, and structured JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses use a data, response_time, credits_used, and credits_remaining envelope; Target review bodies are limited to 8 returned bodies while the rating breakdown covers all reviews.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
