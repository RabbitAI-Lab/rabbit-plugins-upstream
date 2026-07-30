## Description: <br>
腾讯会议 helps an agent manage Tencent Meeting workflows, including scheduling and changing meetings, finding meeting details and participants, handling invitees and in-meeting controls, retrieving recordings and transcripts, requesting recording permissions, and submitting confirmed feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wemeeting](https://clawhub.ai/user/wemeeting) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and authorized Tencent Meeting users use this skill to create, update, cancel, search, and inspect meetings, participants, invitees, recordings, transcripts, and meeting summaries through an agent. It is also useful for controlled invitee management, in-meeting call or kick actions, recording permission requests, and feedback submission when the user has provided a Tencent Meeting token. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a Tencent Meeting token to read or change meetings, recordings, transcripts, invitees, and meeting participants. <br>
Mitigation: Install only when this access is intended, use the least-privileged token available, and review confirmations before meeting changes, invitee changes, recording permission requests, calls, kicks, or feedback submissions. <br>
Risk: Meeting, recording, contact, and feedback workflows can expose personal or business-sensitive information. <br>
Mitigation: Follow the bundled privacy policy: minimize disclosure, redact phone numbers, email addresses, names, meeting subjects, URLs, and identifiers before user display or feedback submission, and require explicit user confirmation for sensitive actions. <br>
Risk: Contact lookup tools can resolve names, phone numbers, or emails to internal open_id values. <br>
Mitigation: Use contact lookup only for explicit invite or call workflows in the same turn, do not use it for general personnel lookup, and do not show open_id values to the user. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wemeeting/skills/tencent-meeting-skill) <br>
- [Tencent Meeting Homepage](https://meeting.tencent.com/) <br>
- [Tencent Meeting AI Skill Token Page](https://meeting.tencent.com/ai-skill) <br>
- [Tencent Meeting MCP Endpoint](https://mcp.meeting.tencent.com/mcp/wemeet-open/v1) <br>
- [API References](artifact/references/api_references.md) <br>
- [Error Dictionary](artifact/references/error_dictionary.md) <br>
- [Privacy Policy](artifact/references/privacy_policy.md) <br>
- [Feedback Rules](artifact/references/feedback_rules.md) <br>
- [Version Management](artifact/references/version_management.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text guidance with JSON tool-call arguments and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TENCENT_MEETING_TOKEN for tool execution.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence and artifact config.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
