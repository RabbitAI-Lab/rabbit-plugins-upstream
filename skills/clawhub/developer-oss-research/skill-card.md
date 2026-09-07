## Description:

Researches GitHub repositories, users, organizations, and Chrome Web Store extensions through the Crawlora API, returning normalized JSON for profiles, search results, contributors, releases, trends, extension details, permissions, privacy, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to research public GitHub projects, maintainers, organizations, and Chrome Web Store extensions before dependency, market, or extension safety decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to a configurable API destination.

Mitigation: Install only if comfortable giving the helper a Crawlora API key; prefer enforcing the documented https://api.crawlora.net/api/v1 origin and monitor how the helper is invoked.

Risk: The helper script behavior is broader than the stated GitHub and Chrome Web Store research purpose.

Mitigation: Restrict allowed paths to the documented GitHub and Chrome Web Store endpoints before operational use.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/developer-oss-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; list endpoints are paginated.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
