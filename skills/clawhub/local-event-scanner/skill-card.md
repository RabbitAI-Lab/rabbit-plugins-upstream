## Description: <br>
Finds, scores, and shortlists real-world events in a requested city, area, or region for an upcoming date range, with optional calendar-aware review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobiaswestholm](https://clawhub.ai/user/tobiaswestholm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People use this skill to discover public local events, compare them against stated interests and dealbreakers, and receive a ranked shortlist with source links, caveats, and next actions. When enabled by the user, it can also use calendar availability to adjust practicality or add a specific selected event. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional calendar access could expose availability context or create calendar events if enabled without care. <br>
Mitigation: Enable calendar access only by user choice, use busy/free availability for the requested window, and create a calendar event only after the user explicitly asks to add a specific suggestion. <br>
Risk: Local run notes and preference files may contain event interests, source choices, and availability summaries on shared or synced machines. <br>
Mitigation: Store only the minimum event metadata and preference information needed, avoid raw private calendar details, and periodically inspect or delete local runs and preference files when appropriate. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tobiaswestholm/skills/local-event-scanner) <br>
- [Operating Model](references/operating-model.md) <br>
- [Privacy And Access](references/privacy-and-access.md) <br>
- [Scoring Rubric](references/scoring-rubric.md) <br>
- [Availability Rules](references/availability-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown shortlist and run-note content with source links, recommendation labels, caveats, and optional setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include calendar availability summaries or a calendar event creation action only when the user enables calendar access and explicitly requests it.] <br>

## Skill Version(s): <br>
1.1.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
