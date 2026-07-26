## Description: <br>
Vta Memory provides a reward and motivation system for AI agents with drive, rewards, seeking, and anticipation state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[impkind](https://clawhub.ai/user/impkind) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to add reward, drive, seeking, and anticipation state to an AI agent and surface that state in session context and a local dashboard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can scan OpenClaw session transcripts and store reward-related excerpts or inferences. <br>
Mitigation: Review generated memory files such as reward-signals.jsonl and reward-state.json, and avoid using the skill in workspaces that contain sensitive conversations. <br>
Risk: The --with-cron option adds recurring agent work for drive decay and reward encoding. <br>
Mitigation: Enable cron only after reviewing the scheduled jobs, and disable the jobs when recurring processing is not desired. <br>
Risk: Generated motivation state can influence future agent sessions. <br>
Mitigation: Inspect VTA_STATE.md and brain-dashboard.html before relying on future sessions, and edit or remove generated state when neutral behavior is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/impkind/skills/vta-memory) <br>
- [README](artifact/README.md) <br>
- [Reward encoding prompt](artifact/prompts/encode-rewards.md) <br>
- [Hippocampus related skill](https://www.clawhub.ai/skills/hippocampus) <br>
- [Amygdala Memory related skill](https://www.clawhub.ai/skills/amygdala-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, shell command output, JSON state files, and a local HTML dashboard] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq, awk, and bc; optional cron jobs can refresh motivation state over time.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release, target metadata, and OpenClaw metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
