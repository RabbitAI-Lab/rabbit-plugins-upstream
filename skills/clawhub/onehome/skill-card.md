## Description:

Search OneHome (CoreLogic) portal listings, get property details, photos, schools, saved searches. Use when the user asks about real estate listings shared by their agent, OneHome links, portal.onehome.com properties, or specific addresses / MLS numbers they want to look up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to inspect real-estate listings shared through a private OneHome portal, including property details, photos, schools, saved searches, comparisons, and mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated OneHome access can expose private portal sessions, listing activity, bearer tokens, or magic links.

Mitigation: Install only when that access is acceptable, treat tokens and captured sessions as secrets, and run a health check before use to confirm the intended authentication mode.

Risk: The raw GraphQL escape hatch and full response views can expose private account or portal fields beyond the immediate listing question.

Mitigation: Prefer structured listing tools, use compact views by default, and request full views or raw GraphQL only when the needed listing data is unavailable through scoped tools.

Risk: Media queries through the raw GraphQL path can appear successful while compact mode strips image URLs.

Mitigation: Use the dedicated photos tool for listing images, or explicitly request full view for media-specific GraphQL queries.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text summaries with structured tool-call inputs and outputs when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing details, comparisons, photos, school and walkability data, user or portal fields, and local mortgage or affordability calculations depending on the requested workflow.]

## Skill Version(s):

0.15.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
