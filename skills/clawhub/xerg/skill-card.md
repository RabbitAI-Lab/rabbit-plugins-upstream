## Description: <br>
Audit and reduce AI agent spend in dollars across OpenClaw, Hermes, Claude Code, Cursor, and event-ingest workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xerg](https://clawhub.ai/user/xerg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering teams, and AI operations teams use this skill to run Xerg CLI audits, summarize AI spend and waste in dollars, and compare workflow or model changes. It is useful when investigating retry loops, context bloat, downgrade candidates, per-agent spend, or optional hosted sync setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI can inspect local AI usage records and logs for cost analysis. <br>
Mitigation: Run it only on data sources you intend to audit, and review the local sources reported by `xerg doctor` before running an audit. <br>
Risk: Cloud push, connect, hosted MCP, remote SSH, and Railway flows can move beyond a local-only audit. <br>
Mitigation: Keep audits local unless the user explicitly chooses hosted or remote setup, and review the generated SSH, Railway, or MCP configuration before use. <br>
Risk: The `npx @xerg/cli@latest` path fetches and executes a third-party npm package. <br>
Mitigation: Use the published package only when third-party CLI execution is acceptable, or install and pin the CLI through the environment's normal package controls. <br>


## Reference(s): <br>
- [Xerg documentation](https://xerg.ai/docs) <br>
- [Xerg skill](https://xerg.ai/skill.md) <br>
- [Xerg service status](https://status.xerg.ai) <br>
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli) <br>
- [OpenSSH](https://www.openssh.com/) <br>
- [rsync](https://rsync.samba.org/) <br>
- [Railway CLI](https://github.com/railwayapp/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local CLI commands, runtime-specific flags, hosted setup steps, and concise summaries of audit JSON fields.] <br>

## Skill Version(s): <br>
0.13.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
