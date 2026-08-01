## Description: <br>
Self-hosted AI platform that helps an agent guide setup and use of a Docker Compose OpenAI-compatible gateway with inference routing, MCP tool use, browser automation, media generation, transcription, storage, code execution, search, messaging, forecasting, an async queue, and a web UI behind one bearer token. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when they want an agent to help deploy, configure, and call a self-hosted OpenAI-compatible AI gateway that aggregates model providers, local models, tools, media services, storage, search, messaging, and a web UI. It is most relevant when the user wants one endpoint and routing layer instead of wiring each service separately. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A single bearer token can unlock code execution, browser control, messaging, storage, and credentials when many services are enabled. <br>
Mitigation: Set separate per-service tokens before giving any token to an agent, provide tokens only for explicitly requested work, and avoid treating AIGATE_TOKEN as chat-only access. <br>
Risk: Public exposure of the gateway can create a high-blast-radius entry point. <br>
Mitigation: Keep port 4000 off the public internet and use Cloudflare Tunnel, Tailscale, or a real authenticating gateway when remote access is required. <br>
Risk: Configuration files can contain plaintext provider, mailbox, Telethon, database, and service credentials. <br>
Mitigation: Protect .env, mailbox, and Telethon configuration files as sensitive secrets and do not commit tokens or credentials to repositories. <br>
Risk: Enabling unnecessary optional services expands the actions available through the gateway. <br>
Mitigation: Enable only the services needed for the current deployment and leave unused providers, browser automation, messaging, storage, and code execution routes disabled. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate) <br>
- [aigate setup reference](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands, HTTP examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Docker Compose setup steps, environment variable guidance, curl examples, service route summaries, and safety warnings.] <br>

## Skill Version(s): <br>
3.17.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
