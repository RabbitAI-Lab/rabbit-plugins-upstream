## Description:

Search and compare flights with the Ktemia flight search API - one-way, round trip, or multi-city - and return fares from each seller with booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ktemiainc](https://clawhub.ai/user/ktemiainc)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers use this skill to compare one-way, round-trip, and multi-city fares, look up airport or airline codes, and get seller booking links. It asks for missing trip details instead of guessing; purchases are completed on the seller's site.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trip searches are sent to an external flight API and require an API key.

Mitigation: Review the service's data handling and the host's permission controls before use; provide only the trip details needed for the search.

Risk: The security scan has partial coverage because a local reference was missing.

Mitigation: Review the complete release and the missing reference before relying on the scan verdict.

## Reference(s):

- [Ktemia Flight Search API](https://www.ktemia.com/docs/api/flights/search/)
- [Ktemia API Reference](https://www.ktemia.com/docs/api/)
- [Ktemia API Authentication](https://www.ktemia.com/docs/api/#authentication)
- [Ktemia API Errors](https://www.ktemia.com/docs/api/#errors)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Concise flight comparisons with itinerary details, prices, and seller booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices may change; the skill provides booking links and does not book tickets.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; supplied SKILL.md declares 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
