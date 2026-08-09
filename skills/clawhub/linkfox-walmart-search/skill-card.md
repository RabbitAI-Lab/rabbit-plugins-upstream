## Description:

Searches Walmart product listings by keyword, category, price range, sort order, store, and device view, then returns structured listing data for e-commerce research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce sellers, and marketplace researchers use this skill to search Walmart listings, compare prices, check availability, and inspect seller, rating, shipping, and sponsored-placement signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox handles Walmart search queries, API keys, phone-number SMS login, and payment-plan workflows.

Mitigation: Install only if the publisher is trusted; prefer self-service account setup and avoid sharing OTPs unless necessary.

Risk: Endpoint environment variables can affect where requests are sent.

Mitigation: Verify LinkFox endpoint environment variables before use and keep API keys scoped to the intended service.

Risk: Generated API keys and saved response files may contain sensitive account or marketplace research data.

Mitigation: Treat API keys and saved response files as sensitive, store them only in trusted workspaces, and remove them when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-walmart-search)
- [Walmart Search API reference](references/api.md)
- [Authentication and credits onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables with JSON snippets and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save complete Walmart API responses in the workspace while printing summaries for larger responses.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
