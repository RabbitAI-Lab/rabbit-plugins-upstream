## Description:

Guides developers in deploying and using a self-hosted AI gateway that combines model routing and optional tools behind an OpenAI-compatible endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to deploy a self-hosted gateway and access enabled AI models and tools through a single endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One bearer token can grant broad control over enabled services, including code execution, browsing, and messaging.

Mitigation: Treat AIGATE_TOKEN as an admin secret; override per-service tokens before granting agents access.

Risk: Enabled services may expose sensitive host or account capabilities if the gateway is publicly reachable.

Mitigation: Enable only needed services and avoid exposing port 4000 directly to the public internet.

Risk: Starting the self-hosted stack runs third-party Docker Compose services.

Mitigation: Review the upstream Docker Compose repository before running it.

## Reference(s):

- [aigate ClawHub release](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate project homepage](https://github.com/psyb0t/aigate)
- [Setup guide](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker and curl; access to the gateway uses AIGATE_TOKEN.]

## Skill Version(s):

5.7.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
