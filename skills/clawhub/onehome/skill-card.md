## Description:

Search OneHome (CoreLogic) portal listings, get property details, photos, schools, saved searches. Use when the user asks about real estate listings shared by their agent, OneHome links, portal.onehome.com properties, or specific addresses / MLS numbers they want to look up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate-focused agents use this skill to work with OneHome listing data shared through a private agent portal, including searches, property details, photos, schools, walkability, saved searches, comparisons, and mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneHome magic links, bearer tokens, and signed-in portal sessions can expose private listing data shared by a real-estate agent.

Mitigation: Treat OneHome links and tokens as private credentials, use only accounts or sessions the user is authorized to access, and avoid sharing token-bearing URLs.

Risk: The raw GraphQL escape hatch can request fields beyond the structured OneHome tools.

Mitigation: Prefer the structured tools for normal listing, photo, school, walkability, and comparison tasks; use raw GraphQL only when a needed field is unavailable through those tools.

Risk: Expired or stale OneHome tokens can cause failed or incomplete listing lookups.

Mitigation: Run the health check before portal operations and refresh the token or portal capture when expiry is near or authentication fails.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with tool-call guidance and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing summaries, property comparisons, authentication setup guidance, raw GraphQL examples, and local mortgage or affordability calculations.]

## Skill Version(s):

0.13.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
