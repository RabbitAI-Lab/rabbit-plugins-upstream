## Description:

Search Google Jobs for job and recruitment listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert Google Jobs search requests into Dataify Scraper API calls and return job listing results. It supports structured parameters, natural-language search requests, preview tables, and raw JSON or HTML output when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live searches send job-search parameters and a Dataify API token to Dataify.

Mitigation: Configure DATAIFY_API_TOKEN in the environment and avoid sharing tokens in chat or command arguments.

Risk: Searches may consume Dataify credits, especially when requesting multiple pages or bypassing cache.

Mitigation: Review consequential search scope, pagination, and cache-bypass settings before execution.

## Reference(s):

- [Dataify Google Jobs API](artifact/references/google_jobs_api.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-jobs)
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration guidance]

**Output Format:** [Markdown, parameter tables, raw JSON, raw HTML, or shell command examples depending on the request.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Dataify API token for live API calls; previews and dry runs can show normalized parameters without calling the API.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
