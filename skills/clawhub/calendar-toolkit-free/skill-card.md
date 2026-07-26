## Description: <br>
A calendar management and scheduling skill for creating events, arranging meetings, reviewing schedules, setting recurring events, and syncing across Google, Apple, and Outlook calendars. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and individuals use this skill to manage personal calendar workflows, including event creation, meeting scheduling, schedule review, reminders, recurring events, and cross-provider calendar sync. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar accounts, API keys, and tokens may be exposed to configured calendar providers or supporting tools. <br>
Mitigation: Use only accounts and credentials appropriate for this publisher, prefer least-privilege access, and avoid entering sensitive calendars or secrets unless the provider path is trusted. <br>
Risk: The artifact claims local-only privacy while also describing calendar sync, external API access, and callback URLs. <br>
Mitigation: Treat privacy boundaries as unverified until the publisher clarifies which operations remain local and which contact external services. <br>
Risk: Calendar creation, availability checks, synchronization, and callback use can change schedules or disclose participant availability. <br>
Mitigation: Require explicit user confirmation before creating or modifying events, checking other participants' availability, enabling sync, or using callback URLs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/calendar-toolkit-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets; runtime responses may be JSON, text, or CSV.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include status, result data, execution logs, configuration values, and error details.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and target metadata; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
