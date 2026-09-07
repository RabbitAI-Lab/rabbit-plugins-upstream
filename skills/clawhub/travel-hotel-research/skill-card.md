## Description:

Researches hotels, flights, attractions, short-term rentals, and live events through the Crawlora API, returning normalized JSON from supported travel and event platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, travel researchers, and agents use this skill to compare hotels, flights, short-term rentals, attractions, reviews, and live events across supported travel and event platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to an arbitrary API base URL if CRAWLORA_API_BASE is overridden.

Mitigation: Keep CRAWLORA_API_BASE unset or set only to the trusted Crawlora API origin, and avoid running the skill where shell profiles, CI settings, launchers, or other users can change that variable.

Risk: Travel search details are sent to Crawlora when the skill calls the API.

Mitigation: Use the skill only when sharing the requested travel, stay, review, or event query with Crawlora is acceptable.

Risk: Some Expedia POST request-body fields are documented as unconfirmed in the artifact.

Mitigation: Confirm the current Expedia request shape in Crawlora documentation or the playground before relying on those endpoints.

## Reference(s):

- [Travel Hotel Research release page](https://clawhub.ai/tonywangcn/skills/travel-hotel-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public travel, stay, review, and event data; no booking or payment actions are performed.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
