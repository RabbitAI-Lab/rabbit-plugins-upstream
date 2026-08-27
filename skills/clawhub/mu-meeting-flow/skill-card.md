## Description:

高效会议流程管理助手 helps an AI agent coordinate the full meeting lifecycle, including scheduling, room booking, agenda preparation, facilitation guidance, minutes extraction, TODO tracking, and knowledge capture with manual fallback paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Employees, team leads, and operations users use this skill to turn meeting requests into a structured workflow for preparation, facilitation, minutes, follow-up actions, and reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured adapters may allow the agent to access or modify calendars, transcripts, notes, notifications, email, or meeting-platform records.

Mitigation: Configure only the adapters needed for the deployment, use "none" or manual mode for unwanted capabilities, and review external operations before relying on them.

Risk: Adapter configuration can contain credentials or environment-specific tool settings.

Mitigation: Keep credentials out of shared repositories and avoid committing config/adapters.json.

Risk: Meeting minutes and TODO extraction can be inaccurate when transcript quality is poor or when no transcript is available.

Mitigation: Base summaries on supplied transcripts or notes, mark low-confidence outputs for review, and ask the user for notes when transcript data is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-meeting-flow)
- [Landing page](https://muippt.github.io/mu-meeting-flow/)
- [Meeting methodology](references/methodology.md)
- [Adapter integration rules](references/integration-rules.md)
- [TODO pool design](references/todo-pool.md)
- [FAQ](references/faq.md)
- [Adapter configuration example](config/adapters.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance, structured meeting summaries, copyable messages, and JSON-style adapter configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce manual fallback instructions when calendar, transcription, document, messaging, room, or meeting-platform adapters are not configured.]

## Skill Version(s):

1.0.2 (source: server release metadata; SKILL.md frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
