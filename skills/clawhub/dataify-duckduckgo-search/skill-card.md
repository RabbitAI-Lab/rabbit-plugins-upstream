## Description:

Run a DuckDuckGo web search. Do not use when the user explicitly requests Google, Bing, or Yandex.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run DuckDuckGo searches through Dataify, with optional region, safe-search, date, result-count, cache, and output-format controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and selected parameters are sent to Dataify.

Mitigation: Do not include secrets, credentials, or private data in search requests.

Risk: Live API calls require a Dataify API token.

Mitigation: Install and use the skill only when use of a Dataify API token is acceptable for the workspace.

Risk: Raw JSON or HTML output may expose more response detail than a compact result view.

Mitigation: Prefer compact text results by default and request raw JSON or HTML only when explicitly needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-duckduckgo-search)
- [Dataify API endpoint](https://scraperapi.dataify.com/request)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML, shell commands, guidance]

**Output Format:** [Markdown guidance and command output; search responses may be compact text, raw JSON, or raw HTML when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Dataify API token for live API calls; result count is clamped to 1..50.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
