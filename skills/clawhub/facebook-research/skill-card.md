## Description:

Searches Facebook Marketplace listings and looks up public Facebook Page details (name, follower/like counts, category, contact info) via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to gather public Facebook Marketplace listing data for a location or category and to retrieve public Facebook Page profile details for research, pricing, or lead-enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to a non-default API host if CRAWLORA_API_BASE is changed.

Mitigation: Use the default Crawlora API base unless the alternate host is fully trusted, and review the environment before running the helper.

Risk: The helper is a generic Crawlora client, not a Facebook-only wrapper.

Mitigation: Use only the documented Facebook endpoints for this skill and avoid non-Facebook paths or sensitive JSON request bodies.

Risk: Facebook lookup targets and the Crawlora API key are sent to Crawlora.

Mitigation: Install and use the skill only when sharing those lookup targets and credentials with Crawlora is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/facebook-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)
- [facebook-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns only the first page of Marketplace results.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
