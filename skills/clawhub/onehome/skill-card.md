## Description:

Search OneHome (CoreLogic) portal listings, get property details, photos, schools, saved searches. Use when the user asks about real estate listings shared by their agent, OneHome links, portal.onehome.com properties, or specific addresses / MLS numbers they want to look up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real estate-focused agents use this skill to work with private OneHome portal listings shared by an agent, including listing search, property details, photos, schools, saved searches, comparisons, and affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad authenticated access to private OneHome portal data beyond narrow listing lookups.

Mitigation: Install only when the agent should use the user's private OneHome portal access, and avoid raw GraphQL or full responses unless specifically needed.

Risk: Magic links, bearer tokens, and captured browser sessions can expose private account or listing data if logged or shared.

Mitigation: Treat these credentials like passwords, prefer compact views when sufficient, and refresh or remove stale tokens when access is no longer needed.

## Reference(s):

- [ClawHub onehome skill page](https://clawhub.ai/chrischall/skills/onehome)
- [OneHome portal](https://portal.onehome.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown or text with structured OneHome tool results and optional local calculation outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include private listing, saved-search, user, school, walkability, media, or affordability data depending on authenticated access and requested view.]

## Skill Version(s):

0.15.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
