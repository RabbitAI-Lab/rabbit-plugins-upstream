## Description:

Searches Facebook Marketplace listings and looks up public Facebook Page details (name, follower/like counts, category, contact info) via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to search public Facebook Marketplace listings for location/category research and to retrieve public Facebook Page profile details for business or lead enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call arbitrary Crawlora API paths and methods with the user's API key, broader than the Facebook-only skill description.

Mitigation: Review or restrict scripts/crawlora.sh to the documented Facebook GET endpoints before using it with a paid or sensitive API key.

Risk: The skill requires a Crawlora API key for external API calls.

Mitigation: Provide the key through CRAWLORA_API_KEY only, and do not hardcode, pass in query parameters, or commit the key.

Risk: Marketplace results are limited to public, single-page server-rendered data and may be slow in the worst case.

Mitigation: Set user expectations that pagination requiring login is out of scope and that some marketplace searches may take up to roughly a minute.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Publisher Profile](https://clawhub.ai/user/tonywangcn)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/facebook-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands that return JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; documented Facebook endpoints return public Marketplace and Page data only.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
