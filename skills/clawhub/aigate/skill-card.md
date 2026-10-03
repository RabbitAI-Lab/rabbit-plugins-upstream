## Description:

Guides developers in deploying and using a self-hosted, OpenAI-compatible AI gateway that connects model providers and optional tools behind one endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up a Docker Compose gateway and connect agents to model inference, automation, and other optional services through one endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single bearer token may grant broad access to code execution, browser sessions, messaging, storage, and configured provider accounts.

Mitigation: Give access only to trusted agents for explicitly requested tasks; set distinct per-service tokens and enable only needed services.

Risk: Exposing the gateway publicly can give token holders control over high-privilege services.

Mitigation: Install on a trusted host and keep port 4000 behind localhost, Tailscale, Cloudflare Tunnel, or an authenticating gateway.

## Reference(s):

- [aigate on ClawHub](https://clawhub.ai/psyb0t/skills/aigate)
- [Setup guide](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions cover optional services and authenticated requests to a self-hosted gateway.]

## Skill Version(s):

7.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
