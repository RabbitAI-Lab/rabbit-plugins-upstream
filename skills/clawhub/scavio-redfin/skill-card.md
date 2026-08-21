## Description:

Search Redfin listings for sale, sold or for rent, pull one property in full with the Redfin Estimate and MLS fact sheet, and read housing-market stats for a region. 3 endpoints, 1 credit each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Redfin listings, inspect full property records, and gather regional housing-market statistics through Scavio's Redfin API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Redfin search parameters and property URLs are sent to Scavio for API requests.

Mitigation: Confirm the user is comfortable sharing those query details with Scavio before using the integration.

Risk: Every endpoint call spends Scavio credits.

Mitigation: Prefer deliberate, well-scoped requests and confirm credit usage expectations before making calls.

Risk: The Scavio API key could be exposed if placed in source code or shared output.

Mitigation: Keep SCAVIO_API_KEY in environment variables or a secret store, not in source code.

## Reference(s):

- [Scavio Redfin documentation](https://scavio.dev/docs/redfin-search)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-redfin)
- [ClawHub publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with API request examples and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses one Scavio credit per endpoint call.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
