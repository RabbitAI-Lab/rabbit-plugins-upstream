## Description:

Search OneHome (CoreLogic) portal listings, get property details, photos, schools, saved searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to search private OneHome portal listings, inspect property details, retrieve photos and school information, compare listings, and run local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private OneHome portal listings when configured with a magic link or ONEHOME_TOKEN.

Mitigation: Install only when the agent should access those listings, and treat magic links and ONEHOME_TOKEN values as credentials.

Risk: Raw GraphQL access can request fields outside the structured OneHome tools.

Mitigation: Prefer the structured OneHome tools and use raw GraphQL only when a needed field is missing.

Risk: OneHome JWTs expire and may cause failed or stale listing lookups.

Mitigation: Run onehome_healthcheck before use and refresh the token when expiry is near or authentication fails.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration]

**Output Format:** [Markdown guidance with tool-call parameters and credential setup details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires access to a private OneHome portal token or magic link for listing data; mortgage and affordability calculations are local.]

## Skill Version(s):

0.14.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
