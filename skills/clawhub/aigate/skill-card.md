## Description:

Helps developers deploy and use a self-hosted, OpenAI-compatible gateway that combines model routing with optional AI tools and services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up a self-hosted AI gateway and access model inference, optional tools, and related services through a single endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single gateway token can grant enabled tools access to code execution, browsing, messaging, storage, and provider credentials.

Mitigation: Treat AIGATE_TOKEN as a root-level secret, use separate per-service tokens, and grant agents access only to the services and actions they need.

Risk: Public exposure of the gateway could make privileged tools accessible remotely.

Mitigation: Install on a trusted machine and do not expose port 4000 directly to the public internet; use an authenticated access layer.

Risk: Optional browser, email, Telegram, storage, and coding services can act using the operator's credentials.

Mitigation: Enable only necessary services and review their permissions and credentials before authorizing agent use.

## Reference(s):

- [aigate on ClawHub](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate setup guide](references/setup.md)
- [Project homepage (listed in skill metadata)](https://github.com/psyb0t/aigate)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for a Docker Compose deployment and authenticated gateway requests.]

## Skill Version(s):

9.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
