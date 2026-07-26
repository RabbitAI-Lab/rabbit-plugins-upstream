## Description: <br>
Edit and validate OpenClaw Gateway config (openclaw.json / JSON5). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[caopulan](https://clawhub.ai/user/caopulan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to safely edit, validate, and troubleshoot OpenClaw Gateway configuration, including schema-backed changes to gateway, agents, models, channels, tools, skills, plugins, and modular $include files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect or over-broad configuration edits can prevent OpenClaw Gateway startup or weaken security behavior. <br>
Mitigation: Use the running Gateway schema or documented schema sources before editing, prefer targeted config set/unset operations, and run openclaw doctor after changes. <br>
Risk: Whole-config replacement and automatic repair commands can overwrite intended local settings. <br>
Mitigation: Keep backups, review proposed changes before applying them, and require explicit user consent before running write-oriented repair commands. <br>
Risk: Long-lived tokens or API keys stored directly in openclaw.json can expose credentials. <br>
Mitigation: Prefer environment variables or credential files, and review file permissions for local configuration files. <br>


## Reference(s): <br>
- [OpenClaw Config field index](references/openclaw-config-fields.md) <br>
- [OpenClaw Config schema sources](references/schema-sources.md) <br>
- [OpenClaw source repository](https://github.com/openclaw/openclaw.git) <br>
- [ClawHub skill page](https://clawhub.ai/caopulan/skills/openclaw-config) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON5 configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose edits to local OpenClaw configuration and validation commands; users should review changes before applying them.] <br>

## Skill Version(s): <br>
0.1.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
