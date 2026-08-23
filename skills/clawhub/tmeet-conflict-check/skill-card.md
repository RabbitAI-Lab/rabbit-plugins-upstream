## Description:

Check the current account's Tencent Meeting list for hard overlaps, short transition gaps, and three-or-more concurrent meetings, or configure a deterministic weekday office-hours watcher that wakes the Agent only for new conflicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[metaphor279](https://clawhub.ai/user/metaphor279)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to check visible Tencent Meeting schedules for time conflicts and to configure weekday office-hours monitoring for newly detected conflicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the user's visible Tencent Meeting list through the tmeet CLI.

Mitigation: Use it only for accounts where this meeting-data access is acceptable, and keep outputs limited to meeting topic, meeting number, and time.

Risk: The watcher stores local conflict state that can include meeting subjects, meeting numbers, times, and status.

Mitigation: Store watcher state in a private local directory and avoid committing state or event files.

Risk: The monitoring path is scheduled polling, not a Tencent Meeting server-side real-time event feed.

Mitigation: Set expectations that new conflicts can be delayed by the configured check schedule and that monitoring stops if the scheduler, OAuth session, CLI, or network fails.

Risk: Windows setup depends on external npm and Python packages.

Mitigation: Install dependencies from trusted package sources and run the bundled Windows smoke test before relying on monitoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/metaphor279/skills/tmeet-conflict-check)
- [会议冲突监测协议](references/conflict-watcher-protocol.md)
- [Windows x64 执行与验收](references/windows-execution.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown responses with command snippets and NDJSON conflict events]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Only current-account visible Tencent Meeting details are reported; watcher events omit internal meeting IDs.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
