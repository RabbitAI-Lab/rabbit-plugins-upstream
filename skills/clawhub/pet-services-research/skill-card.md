## Description:

Researches public Rover sitter and trainer profiles through the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to discover public Rover sitters, dog walkers, and trainers near a location, or to inspect public provider profiles as normalized JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can be reused as a broad authenticated Crawlora client beyond the Rover endpoints documented for this skill.

Mitigation: Review proposed commands before execution and restrict use to the documented Rover endpoints.

Risk: Setting CRAWLORA_API_BASE can send the API key to an overridden endpoint.

Mitigation: Set CRAWLORA_API_KEY only in trusted shells and avoid setting CRAWLORA_API_BASE unless the endpoint is explicitly trusted.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; intended for public Rover profile and search data.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
