## Description: <br>
Sets up a daily scheduled update check for SkillHub and installed skills, then reports the update summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and SkillHub users use this skill to configure unattended daily update checks for SkillHub and installed skills, with a summary of what changed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can configure a persistent scheduled job that updates SkillHub and installed skills without per-update review. <br>
Mitigation: Use it only when unattended updates are intentional; run the dry-run command first and confirm the cron entry before enabling it. <br>
Risk: Automatic updates may introduce skill changes that have not been reviewed for the local environment. <br>
Mitigation: Use a notification-only or allowlisted update process when tighter control over skill changes is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/auto-updater) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup and troubleshooting guidance for scheduled SkillHub updates.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
