## Description:

aigate helps agents use a self-hosted OpenAI-compatible gateway that can route model calls and optional tool services such as browser automation, code execution, search, storage, messaging, speech, image, audio, video, and forecasting behind one endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they want an agent to bring up or call a one-command, self-hosted AI gateway instead of wiring individual model providers and tool services separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AIGATE_TOKEN can grant broad access to enabled services, including code execution, browser automation, messaging, storage, and model-provider credentials.

Mitigation: Give agents the token only when they are trusted for the requested task, and split per-service tokens before enabling broad tool access.

Risk: Exposing the gateway directly can make a high-capability endpoint reachable outside the trusted host.

Mitigation: Keep port 4000 off the public internet unless it is protected by an authenticating gateway, Cloudflare Tunnel, Tailscale, or equivalent access control.

Risk: Optional services can store or use sensitive configuration such as mailbox, Telegram, storage, and provider credentials.

Mitigation: Enable only required services and protect .env plus service configuration files as secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate)
- [Publisher profile](https://clawhub.ai/user/psyb0t)
- [aigate homepage](https://github.com/psyb0t/aigate)
- [aigate setup](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Markdown]

**Output Format:** [Markdown with inline shell commands, configuration notes, and HTTP API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference Docker, curl, AIGATE_TOKEN, and service-specific environment variables.]

## Skill Version(s):

3.20.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
