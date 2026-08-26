## Description:

Researches GitHub repos, users, orgs, and Chrome Web Store extensions via the Crawlora API, including search, profiles, contributors, releases, trending repositories, extension details, reviews, and permissions, and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical reviewers use this skill to research public GitHub projects, developers, organizations, and Chrome Web Store extensions for due diligence, trend monitoring, contributor analysis, release review, extension permission checks, and similar open-source research tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send arbitrary requests and payloads to Crawlora or another configured API base.

Mitigation: Review before installing, use a scoped Crawlora API key, and restrict automated use to the documented GitHub and Chrome Web Store endpoints.

Risk: Prompts or request bodies may include sensitive data that would be sent to an external API.

Mitigation: Avoid placing secrets, private source, or sensitive personal data in Crawlora request parameters or bodies.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/developer-oss-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API calls; list endpoints are paginated.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
