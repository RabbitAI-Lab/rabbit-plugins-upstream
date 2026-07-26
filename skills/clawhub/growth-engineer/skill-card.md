## Description: <br>
Growth Engineer helps mobile app and agent-runtime teams correlate analytics, crashes, billing, feedback, store signals, and repo context into proposal drafts that can flow into agent chat, GitHub issues, or draft pull requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wotaso-dev](https://clawhub.ai/user/wotaso-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and growth engineers use this skill to collect product, crash, monetization, store, feedback, and repo signals for mobile apps and turn them into execution-ready proposals, chat handoffs, GitHub issues, or draft pull requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install or update tools on the host. <br>
Mitigation: Review before installing on a primary machine and prefer a dedicated workspace or host. <br>
Risk: The skill can persist schedulers and recurring run state. <br>
Mitigation: Verify cron, HEARTBEAT, and profile changes before enabling recurring runs. <br>
Risk: Configured command sources or deliveries may execute shell commands or create external artifacts. <br>
Mitigation: Disable self-update and command-based sources or deliveries unless needed, and keep provider and GitHub tokens read-only until artifact creation is explicitly desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wotaso-dev/skills/growth-engineer) <br>
- [Growth Engineer Homepage](https://github.com/Wotaso/growth-engineer-skill) <br>
- [Advanced Setup](references/advanced-setup.md) <br>
- [Setup And Scheduling](references/setup-and-scheduling.md) <br>
- [Required Secrets](references/required-secrets.md) <br>
- [Input Schema](references/input-schema.md) <br>
- [Generated GitHub Issue Template](references/issue-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration, local proposal or outbox files, and issue or pull request drafts when configured.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [External artifact creation is configurable; GitHub issues or draft pull requests should be created only when explicitly enabled.] <br>

## Skill Version(s): <br>
1.0.209 (source: release evidence, SKILL.md metadata, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
