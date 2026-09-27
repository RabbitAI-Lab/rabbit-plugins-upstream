## Description:

Guides developers in deploying a self-hosted AI gateway that routes model requests and optional tools through an OpenAI-compatible endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up and operate a self-hosted, OpenAI-compatible gateway with model fallback and optional AI services, rather than configuring each integration separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One bearer token can grant code execution, browser automation, messaging, and storage access when those services are enabled.

Mitigation: Use a strong AIGATE_TOKEN, override per-service tokens, and grant agents only the access needed for an explicit task.

Risk: Exposing the gateway can give unintended parties access to sensitive services.

Mitigation: Install on a trusted host and keep the endpoint localhost-only unless protected by a real access-control layer.

## Reference(s):

- [aigate on ClawHub](https://clawhub.ai/psyb0t/skills/aigate)
- [Setup instructions](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions for an optional, self-hosted stack; enabled services require appropriate credentials and operator configuration.]

## Skill Version(s):

6.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
