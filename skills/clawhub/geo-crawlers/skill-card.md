## Description:

AI crawler access analysis. Checks robots.txt, meta tags, and HTTP headers to determine which AI crawlers can access the site. Provides a complete access map and recommendations for maximizing AI visibility while maintaining appropriate control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and search visibility teams use this skill to analyze how a website handles AI crawler access and to produce recommendations for robots.txt, meta robots tags, HTTP headers, and related AI discovery files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated crawler-access recommendations could allow AI crawlers that conflict with a site's content licensing, training-data, or crawler-control requirements.

Mitigation: Review the generated robots.txt, meta tag, and HTTP header recommendations against the site's policy requirements before applying them to production.

Risk: Crawler access analysis depends on the sampled pages and the current public responses from the target website.

Mitigation: Run the analysis against representative key pages and re-check results after CDN, WAF, robots.txt, or publishing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/geo-crawlers)
- [OpenAI GPTBot documentation](https://openai.com/gptbot)
- [OpenAI crawler overview](https://docs.openai.com/bots/overview)
- [OpenAI ChatGPT-User documentation](https://openai.com/bot)
- [Anthropic ClaudeBot documentation](https://www.anthropic.com/claude-bot)
- [PerplexityBot documentation](https://perplexity.ai/perplexitybot)
- [Amazonbot documentation](https://developer.amazon.com/support/amazonbot)
- [Common Crawl FAQ](https://commoncrawl.org/faq/)
- [Content Signals specification](https://contentsignals.org/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with tables, findings, recommendations, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces GEO-CRAWLER-ACCESS.md for the analyzed domain.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
