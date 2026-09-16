## Description:

Searches OneHome (CoreLogic) portal listings and helps retrieve property details, photos, schools, saved searches, comparisons, and local mortgage or affordability calculations for agent-shared real-estate portals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and inspect real-estate listings shared through a OneHome portal, including property details, photos, schools, saved searches, comparisons, and mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private OneHome portal data available through a bearer token, magic link, or signed-in browser session.

Mitigation: Install and use it only when the user intends the agent to access their OneHome portal data, and verify authentication with the healthcheck before using listing tools.

Risk: The raw GraphQL escape hatch can expose advanced access to the same portal data beyond the structured listing tools.

Mitigation: Prefer the structured OneHome tools for normal workflows and reserve raw GraphQL calls for fields the structured tools do not expose.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, API calls, Configuration]

**Output Format:** [Markdown guidance with tool names, parameters, and workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes compact/full response guidance and authentication setup notes.]

## Skill Version(s):

0.15.7 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
