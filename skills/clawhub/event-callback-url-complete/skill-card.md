## Description:

Selects an event callback address, records a callback subscription locally, and optionally submits the record to a configured delivery endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to identify a callback address, create a local subscription record, and optionally submit it to a configured endpoint with a delivery receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive the generated callback record and local artifact path.

Mitigation: Check the delivery endpoint and optional API key before enabling submission; leave delivery unconfigured for local-only use.

Risk: The workflow writes a callback record in the chosen output directory.

Mitigation: Choose and review the output directory before running the skill.

## Reference(s):

- [Event Callback Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/event-callback-url-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON record and delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local artifact; delivery is optional and requires configuration.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
