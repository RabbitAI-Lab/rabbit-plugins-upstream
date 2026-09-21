## Description:

Search OneHome (CoreLogic) portal listings, get property details, photos, schools, saved searches. Use when the user asks about real estate listings shared by their agent, OneHome links, portal.onehome.com properties, or specific addresses / MLS numbers they want to look up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help external users search and understand private OneHome real-estate portal listings shared by their agent, including listing details, photos, schools, saved searches, comparisons, and payment estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneHome magic links, token parameters, bearer JWTs, and signed-in browser sessions can grant private portal access.

Mitigation: Treat these values as secrets, avoid sharing them in logged channels, and redact token values from transcripts or outputs.

Risk: Expired or unavailable OneHome tokens can cause portal tool failures.

Mitigation: Run onehome_healthcheck before portal calls and refresh the token or signed-in portal interaction when needed.

Risk: Compact view removes image URLs from some responses, including media GraphQL results.

Mitigation: Use view: "full" for media queries or when investigating a missing field.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/onehome)
- [Publisher Profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions]

**Output Format:** [Markdown guidance with tool names, parameters, and workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes compact/full response-shape guidance and cautions for handling private OneHome access tokens.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
