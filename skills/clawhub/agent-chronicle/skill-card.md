## Description:

AI-powered diary generation for agents - creates rich, reflective journal entries (400-600 words) with Quote Hall of Fame, Curiosity Backlog, Decision Archaeology, Relationship Evolution, mood analytics, weekly digests, "On This Day" resurfacing, and scheduled auto-generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use Agent Chronicle to create persistent diary entries, weekly digests, quote lists, curiosity backlogs, decision records, relationship notes, and mood or topic analyses from agent session activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local session memory and preserve sensitive quotes, moods, decisions, relationship notes, and diary summaries over time.

Mitigation: Use explicit diary commands, review generated entries before saving, and periodically delete or redact diary entries, quotes, relationship notes, exports, and duplicated daily-memory entries.

Risk: Scheduled auto-generation can capture diary content without direct per-entry prompting when automation is enabled.

Mitigation: Keep automation disabled unless unattended capture is intended, and grant only the exact commands and working directory needed for the scheduled job.

Risk: PDF and HTML exports can make private diary records easier to share or retain outside the normal memory directory.

Mitigation: Review export files before sharing and remove generated exports that contain private or sensitive content.

## Reference(s):

- [Agent Chronicle on ClawHub](https://clawhub.ai/robbyczgw-cla/skills/agent-chronicle)
- [OpenClaw Automations Documentation](https://docs.openclaw.ai/automation/cron-jobs)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown diary entries, weekly digests, analysis reports, export files, and JSON task payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diary records are saved under the configured memory/diary path; exports may be produced as PDF or HTML when optional dependencies are available.]

## Skill Version(s):

0.8.0 (source: server release, frontmatter, skill.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
