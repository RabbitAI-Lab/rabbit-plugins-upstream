## Description:

Search agent-shared OneHome listings and retrieve property details, photos, schools, and saved searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers and their assistants use this skill to explore agent-shared OneHome listings, compare properties, view photos and school information, and estimate housing costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneHome portal access exposes private account and listing information; magic links and bearer tokens are account credentials.

Mitigation: Use only with the account holder's permission and keep links and tokens private.

Risk: Compact responses omit image and avatar URLs, including photos requested through media queries.

Mitigation: Request full view for media-heavy results or when investigating missing fields.

## Reference(s):

- [OneHome skill on ClawHub](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include property details, comparison results, photo links, school information, and housing-cost estimates.]

## Skill Version(s):

1.1.9 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
