## Description:

Researches public Rover sitter and trainer profiles through the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to discover public Rover sitters, dog walkers, and trainers by location, then inspect public provider profiles as normalized JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the Crawlora API key and pet-service search details such as locations or profile slugs to Crawlora.

Mitigation: Use the skill only when Crawlora is an acceptable API provider for the request and avoid sending sensitive or unnecessary search details.

## Reference(s):

- [pet-services-research endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key setup](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/pet-services-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET-only Rover endpoints.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
