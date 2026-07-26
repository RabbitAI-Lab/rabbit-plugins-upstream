## Description: <br>
Generate private meeting briefings from Fulcra calendar data with optional CRM notes and web research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arc-claw-bot](https://clawhub.ai/user/arc-claw-bot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and professionals use this skill to prepare for upcoming, same-day, or next-day meetings by turning Fulcra calendar events, optional CRM notes, and allowed public research into concise private briefings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar details, attendee information, locations, CRM notes, or generated briefing content may be private. <br>
Mitigation: Use only safe metadata in shared chats unless the user explicitly approves real calendar, attendee, location, or CRM details. <br>
Risk: The skill may access Fulcra calendar data and configured CRM notes while preparing briefings. <br>
Mitigation: Install and use it only when that access is intended, keep auth tokens out of chat, and rely on configured local CRM paths only when the user provides them. <br>
Risk: Thin context or premature public research can produce unsupported meeting intelligence. <br>
Mitigation: Confirm a real qualifying meeting before research, ground the briefing in available evidence, and fail closed rather than producing filler. <br>


## Reference(s): <br>
- [Fulcra Dynamics](https://fulcradynamics.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown briefing text with optional shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Briefings should be concise, private, evidence-grounded, and saved only when the user asks or an explicit local destination is configured.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
