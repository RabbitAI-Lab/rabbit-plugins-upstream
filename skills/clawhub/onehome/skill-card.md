## Description:

Helps agents search private OneHome property listings and retrieve listing details, photos, schools, and saved searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers and their agents use this skill to review privately shared OneHome listings, compare properties, and check related property information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private OneHome listings and bearer credentials may be exposed through magic links, JWTs, or token-bearing URLs.

Mitigation: Use only when private portal access is intended; treat credentials and token-bearing URLs as secrets and avoid sharing them unnecessarily.

Risk: Portal access through the connected tool may exceed the intended read-only lookup.

Mitigation: Prefer read-only listing lookups unless the connected tool's behavior is understood.

## Reference(s):

- [OneHome skill release on ClawHub](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing details, property comparisons, school information, and affordability calculations.]

## Skill Version(s):

1.1.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
