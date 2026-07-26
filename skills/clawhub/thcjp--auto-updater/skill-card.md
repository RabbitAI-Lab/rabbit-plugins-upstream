## Description: <br>
Automatically update Clawdbot and all installed skills once daily. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to configure daily update checks for Clawdbot and installed skills, receive update summaries, and run manual update or troubleshooting commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can configure unattended daily updates that change the agent and installed skills without strong confirmation, scoping, or rollback guidance. <br>
Mitigation: Install only when unattended updates are intended; review or narrow trigger wording, require explicit confirmation before creating the cron job, and keep a documented way to disable the job and recover from a broken update. <br>


## Reference(s): <br>
- [Auto Updater on ClawHub](https://clawhub.ai/thcjp/skills/auto-updater) <br>
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating) <br>
- [SkillHub CLI](https://docs.clawd.bot/tools/clawdhub) <br>
- [Cron Jobs](https://docs.clawd.bot/cron) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires command execution capability and creates persistent scheduled automation when the user chooses to install the cron job.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
