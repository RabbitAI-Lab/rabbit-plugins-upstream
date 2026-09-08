## Description:

Researches Target catalog categories, products, filters, prices, questions, and reviews through the Crawlora API and returns normalized JSON for product search, browsing, comparison, Q&A, and review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting external users and developers use this skill to search and browse public Target catalog data, compare prices and availability, and summarize product details, Q&A, and reviews using Crawlora instead of direct HTML scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a generic authenticated Crawlora helper that can make requests beyond the Target endpoints documented for this workflow.

Mitigation: Use the helper only for the documented Target GET endpoints, or restrict it before installation if broader Crawlora access is not intended.

Risk: The Crawlora API key may be exposed or sent to an unintended destination if configuration is mishandled.

Mitigation: Keep the key in CRAWLORA_API_KEY, avoid hardcoding or committing it, and set CRAWLORA_API_BASE only when the destination is fully trusted.

## Reference(s):

- [Target endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/target-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples and JSON-oriented API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Crawlora API requests and normalized JSON fields to inspect; API responses are paginated.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
