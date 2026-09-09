## Description:

aigate provides a self-hosted Docker Compose AI gateway with an OpenAI-compatible endpoint for model routing, MCP tool use, browser automation, media generation, code execution, search, messaging, storage, forecasting, and a web UI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to deploy and interact with a self-hosted AI gateway that aggregates model providers, local inference, tools, and web UI access behind one endpoint. It is useful when a user wants Docker-based setup guidance, endpoint calls, routing configuration, and risk-aware operating practices for aigate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default single-token design can grant broad access to enabled services, including code execution, browser automation, messaging, storage, and model provider credentials.

Mitigation: Use distinct per-service tokens, provide credentials only to trusted agents for explicit tasks, and avoid relying on inherited AIGATE_TOKEN access for sensitive services.

Risk: The Docker-based installer and upstream configuration can change if the source repository is not pinned.

Mitigation: Pin the upstream repository to a reviewed commit and inspect the Makefile, Docker Compose files, and generated configuration before running make targets.

Risk: Exposing the gateway port directly can make the high-capability endpoint reachable outside the trusted host boundary.

Mitigation: Do not expose port 4000 directly; use Cloudflare Tunnel, Tailscale, or a real authenticating reverse proxy for remote access.

Risk: Environment files and mailbox or Telethon configuration can contain plaintext secrets.

Mitigation: Keep .env, mailbox configuration, Telethon sessions, and related credentials out of repositories, logs, and shared transcripts.

## Reference(s):

- [aigate ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate GitHub repository](https://github.com/psyb0t/aigate)
- [aigate setup](references/setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown with inline shell commands, endpoint examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker Compose operations, curl requests, environment-variable guidance, and security cautions.]

## Skill Version(s):

5.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
