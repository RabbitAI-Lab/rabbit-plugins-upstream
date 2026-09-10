## Description:

高效会议流程管理助手 helps agents coordinate meeting scheduling, preparation, facilitation, minutes, TODO tracking, and knowledge capture while preserving manual fallback paths when external adapters are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users use this skill to turn meeting requests into an end-to-end workflow covering availability checks, room booking, calendar details, pre-read material, live facilitation prompts, meeting minutes, and follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to use configured calendar, document, meeting-platform, and messaging tools across an end-to-end meeting workflow.

Mitigation: Enable only the adapters needed for the deployment and restrict API scopes before use.

Risk: Meeting records, transcripts, documents, and TODO data can include sensitive business or personal information.

Mitigation: Avoid broad meeting-recording access and require users to provide or approve source notes before generating minutes and follow-up actions.

Risk: Notifications and TODO reminders can create persistent or recurring behavior with limited consent controls.

Mitigation: Review recipients before sending messages and treat TODO reminders or daily scans as opt-in behavior.

## Reference(s):

- [Skill page](https://clawhub.ai/muippt/skills/mu-meeting-flow)
- [Landing page](https://muippt.github.io/mu-meeting-flow/)
- [Adapter integration rules](references/integration-rules.md)
- [Meeting methodology](references/methodology.md)
- [TODO pool design](references/todo-pool.md)
- [FAQ](references/faq.md)
- [Adapter configuration example](config/adapters.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance, structured meeting artifacts, copyable notification text, and adapter configuration JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include calendar-ready meeting details, agendas, facilitation prompts, minutes, TODO items, risk notes, and manual fallback instructions.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
