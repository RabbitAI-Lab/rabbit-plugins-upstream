## Description:

Search Etsy listings, pull one listing with its variations and reviews, open a shop's profile and catalogue, and page through a shop's reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to search Etsy products, inspect listings, review shop profiles and catalogues, and retrieve shop review data for ecommerce research and price comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Etsy lookup requests are sent to Scavio using SCAVIO_API_KEY.

Mitigation: Keep the API key in an environment variable or secret store and do not commit it to source control.

Risk: Each Etsy endpoint call consumes API credits, including calls that return empty results.

Mitigation: Confirm query parameters before making requests and widen filters only when needed.

Risk: Returned review text is written by real Etsy buyers.

Mitigation: Summarize review content and avoid building profiles of individual reviewers.

## Reference(s):

- [Scavio API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/etsy-product-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and optional Python or curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Etsy endpoint calls consume Scavio API credits.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
