## Description: <br>
Complete toolkit for creating autonomous AI agents and managing Discord channels for OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuzzyb33s](https://clawhub.ai/user/fuzzyb33s) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to create OpenClaw agents, bind them to Discord channels, manage channel setup and renaming, and generate the supporting workspace files, gateway configuration, and cron setup guidance for multi-agent systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make persistent OpenClaw gateway and Discord changes, including created agents, bindings, channels, and cron jobs. <br>
Mitigation: Install it only when those changes are intended, review generated configuration before applying where possible, and document how to remove created agents, bindings, channels, and cron jobs. <br>
Risk: Workspace files can be created or overwritten during agent creation and channel-renaming workflows. <br>
Mitigation: Use a fresh, dedicated workspace path and keep version control or backups available before running workflows that modify files. <br>
Risk: Example agent workflows may involve health or other sensitive personal data. <br>
Mitigation: Avoid sensitive personal data unless appropriate privacy controls and operational policies are already in place. <br>


## Reference(s): <br>
- [OpenClaw Documentation](https://docs.openclaw.ai) <br>
- [OpenClaw Agents Documentation](https://docs.openclaw.ai/agents) <br>
- [OpenClaw Discord Channels Documentation](https://docs.openclaw.ai/channels/discord) <br>
- [Agent Council on ClawHub](https://clawhub.ai/fuzzyb33s/agent-council) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration patches, generated workspace files, and script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update OpenClaw agent workspaces, gateway configuration, Discord channel state, workspace markdown files, and optional cron jobs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
