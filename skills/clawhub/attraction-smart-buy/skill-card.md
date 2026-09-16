## Description:

Compares attraction ticket prices from Meituan and Tuniu, showing price differences, potential savings, booking links, attraction images, and ticket-type guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travel users and agents use this skill to search attractions, compare ticket prices across supported travel platforms, and receive purchase guidance before booking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill forwards travel search queries to external proxy services.

Mitigation: Review the data flow before deployment and disclose external query forwarding to users or operators.

Risk: The artifact includes and uses a hard-coded proxy credential.

Mitigation: Remove the embedded token, rotate the exposed credential, and load credentials from a managed secret or environment variable.

Risk: The skill description and implementation make inconsistent claims about the number of supported price sources.

Mitigation: Confirm the supported platforms before release and align user-facing documentation with implemented behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/attraction-smart-buy)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON with attraction search results, ticket price comparisons, booking URLs, and advisory signals.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include external booking links, image URLs, platform price differences, savings estimates, unmatched-platform notices, and ticket-type recommendations.]

## Skill Version(s):

3.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
