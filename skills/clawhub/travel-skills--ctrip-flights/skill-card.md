## Description:

Searches Ctrip for domestic flights in China, including prices, airline schedules, aircraft types, route comparisons, and low-price calendars.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to search Ctrip domestic flights in China, compare prices across city or province routes, and return low-price calendar results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill currently disables HTTPS certificate and hostname verification when calling Ctrip endpoints.

Mitigation: Review before installing and update the script to use normal TLS verification before routine use.

Risk: The skill caches generated cookie identifiers locally and sends flight search details to Ctrip.

Mitigation: Disclose the local cookie cache behavior, minimize retained identifiers, and clear cached data when it is no longer needed.

Risk: The skill relies on reverse-engineered signing code for Ctrip requests.

Mitigation: Review compatibility and terms before deployment, and monitor the signing dependency for breakage or changed behavior.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown tables or structured JSON emitted by a Python CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include query metadata, per-route summaries, best-route selection, direct and transfer flights, and low-price calendar entries.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
