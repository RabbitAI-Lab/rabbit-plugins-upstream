## Description:

Search OneHome (CoreLogic) portal listings, get property details, photos, schools, saved searches. Use when the user asks about real estate listings shared by their agent, OneHome links, portal.onehome.com properties, or specific addresses / MLS numbers they want to look up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate buyers use this skill to work with listings, saved searches, photos, schools, and comparisons from their authorized OneHome portal access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private OneHome portal data through magic links, bearer tokens, or captured browser sessions.

Mitigation: Use only with authorized OneHome sessions and treat magic links, bearer tokens, and captured sessions like passwords.

Risk: Default compact responses strip image and avatar URLs, which can make media-focused GraphQL results appear incomplete.

Mitigation: Request full responses when retrieving media or diagnosing missing fields.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, text, configuration]

**Output Format:** [Markdown and structured tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated OneHome MCP calls and local mortgage or affordability calculations.]

## Skill Version(s):

0.15.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
