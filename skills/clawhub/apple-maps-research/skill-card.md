## Description:

Researches places, categories, guides, routes, transit, and travel times through Apple Maps via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Apple Maps places, retrieve place details and photos, browse Apple Guides, reverse-geocode coordinates, and produce route, transit, and ETA research from Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apple Maps searches, precise coordinates, route endpoints, and ETA inputs are sent to Crawlora.

Mitigation: Use only when sharing those query details with Crawlora is acceptable for the deployment context.

Risk: The helper can send the Crawlora API key to a caller-controlled API base if CRAWLORA_API_BASE is influenced by untrusted content.

Mitigation: Keep CRAWLORA_API_BASE fixed to the trusted Crawlora API base and treat CRAWLORA_API_KEY as a secret.

Risk: The helper can make broader authenticated Crawlora requests than the Apple Maps endpoints documented for the skill.

Mitigation: Prefer deployments that allowlist Apple Maps endpoints and review generated shell commands before execution.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/apple-maps-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses may include Apple Maps place, guide, coordinate, route, transit, photo, and ETA data.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
