## Description:

Search Google News for current news results. Do not use for general Google web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert Google News requests into Dataify Scraper API calls and return compact news results with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package contains broader data-collection workflows beyond the advertised Google News search task.

Mitigation: Review the bundled scripts before installation and limit routine use to the documented Google News workflow unless the broader workflows are intentionally needed.

Risk: Dataify API credentials could be exposed or misused if handled through chat text or command arguments.

Mitigation: Use session-scoped DATAIFY_API_TOKEN setup, do not paste tokens into chat, and avoid passing tokens directly on the command line.

Risk: Generated preview or resume shell commands may perform actions the user did not intend if run without inspection.

Mitigation: Inspect generated shell commands before execution and confirm any high-volume, multi-page, or cost-affecting request first.

## Reference(s):

- [Dataify Google News API Reference](references/google_news_api.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-news)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, JSON, Guidance]

**Output Format:** [Markdown summaries with optional raw JSON or HTML when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns compact user-facing news titles, links, selected vertical fields, counts, and truncation notes; raw response formats are only returned on explicit request.]

## Skill Version(s):

1.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
