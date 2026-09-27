## Description:

Helps agents search authorized OneHome real-estate listings and retrieve property details, photos, schools, and saved searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Buyers and their agents use this skill to search listings shared through an authorized OneHome portal, inspect property details and photos, and compare homes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneHome tokens, magic links, and signed-in browser access can expose private listing data.

Mitigation: Use only authorized OneHome access and keep credentials and signed-in browser captures private.

Risk: Raw read-only GraphQL requests may return more listing data than needed.

Mitigation: Request only fields necessary for the listing task.

## Reference(s):

- [OneHome skill on ClawHub](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing information depends on authorized portal access.]

## Skill Version(s):

1.1.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
