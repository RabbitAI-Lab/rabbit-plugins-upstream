## Description:

Finds package tours, hotels, flights, trains, and activities in Russian travel catalogs, with prices and booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[missial](https://clawhub.ai/user/missial)

### License/Terms of Use:

MIT

## Use Case:

Travelers and travel-planning agents use this skill to find tours, lodging, transport, and activities with prices and links for trip planning. It does not make bookings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel search criteria are sent to an external service.

Mitigation: Send only necessary search criteria; omit names, contact details, passport and payment details, and credentials.

Risk: Listed prices and availability may change before booking.

Mitigation: Verify final prices and availability with the linked providers before booking.

## Reference(s):

- [Travel Search RU on ClawHub](https://clawhub.ai/missial/skills/travel-search-ru)
- [Travel Search CLI usage](references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown travel options with prices, key details, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are informational; prices and availability require provider confirmation.]

## Skill Version(s):

2.5.0 (source: skill metadata, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
