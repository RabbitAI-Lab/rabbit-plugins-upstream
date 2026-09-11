## Description:

Researches GitHub repositories, users, organizations, and Chrome Web Store extensions through the Crawlora API, returning normalized JSON for profiles, contributors, releases, trending projects, extension details, permissions, privacy, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical researchers use this skill to gather public open-source project, developer, organization, and Chrome extension data for due diligence, market discovery, maintenance checks, and extension safety review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public research queries and identifiers are sent to Crawlora using the user's API key.

Mitigation: Use the skill only for public repository, profile, organization, and extension research, and avoid submitting sensitive internal identifiers or private investigation targets.

Risk: The security review found the shell helper broader than its documented read-only endpoint catalog.

Mitigation: Review or constrain scripts/crawlora.sh before use in shared or automated environments, especially to reject POST and enforce exact documented paths when write-like requests are not needed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/developer-oss-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; list endpoints are paginated.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
