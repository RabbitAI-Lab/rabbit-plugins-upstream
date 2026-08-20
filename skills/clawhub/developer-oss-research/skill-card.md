## Description:

Researches GitHub repos/users/orgs and Chrome Web Store extensions via the Crawlora API - search, profiles, contributors, releases, trending, and extension detail/reviews/permissions - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to research public GitHub repositories, users, organizations, and Chrome Web Store extensions for project due diligence, trend scans, contributor and release review, and extension safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send arbitrary Crawlora API requests outside the stated GitHub and Chrome Web Store research scope.

Mitigation: Restrict usage to documented /github/... and /chromewebstore/... public-data endpoints and review requested paths before execution.

Risk: The skill requires a Crawlora API key for outbound API requests.

Mitigation: Store the key only in CRAWLORA_API_KEY; do not hardcode, log, commit, or pass it in URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/developer-oss-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public-data Crawlora endpoints and requires CRAWLORA_API_KEY for live API requests.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
