## Description: <br>
Overcome LLM knowledge cutoffs with real-time developer content. daily.dev aggregates articles from thousands of sources, validated by community engagement, with structured taxonomy for precise discovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[idoshamun](https://clawhub.ai/user/idoshamun) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to retrieve current developer news, technical articles, personalized feeds, bookmarks, and topic-specific content from the daily.dev API for research, onboarding, profile setup, trend monitoring, and briefing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The daily.dev API token grants access to personalized content and could be exposed if stored or transmitted carelessly. <br>
Mitigation: Use a secrets manager, environment variable, or operating-system credential store, send the token only to api.daily.dev, and revoke it from daily.dev when no longer needed. <br>
Risk: The skill makes authenticated requests to an external daily.dev API and may hit service limits or subscription restrictions. <br>
Mitigation: Confirm the user intends to use daily.dev with a Plus subscription, handle 401, 403, and 429 responses, and respect rate-limit headers. <br>


## Reference(s): <br>
- [daily.dev Skill Page](https://clawhub.ai/idoshamun/skills/daily-dev) <br>
- [daily.dev Public API Base URL](https://api.daily.dev/public/v1) <br>
- [daily.dev Public API OpenAPI Spec](https://api.daily.dev/public/v1/docs/json) <br>
- [daily.dev Plus](https://app.daily.dev/plus) <br>
- [daily.dev API Token Settings](https://app.daily.dev/settings/api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands, HTTP endpoint references, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include authenticated daily.dev API requests and summarized developer content; the documented API rate limit is 60 requests per minute per user.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
