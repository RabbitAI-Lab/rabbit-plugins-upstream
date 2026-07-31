## Description: <br>
aigate is a self-hosted OpenAI-compatible gateway that aggregates model routing, MCP tool use, browser automation, media generation, code execution, storage, search, messaging, forecasting, and a web UI behind one bearer-protected endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use aigate to deploy and operate a self-hosted OpenAI-compatible gateway that centralizes provider fallback, optional AI tools, and service endpoints without wiring each backend separately. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A single AIGATE_TOKEN can grant access to enabled code execution, browser automation, messaging, storage, and provider credentials. <br>
Mitigation: Enable only the services needed, split per-service tokens before agent use, and provide tokens only to trusted agents for explicit user-requested actions. <br>
Risk: Directly exposing port 4000 can put the gateway and its bearer-token surface on the public internet. <br>
Mitigation: Keep the service on a controlled host and use Cloudflare Tunnel, Tailscale, or a real authenticating reverse proxy instead of publishing the port directly. <br>
Risk: .env, mailbox, and Telethon configuration files can contain plaintext credentials or reusable sessions. <br>
Mitigation: Store these files as sensitive secrets, keep them out of source control, and limit filesystem access to operators who need them. <br>
Risk: Optional code execution, browser automation, email, Telegram, and public-read storage features can act with high practical authority once enabled. <br>
Mitigation: Review the enabled feature set before installation and apply extra approval or isolation around these high-capability services. <br>


## Reference(s): <br>
- [aigate setup reference](references/setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate) <br>
- [aigate homepage](https://github.com/psyb0t/aigate) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Docker Compose commands, environment variable guidance, local endpoint URLs, and bearer-token handling notes.] <br>

## Skill Version(s): <br>
3.16.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
