## Description: <br>
aigate helps agents guide setup and use of a self-hosted OpenAI-compatible AI gateway that aggregates model providers, local inference, MCP tools, browser automation, media services, storage, search, messaging, and a web UI behind one endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they want an agent to explain, configure, run, or call a Docker Compose based self-hosted AI gateway with OpenAI-compatible routing and optional tool services. It is suited to trusted local or private deployments where the operator wants one endpoint instead of wiring each provider and service independently. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The gateway can expose broad capabilities through one bearer token, including code execution, browser automation, messaging, storage, and provider credentials when enabled. <br>
Mitigation: Use aigate only as a trusted private gateway, keep AIGATE_TOKEN strong and secret, and provide it only to agents that are fully trusted for the requested task. <br>
Risk: A single master token may grant more access than a task needs if per-service tokens are not separated. <br>
Mitigation: Split high-risk services into separate per-service tokens before giving an agent access, and enable only the services required for the workflow. <br>
Risk: Exposing the gateway directly can widen the impact of credential misuse. <br>
Mitigation: Keep the service private, avoid publishing port 4000 directly, and use a protected tunnel or authenticating reverse proxy for remote access. <br>


## Reference(s): <br>
- [ClawHub aigate page](https://clawhub.ai/psyb0t/skills/aigate) <br>
- [aigate setup](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/aigate) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline bash and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Docker Compose commands, curl examples, environment variable names, endpoint paths, and operational cautions.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
