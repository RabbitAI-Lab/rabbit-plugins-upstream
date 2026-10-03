## Description:

Search OneHome portal listings and retrieve property details, photos, schools, and saved searches shared by a real-estate agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers and their agents use this skill to explore privately shared OneHome listings, compare properties, review photos and nearby schools, and estimate housing costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneHome tokens, magic links, and captured sessions grant access to private portal information.

Mitigation: Keep these credentials private; avoid pasting or logging them unnecessarily and grant portal access only when intended.

Risk: Raw portal queries may retrieve more private data than needed for a listing request.

Mitigation: Prefer structured OneHome tools; use raw read-only GraphQL only when a required field is missing.

## Reference(s):

- [OneHome skill on ClawHub](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing details and comparisons, photos and school information, and local mortgage or affordability estimates.]

## Skill Version(s):

1.1.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
