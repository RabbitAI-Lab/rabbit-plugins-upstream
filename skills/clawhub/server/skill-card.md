## Description: <br>
Helps agents diagnose, configure, deploy, tune, and maintain web and application services on a host, including process supervision, reverse proxies, ports, workers, releases, static assets, TLS reloads, logs, capacity, and self-hosted apps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and infrastructure maintainers use this skill to keep web and application services running on hosts, debug request-path failures, size workers, manage releases and rollbacks, and maintain service records without storing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server-operations guidance can affect live infrastructure when it includes restarts, stops, pruning, firewall changes, or volume deletion. <br>
Mitigation: Keep confirmation required for service-affecting actions and prefer validation plus reload paths where the skill provides them. <br>
Risk: Local service notes may contain hostnames, ports, topology decisions, incidents, and runbooks. <br>
Mitigation: Review the configured local note paths before installation and store credentials only as pointers such as environment variables, keychain entries, or secret-manager references. <br>
Risk: Incorrect server changes can cause outages, dropped requests, or failed rollbacks. <br>
Mitigation: Apply changes one request-path hop at a time, validate configuration before reload, and keep named rollback artifacts for deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/server) <br>
- [Clawic skill page](https://clawic.com/skills/server) <br>
- [Server skill definition](artifact/SKILL.md) <br>
- [Capacity](artifact/capacity.md) <br>
- [Containers](artifact/containers.md) <br>
- [Debugging](artifact/debug.md) <br>
- [Deployment](artifact/deployment.md) <br>
- [Processes](artifact/processes.md) <br>
- [Proxy](artifact/proxy.md) <br>
- [Security](artifact/security.md) <br>
- [TLS](artifact/tls.md) <br>
- [Workers](artifact/workers.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, checklists, and file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should identify the affected request-path hop, name exact files and reload commands when applicable, and require confirmation before service-affecting actions.] <br>

## Skill Version(s): <br>
1.0.2 (source: artifact/SKILL.md frontmatter and evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
