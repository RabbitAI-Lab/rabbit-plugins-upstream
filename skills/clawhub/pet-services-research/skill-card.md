## Description:

Researches public Rover sitter and trainer profiles through the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to discover Rover pet sitters, dog walkers, and trainers by location, then inspect public provider profiles as normalized JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rover search terms, profile slugs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only in trusted environments with an intended Crawlora API key, and avoid placing private notes or secrets in query or body arguments.

Risk: Returned Rover data is public marketplace information rather than verified background-check data.

Mitigation: Use results for discovery and profile research, then verify provider suitability through appropriate channels before acting on them.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API setup](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/pet-services-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; returns normalized public Rover listing and profile data from Crawlora.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
