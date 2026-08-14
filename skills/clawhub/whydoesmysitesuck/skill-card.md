## Description:

Grade any website 0-100 across categories like SEO, security, performance, accessibility, content, email auth and AI/LLM readiness, using the free whydoesmysitesuck.com API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and external auditors use this skill to request a website quality baseline, compare domains, or check whether changes improved SEO, security, performance, accessibility, content, email authentication, and AI/LLM readiness signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting a domain sends it to an external audit API and may trigger a live crawl.

Mitigation: Use the skill only for domains the user owns or is authorized to assess, and tell the user when an external crawl is being requested.

Risk: API key registration can require an email address.

Mitigation: Ask the user for their own email before registration and do not invent or substitute an address.

Risk: Website scores can be stale or incomplete if a scan is refreshing, failed, or not yet ready.

Mitigation: Report API status accurately, respect Retry-After guidance, avoid retry loops, and do not invent scores when the call fails.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/marcindudekdev/skills/whydoesmysitesuck)
- [whydoesmysitesuck.com](https://whydoesmysitesuck.com)
- [whydoesmysitesuck.com API documentation](https://whydoesmysitesuck.com/api)
- [whydoesmysitesuck.com OpenAPI specification](https://whydoesmysitesuck.com/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a numeric score, letter grade, weakest categories, and a report URL returned by the external API.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
