## Description: <br>
Check Claude Code OAuth usage limits for session and weekly quotas, with optional automated refresh reminders and reset monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[azaidi94](https://clawhub.ai/user/azaidi94) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers who use Claude Code can ask an agent to check remaining session and weekly quota, return a formatted usage summary or JSON, and optionally set up reminders for quota resets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local Claude Code OAuth credentials to query usage data. <br>
Mitigation: Install only if you are comfortable with that credential access, and review the shell scripts before running them. <br>
Risk: An included notification script can send usage-reset messages to a fixed Telegram target. <br>
Mitigation: Inspect or avoid scripts/monitor-and-notify.sh unless the destination is removed or replaced with your own target. <br>
Risk: Optional monitoring creates recurring or self-scheduling checks. <br>
Mitigation: Review any Clawdbot or cron jobs after setup and disable recurring checks when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/azaidi94/skills/claude-code-usage) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [CRON_SETUP.md](artifact/CRON_SETUP.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces cached or fresh Claude Code usage summaries, reset timing, and optional cron or Clawdbot monitoring setup guidance.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
