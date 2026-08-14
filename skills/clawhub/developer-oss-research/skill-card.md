## Description:

Researches GitHub repos, users, orgs, and Chrome Web Store extensions via the Crawlora API, including search, profiles, contributors, releases, trending results, extension details, reviews, and permissions, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and analysts use this skill to research public GitHub projects, users, organizations, and Chrome Web Store extensions before dependency, market, or safety decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and identifiers are sent to Crawlora using the user's API key.

Mitigation: Use only public or approved inputs and avoid confidential repository, developer, or extension identifiers when strict data-boundary controls are required.

Risk: The helper script can call Crawlora API paths beyond the documented GitHub and Chrome Web Store endpoints.

Mitigation: Constrain use to the documented /github and /chromewebstore endpoint families and review proposed commands before execution.

Risk: Results come from live third-party API responses used for OSS and extension research.

Mitigation: Treat outputs as research signals and verify high-impact decisions against primary sources before acting.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and calls Crawlora endpoints for public GitHub and Chrome Web Store data.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
