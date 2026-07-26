## Description: <br>
Stop waiting for prompts. Keep working. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to turn reactive agents into proactive workers that pull from a task queue, run heartbeat routines, coordinate progress, and produce handoff notes without repeated prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled unattended agent work can continue without fresh prompts and make file updates or team-channel posts without strong user-control boundaries. <br>
Mitigation: Enable the skill only for intentional autonomy workflows, restrict the queue to approved low-risk tasks, use isolated sessions where possible, and keep scheduled jobs easy to disable. <br>
Risk: Logs, reports, handoff notes, or team-channel updates may expose credentials or confidential information if autonomy tasks are too broad. <br>
Mitigation: Keep credentials and confidential details out of task queues, memory files, reports, and progress posts; review queued tasks before enabling cron or team-channel posting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/seanford/skills/agent-autonomy-kit) <br>
- [Declared Skill Homepage](https://github.com/itskai-dev/agent-autonomy-kit) <br>
- [README Repository Link](https://github.com/reflectt/agent-autonomy-kit) <br>
- [Agent Memory Kit](https://github.com/reflectt/agent-memory-kit) <br>
- [Agent Team Kit](https://github.com/reflectt/agent-team-kit) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces task queue, heartbeat, reporting, and coordination patterns for unattended agent workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
