## Description:

Helps users search their agent-shared OneHome listings and retrieve property details, photos, schools, saved searches, and comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers and their agents use this skill to explore private OneHome listings, compare properties, review photos and schools, and estimate mortgage payments or affordability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private OneHome listing and account information may be exposed through portal access.

Mitigation: Enable the skill only when authorized to access the user's private OneHome portal data.

Risk: A magic-link token or signed-in browser session can grant access to private portal data.

Mitigation: Keep ONEHOME_TOKEN and ONEHOME_MAGIC_LINK secret, redact token query parameters, and use browser capture only when the user intends to use their signed-in session.

## Reference(s):

- [OneHome skill on ClawHub](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include listing details, photo links, school information, comparisons, and locally calculated affordability estimates.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
