## Description:

Research app-market opportunities using Crawlora app catalogs, historical charts, live store listings, release notes, reviews, and Google Trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, product teams, and market researchers use this skill to assess app niches, compare competitors, inspect chart and review signals, and form evidence-backed unmet-need hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can send the API key and request data to an endpoint set through CRAWLORA_API_BASE.

Mitigation: Run the skill only where CRAWLORA_API_BASE cannot be set by untrusted project files, shell profiles, CI settings, or wrappers; prefer pinning or validating the Crawlora production host before sending credentials.

Risk: App rank, review, and Trends samples can be mistaken for market size, downloads, revenue, or causal release impact.

Mitigation: Report sampling bounds and conflicting evidence, compare only like-for-like chart definitions, and separate opportunity hypotheses from demonstrated demand or forecasts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/tonywangcn/skills/app-market-opportunity-research)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with optional shell command examples and evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Opportunity briefs should keep data freshness, sampling bounds, assumptions, and unavailable sources visible.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
