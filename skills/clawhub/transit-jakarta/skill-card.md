## Description:

Helps agents answer TransJakarta stop, route, and live bus arrival questions using a public transit service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jrrqd](https://clawhub.ai/user/jrrqd)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and assistants use this skill to find TransJakarta stops and routes, check bus arrival estimates, and review live service information around Jakarta.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live arrival estimates may be stale or unavailable when the transit feed is delayed or unreachable.

Mitigation: Check the reported update time and confirm time-sensitive journeys against current transit information.

Risk: Broad bus-related trigger wording may activate this skill for unrelated bus questions.

Mitigation: Use it only for TransJakarta-related requests, or narrow its activation wording.

## Reference(s):

- [Transit Jakarta on ClawHub](https://clawhub.ai/jrrqd/skills/transit-jakarta)
- [Transit Jakarta public transit service](https://transit.oyenza.com)
- [TransJakarta GTFS data](https://gtfs.transjakarta.co.id/files/file_gtfs.zip)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain-text transit results and concise answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live arrival estimates depend on the transit service; stop and route metadata may be cached locally.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
