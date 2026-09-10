## Description:

Searches OneHome (CoreLogic) portal listings, property details, photos, schools, and saved searches when the user asks about agent-shared real estate listings, OneHome links, portal.onehome.com properties, addresses, or MLS numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to work with private OneHome listing groups, retrieve listing details, photos, schools, walkability, and saved searches, compare listings, and estimate mortgage or affordability from data they are authorized to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneHome tokens and magic links can provide access to private portal listing data under the user's account.

Mitigation: Treat tokens and magic links like passwords, avoid sharing them in chat or logs, and refresh or revoke access if a token may have been exposed.

Risk: The raw GraphQL escape hatch can retrieve broader account or saved-search data than a narrow listing workflow needs.

Mitigation: Prefer structured OneHome tools for normal listing tasks and use raw GraphQL only when the user intentionally needs fields those tools do not expose.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown or structured tool-call guidance with OneHome listing summaries and calculator results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools support compact and full views; compact removes media URLs, while full preserves returned media data.]

## Skill Version(s):

0.15.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
