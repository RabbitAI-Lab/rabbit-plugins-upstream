## Description:

Search Google Play, read a full Android app listing including the real install count and Data safety table, and page reviews by cursor. 3 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agent builders use this skill to search Android apps, retrieve Google Play listing metadata, inspect permissions and Data safety details, and page through reviews using Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, app IDs, and Play URLs are sent to Scavio under the user's API key.

Mitigation: Avoid confidential target lists and unnecessary URL parameters before making requests.

Risk: Google Play endpoint calls are billed at 2 credits each, and multi-page review crawls can consume credits quickly.

Mitigation: Use the 20 reviews already included in the app listing when sufficient and cap review pagination before starting a crawl.

Risk: Incorrect language or country settings can change storefront results or silently fall back to another locale.

Mitigation: Choose the intended hl and gl values explicitly and verify returned locale-sensitive fields before using them in analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-play-store-api)
- [Scavio Google Play documentation](https://scavio.dev/docs/google-play-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-play-store-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-play-store-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response descriptions and Python, JavaScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scavio endpoint calls return structured JSON envelopes and require SCAVIO_API_KEY.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
