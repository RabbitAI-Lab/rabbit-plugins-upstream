## Description:

Guides deployment and use of a self-hosted, OpenAI-compatible AI gateway that combines model routing with optional tools and services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up a Docker-based AI gateway and connect clients to model providers and optional tools through one endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One bearer token can grant access to enabled code execution, browser sessions, messaging, storage, and model-provider accounts.

Mitigation: Use a strong unique master token, separate sensitive per-service tokens, and share credentials only with trusted agents for authorized tasks.

Risk: Exposing the gateway or enabling unnecessary services increases the impact of unauthorized access.

Mitigation: Install on a trusted host or isolated VM, enable only needed services, and do not expose port 4000 directly to the internet.

## Reference(s):

- [aigate release on ClawHub](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate setup guide](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes examples for configuring services and calling the gateway.]

## Skill Version(s):

8.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
