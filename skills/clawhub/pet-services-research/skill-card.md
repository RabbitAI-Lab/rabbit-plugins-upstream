## Description:

Researches public Rover sitter and trainer profiles through the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to discover Rover pet sitters, dog walkers, and trainers by location, then inspect public provider profiles as normalized JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can expose the user's Crawlora API key to a caller-selected API host.

Mitigation: Use the default Crawlora API host, do not set CRAWLORA_API_BASE unless the destination is trusted, and avoid sending precise home addresses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/pet-services-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; sends query locations and public profile identifiers to Crawlora.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
