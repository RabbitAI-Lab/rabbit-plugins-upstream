## Description:

Search OneHome (CoreLogic) portal listings, get property details, photos, schools, saved searches. Use when the user asks about real estate listings shared by their agent, OneHome links, portal.onehome.com properties, or specific addresses / MLS numbers they want to look up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help buyers work with private OneHome portal listings shared by a real-estate agent, including listing search, property details, photos, schools, saved searches, comparisons, and local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private OneHome access can expose buyer, listing, and account data through bearer tokens, magic links, or captured browser sessions.

Mitigation: Treat ONEHOME_TOKEN values, OneHome magic links, and captured browser sessions like passwords, and refresh or remove access when it is no longer needed.

Risk: Broad authenticated GraphQL access can return more data than the user intended.

Mitigation: Prefer the structured OneHome tools over onehome_graphql unless raw GraphQL access is intentionally required.

Risk: Compact responses intentionally strip media URLs, which can hide photos in media-focused queries.

Mitigation: Use full view for media queries or when investigating missing payload fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Markdown or plain text responses with structured tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact or full result views depending on the requested OneHome data; media queries require full view when image URLs are needed.]

## Skill Version(s):

0.15.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
