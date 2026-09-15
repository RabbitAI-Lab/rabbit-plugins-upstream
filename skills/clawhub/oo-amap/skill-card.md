## Description:

AMap (amap.com). Use this skill for ANY AMap request -- searching and reading data. Whenever a task involves AMap, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to make AMap searches, geocoding, route planning, location, place detail, and weather requests through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl-to-bash and irm-to-iex installer commands that execute remote scripts directly.

Mitigation: Review or replace the setup path with a safer official installer process that separates download from execution and verifies integrity; do not let an agent run these installer commands automatically.

Risk: AMap queries, addresses, coordinates, routes, weather requests, and IP-location payloads are sent through OOMOL's connector and the connected AMap service.

Mitigation: Avoid submitting sensitive location or route data unless that data sharing is acceptable for the user and deployment context.

## Reference(s):

- [ClawHub AMap skill listing](https://clawhub.ai/oomol/skills/oo-amap)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [AMap homepage](https://www.amap.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for using the oo CLI to inspect schemas and run AMap connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
