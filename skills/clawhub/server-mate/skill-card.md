## Description: <br>
Build or extend a lightweight server monitoring and AI operations workflow for Linux hosts running Nginx or Apache, with optional centralized remote monitoring through the BT-Panel (Baota) HTTP API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tankeito](https://clawhub.ai/user/tankeito) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to design, configure, or extend monitoring for Linux web hosts, including local or BT-Panel remote log collection, system metrics, alerts, reports, AI diagnosis, and guarded remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide production-level server monitoring and privileged automation. <br>
Mitigation: Keep automation.dry_run true and leave auto_ban and auto_heal disabled until commands, allowlists, cooldowns, and audit destinations are approved. <br>
Risk: Dashboard and monitoring endpoints may expose sensitive operational information if reachable by untrusted users. <br>
Mitigation: Bind dashboards to localhost or place them behind authentication before exposing them beyond the host. <br>
Risk: Webhook URLs, panel API keys, Telegram credentials, GeoIP credentials, and AI analysis inputs can contain secrets or incident data. <br>
Mitigation: Avoid plaintext API keys, keep config files out of version control, and disable AI analysis when logs or incident context must not leave the environment. <br>
Risk: Bootstrap or install commands that pipe remote scripts into privileged shells can be high impact. <br>
Mitigation: Do not use curl-to-sudo-bash installation paths without independently reviewing and verifying the fetched script. <br>


## Reference(s): <br>
- [Server Mate on ClawHub](https://clawhub.ai/tankeito/skills/server-mate) <br>
- [User Guide](user-guide.md) <br>
- [Architecture](references/architecture.md) <br>
- [Data Contracts](references/data-contracts.md) <br>
- [Ops Playbook](references/ops-playbook.md) <br>
- [SQLite Schema](references/sqlite-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, shell command, YAML configuration, JSON payload, and operational report content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce host-local config, SQLite, log, and report file guidance for the operator's workspace] <br>

## Skill Version(s): <br>
1.6.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
