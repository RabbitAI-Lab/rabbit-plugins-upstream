## Description: <br>
Expose installed agent Skills as HTTP(S) REST APIs through a persistent FastAPI service that auto-generates endpoints, supports sync and async runs, webhook callbacks, multiple agent executors, and a bilingual web console. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to turn installed agent Skills into network-callable HTTP(S) endpoints for automation, integrations, and remote execution. It is best suited for trusted local or private-network deployments unless the service is explicitly hardened for broader exposure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make local agent skills broadly callable over a network, and default broad exposure can include skills with side effects. <br>
Mitigation: Install only in trusted local or private networks, replace wildcard exposure with a small explicit allowlist, and deny skills that send messages, modify accounts, delete data, deploy code, or access secrets. <br>
Risk: HTTP, public documentation routes, or command-line API keys can expose service metadata or credentials when the service is reachable beyond localhost. <br>
Mitigation: Bind to 127.0.0.1 unless remote access is required, enable HTTPS for non-local use, disable public docs on exposed deployments, and provide API keys through configuration or environment variables instead of command-line arguments. <br>
Risk: High-capability executors may run agent skills with tool access that can affect files, services, external systems, or secrets. <br>
Mitigation: Use least-capability executors where possible, review each exposed skill before deployment, and avoid full-auto or high-capability execution for sensitive workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/songhonglei/skills/skill-to-http) <br>
- [Skill Documentation](SKILL.md) <br>
- [README](README.md) <br>
- [HTTPS Deployment Guide](references/https-deployment.md) <br>
- [Params Schema](references/params-schema.md) <br>
- [TLS Auth Standard](references/tls-auth-standard.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration, and HTTP API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce service configuration guidance and expose skill execution through HTTP(S) endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata, SKILL.md, CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
