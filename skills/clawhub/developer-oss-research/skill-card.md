## Description:

Researches GitHub repositories, users, organizations, and Chrome Web Store extensions through the Crawlora API, returning normalized JSON for profiles, contributors, releases, trending projects, extension details, permissions, privacy, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and technical evaluators use this skill to research public GitHub projects, maintainers, organizations, releases, and Chrome Web Store extensions before dependency, marketplace, or security decisions. It is suited for public open-source and extension due diligence where normalized Crawlora API results are preferred over direct site scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub or Chrome Web Store search terms, identifiers, and request metadata are sent to Crawlora under the user's API key.

Mitigation: Avoid submitting secrets, private repository names, private identifiers, or sensitive internal research terms in API queries.

Risk: The helper relies on curl URL handling and the security evidence recommends tighter protection against URL glob expansion.

Mitigation: Review commands before execution and prefer adding curl --globoff or stricter path-segment validation before broad deployment.

Risk: Results cover public data and may be paginated, rate limited, or incomplete if only one page is queried.

Mitigation: Walk documented page and per_page parameters for complete coverage and treat results as public-source signals requiring human review for high-impact decisions.

Risk: The skill requires a Crawlora API key in the environment.

Mitigation: Keep CRAWLORA_API_KEY out of code, command lines, logs, query parameters, and committed files.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/developer-oss-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and only queries public GitHub and Chrome Web Store data through documented Crawlora routes.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
