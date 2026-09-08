## Description:

Run a Yandex web search. Do not use when the user explicitly requests Google, Bing, or DuckDuckGo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Yandex searches through Dataify and receive search results or raw output when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence security summary reports an under-scoped raw API override that can bypass the advertised Yandex-only search behavior.

Mitigation: Restrict or remove raw parameter overrides before installation, especially where Dataify tokens have spending limits or broader account privileges.

Risk: The skill can spend Dataify API credits when live searches are executed.

Mitigation: Use low-volume defaults, review high-volume or multi-page requests before execution, and keep API tokens out of chat and output.

## Reference(s):

- [Dataify Yandex Search API Fields](references/api_fields.md)
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request)
- [Dataify Yandex Search on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-yandex-search)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, JSON, Guidance]

**Output Format:** [Markdown parameter previews and Yandex search results as compact prose, JSON, or HTML depending on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Dataify API token for live API calls; raw JSON or HTML should be returned only when explicitly requested.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
