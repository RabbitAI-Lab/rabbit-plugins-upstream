## Description:

Collect structured Glassdoor company information from known Glassdoor company URLs while avoiding job-search results and Indeed company URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent prepare and run Dataify Builder requests for Glassdoor company collection from provided company URLs, then monitor the asynchronous task and return the final JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marked suspicious because runtime instructions expose broader Glassdoor company and job-listing scraper modes than the company-URL description.

Mitigation: Constrain use to glassdoor_company_by-url unless the user explicitly requests and accepts a broader Dataify scraper mode.

Risk: The skill sends requests to external Dataify services and may consume account credits.

Mitigation: Confirm high-volume, multi-page, or scope-changing requests before submission, and verify token presence without displaying the token value.

Risk: Persistent API-token setup can leave long-lived credentials in a user's shell environment.

Mitigation: Prefer session-scoped setup for short-term use and ensure persistent configuration is reviewed by the user before adding it to shell startup files.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/dataify-server/skills/dataify-glassdoor-company-by-url)
- [Dataify scraper parameter catalog](artifact/references/tool-params.json)
- [Dataify Builder API endpoint](https://scraperapi.dataify.com/builder)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with curl commands, setup guidance, task status, and JSON collection results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID and resume command when monitoring times out or when submission-only behavior is requested.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
