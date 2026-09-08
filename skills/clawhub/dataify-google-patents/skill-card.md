## Description:

Search Google Patents for patent records. Do not use for Google Scholar papers or general web results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to convert Google Patents search requests into Dataify Scraper API calls and receive compact patent-search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and the Dataify API token are sent to Dataify for patent searches.

Mitigation: Review the skill before installing, configure the token only in the environment, and avoid submitting sensitive search terms.

Risk: The Google Patents-only description conflicts with code and instructions that can include Google Scholar results.

Mitigation: Remove Scholar support or clearly disclose and control Scholar inclusion before release.

## Reference(s):

- [Dataify Google Patents API Reference](references/google_patents_api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Markdown, JSON]

**Output Format:** [Markdown with inline bash commands; compact text summaries by default, with raw JSON or HTML only when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN for live Dataify requests; preserves source links and avoids exposing the full token.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
