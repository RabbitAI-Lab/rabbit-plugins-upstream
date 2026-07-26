## Description: <br>
Schedule automatic OpenClaw and skill updates with reliable cron templates, timezone-safe scheduling, and clear summary outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dasweltall](https://clawhub.ai/user/dasweltall) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to configure scheduled OpenClaw and ClawHub skill updates, choose safer modes such as dry-run or core-only updates, and receive concise update summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled jobs can repeatedly update OpenClaw and installed skills without per-update review. <br>
Mitigation: Start with dry-run or core-only mode, review the cron schedule and update scope, and keep a clear path to edit or remove the cron job before enabling unattended live updates. <br>


## Reference(s): <br>
- [Agent Implementation Guide](references/agent-guide.md) <br>
- [Update Summary Examples](references/summary-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Code, Markdown, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and update-summary examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes cron templates, dry-run and core-only modes, optional helper-script guidance, and concise success/error summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
