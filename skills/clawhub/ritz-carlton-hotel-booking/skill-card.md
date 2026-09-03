## Description:

Searches Ritz-Carlton hotels in Marriott-related inventory and returns prices, hotel details, package offers, and booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel agents use this skill to search Ritz-Carlton hotels by city, review hotel details, compare package offers, and get booking links from the packaged travel-data source.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel search details are sent to an under-disclosed third-party proxy service.

Mitigation: Install only if that data sharing is acceptable; avoid sensitive travel plans unless the publisher documents the proxy operator, data handling, and token management.

Risk: The skill may activate from casual Ritz-Carlton brand mentions rather than explicit booking intent.

Mitigation: Confirm the user intends to search or book Ritz-Carlton hotels before invoking the tools.

Risk: Hotel prices, details, and booking links may become misleading if the agent supplements or edits script output.

Mitigation: Present only returned hotel names, prices, details, and booking links, and avoid adding outside assumptions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/travel-skills/skills/ritz-carlton-hotel-booking)
- [Publisher profile](https://clawhub.ai/user/travel-skills)
- [Packaged proxy service endpoint](https://1439498936-6sysdjjt99.ap-guangzhou.tencentscf.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown/plain text hotel results with booking links and CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hotel and package results are limited by script parameters and should be presented without inventing or modifying returned data.]

## Skill Version(s):

1.1.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
