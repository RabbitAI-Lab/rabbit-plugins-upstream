## Description: <br>
Run a hosted agent on a cron schedule for daily digests, uptime monitors, recurring scrapes, periodic reports, and other scheduled tasks that need idempotent billing and spend caps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[structureintelligence](https://clawhub.ai/user/structureintelligence) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create, manage, and monitor hosted recurring agent jobs without operating their own scheduler, database, or server. It is suited for scheduled digests, monitors, recurring scrapes, reports, and other stateful background work that must survive beyond one conversation turn. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can schedule hosted recurring work that uses the owner's SettleMesh account and may incur charges. <br>
Mitigation: Review browser login prompts, prefer scoped API keys when available, set per-fire and per-day spend caps, and pause or delete schedules that should no longer run. <br>
Risk: Scheduled jobs may keep running after the original conversation unless explicitly paused or deleted. <br>
Mitigation: Monitor schedule history and account balance, and use the documented pause or delete commands when recurring execution is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/structureintelligence/skills/agent-cron-service) <br>
- [Publisher profile](https://clawhub.ai/user/structureintelligence) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command blocks and JSON CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the settlemesh CLI and SETTLE_API_KEY for authenticated, metered SettleMesh operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
