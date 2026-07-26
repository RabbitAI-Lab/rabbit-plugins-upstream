## Description: <br>
Deploy and manage Railway.app projects, including deployments, services, logs, environment variables, databases, SSH access, and CI/CD workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leicao-me](https://clawhub.ai/user/leicao-me) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to operate Railway projects from an agent, including deployment, project linking, service management, logs, environment variables, database provisioning, SSH, and CI/CD setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Railway deployment, redeploy, service deletion, environment, volume, and database commands can affect live infrastructure. <br>
Mitigation: Confirm the Railway project, service, and environment before execution, and require explicit approval before destructive or production-impacting commands. <br>
Risk: Variable, log, SSH, and database workflows can expose secrets or sensitive production data. <br>
Mitigation: Avoid pasting secrets into chat or shell history, redact logs before sharing, and use least-privilege Railway tokens and database credentials. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/leicao-me/skills/railway-skill) <br>
- [Railway Documentation](https://docs.railway.com) <br>
- [Railway CLI Reference](https://docs.railway.com/reference/cli-api) <br>
- [Railway Templates](https://railway.app/templates) <br>
- [Railway CLI GitHub](https://github.com/railwayapp/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown with inline bash and YAML code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the Railway CLI and an authenticated Railway account or token; outputs may include production-sensitive commands.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
