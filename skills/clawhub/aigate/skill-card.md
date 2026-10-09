## Description:

Guides developers in deploying and using a self-hosted, OpenAI-compatible gateway for model routing and optional AI tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up a Docker-based AI gateway and connect clients to model providers and optional tools through one endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One bearer token may grant access to code execution, browser automation, messaging, and storage across enabled services.

Mitigation: Enable only necessary services, split per-service tokens, and grant agent access only for explicitly authorized tasks.

Risk: Direct internet exposure of the gateway could expose high-privilege capabilities.

Mitigation: Install only on a trusted host and avoid exposing port 4000 directly to the internet; use a protected access path.

Risk: Gateway, mailbox, and Telegram configuration may contain sensitive credentials.

Mitigation: Keep AIGATE_TOKEN and mailbox/Telethon configuration private and out of committed files.

## Reference(s):

- [aigate ClawHub release](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate setup guide](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment and API usage depend on enabled services and operator-provided credentials.]

## Skill Version(s):

10.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
