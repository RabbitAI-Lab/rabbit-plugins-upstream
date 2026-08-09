## Description: <br>
Controls a Discord bot from an agent with JSON actions for messaging, reactions, stickers, polls, threads, pins, search, member and role lookup, channel and voice status, scheduled events, and gated moderation actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, community operators, and team administrators use this skill to automate Discord bot workflows such as announcements, message follow-up, community polls, thread management, and moderated member actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad local read, write, and command execution authority beyond typical Discord bot control. <br>
Mitigation: Install only in a constrained environment and remove or deny local read/write/exec authority unless a specific audited workflow requires it. <br>
Risk: Moderation and role actions can delete messages, time out users, kick or ban members, and change roles. <br>
Mitigation: Keep moderation and role actions disabled by default and require explicit confirmation before destructive or privilege-changing actions. <br>
Risk: Callback URLs can expose results or trigger notifications to untrusted endpoints. <br>
Mitigation: Allow only callback URLs that are controlled and trusted by the operator. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration instructions, Shell commands, Markdown] <br>
**Output Format:** [Markdown guidance with JSON action examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Discord bot token and action gates for role and moderation operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
