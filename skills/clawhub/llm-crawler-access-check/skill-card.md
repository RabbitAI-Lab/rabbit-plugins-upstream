## Description:

Check whether a website's robots.txt allows the AI crawlers that decide visibility in ChatGPT Search, Perplexity, Claude, Gemini, and Microsoft Copilot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxaeo](https://clawhub.ai/user/maxaeo)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners, marketers, SEO/AEO teams, and developers use this skill to inspect robots.txt access for AI search and assistant crawlers and identify the exact rules to change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes network requests to the user-specified domain and may consult crawler documentation.

Mitigation: Use it only for public robots.txt checks and keep access limited to robots.txt plus crawler reference documentation.

Risk: robots.txt results do not prove that crawlers can pass WAF, CDN bot rules, IP reputation controls, or other server-side blocking.

Mitigation: Treat the output as a first-gate access check and verify server-side bot controls separately when reachability matters.

Risk: Crawler user-agent names and operator policies can change over time.

Mitigation: Confirm the crawler list against the linked methodology and operator documentation before relying on a final recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maxaeo/skills/llm-crawler-access-check)
- [MaxAEO homepage](https://maxaeo.ai/)
- [MaxAEO crawler matrix](https://maxaeo.ai/geo-method/)

## Skill Output:

**Output Type(s):** [analysis, markdown, configuration, guidance]

**Output Format:** [Markdown table with verdict, exact robots.txt lines, and concise remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only review of a site's public robots.txt file; no account, API key, or private file access is expected.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
