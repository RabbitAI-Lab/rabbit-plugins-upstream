## Description: <br>
OpenClaw operations dashboard for sessions, usage and cost, cron runs, gateway health, DGX Spark work, Local API Hub, and opt-in meeting Copilot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw operators and developers use this skill to install, run, audit, and extend a local operations dashboard for system health, sessions, cost analytics, cron runs, Spark activity, Local API Hub status, and opt-in meeting Copilot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dashboard reads sensitive local OpenClaw operational data, including workspace documents, memory logs, channel metadata, and task artifacts when enabled for authenticated users. <br>
Mitigation: Install only for trusted OpenClaw operators, keep the service bound to loopback or behind strong access control, and use a strong OPENCLAW_AUTH_TOKEN. <br>
Risk: Config inspection and meeting Copilot can expose higher-sensitivity information, including redacted configuration data, meeting transcripts, audio, and data sent to the configured realtime provider. <br>
Mitigation: Leave OPENCLAW_ENABLE_CONFIG_ENDPOINT and OPENCLAW_ENABLE_COPILOT disabled unless the operator accepts that exposure and has configured the required credentials and consent workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jonathanjing/skills/openclaw-dashboard) <br>
- [OpenClaw Dashboard Homepage](https://github.com/JonathanJing/openclaw-dashboard) <br>
- [README](README.md) <br>
- [Security Model](SECURITY.md) <br>
- [Environment Example](env.example.txt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration values, and code references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [For agent use with the bundled dashboard source; generated outputs should preserve authentication, read-only, and opt-in sensitive-feature boundaries.] <br>

## Skill Version(s): <br>
2.0.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
