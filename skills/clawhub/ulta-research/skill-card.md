## Description:

Researches Ulta Beauty's catalog, including categories, products, shades, questions, reviews, and nearby stores, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research Ulta Beauty products, categories, shade variants, product questions, customer reviews, and nearby stores before making recommendations or presenting catalog results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses the user's Crawlora API key and sends Ulta-related queries to Crawlora.

Mitigation: Use the skill only in trusted environments, keep CRAWLORA_API_KEY out of code and logs, and review requested API calls before execution.

Risk: The security evidence flags the release as suspicious because the helper can send undocumented POST requests with the user's Crawlora API key.

Mitigation: Prefer a revised version that rejects POST, validates product IDs as a single path segment, and exposes only the documented GET endpoints before use in automated or untrusted-content workflows.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown usage guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses paginated Crawlora API responses.]

## Skill Version(s):

1.0.13 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
