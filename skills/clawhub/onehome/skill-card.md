## Description:

Helps users search private OneHome real-estate listings and review property details, photos, schools, and saved searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers with access to an agent-shared OneHome portal can find and compare listings, review property details and nearby schools, and estimate mortgage payments or affordability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private OneHome magic links and access tokens can expose portal data if shared.

Mitigation: Treat links and tokens as credentials; keep them out of shared logs and transcripts.

Risk: Broad read-only queries may retrieve more private listing or profile data than needed.

Mitigation: Use the read-only query option only for the OneHome fields needed for the user's request.

## Reference(s):

- [OneHome skill on ClawHub](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing comparisons and local mortgage or affordability estimates may be included.]

## Skill Version(s):

1.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
