## Description:

腾讯会议 helps agents schedule, manage, inspect, and control Tencent Meeting sessions, including invitees, waiting rooms, recordings, transcripts, smart minutes, and recording-permission requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wemeeting](https://clawhub.ai/user/wemeeting)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external Tencent Meeting users can use this skill to have an agent create, update, cancel, search, and inspect meetings; manage invitees and in-meeting controls; and retrieve recordings, transcripts, smart minutes, participant exports, and recording permission flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, modify, cancel, inspect, and control meetings using the configured Tencent Meeting account token.

Mitigation: Install only when the publisher and integration are trusted, and require user confirmation before destructive meeting changes or in-meeting control actions.

Risk: The skill can access recordings, transcripts, smart minutes, participant information, and contact lookup results where the token permits.

Mitigation: Limit use to intended meeting workflows, follow the bundled privacy rules for sensitive information, and avoid using contact lookup for general people search.

Risk: The TENCENT_MEETING_TOKEN grants sensitive account access.

Mitigation: Treat TENCENT_MEETING_TOKEN as a secret and keep the configured MCP endpoint set to the Tencent HTTPS URL.

## Reference(s):

- [Tencent Meeting](https://meeting.tencent.com/)
- [Tencent Meeting Skill Token](https://meeting.tencent.com/ai-skill)
- [Tencent Meeting MCP Endpoint](https://mcp.meeting.tencent.com/mcp/wemeet-open/v1)
- [API References](references/api_references.md)
- [Error Dictionary](references/error_dictionary.md)
- [Feedback Rules](references/feedback_rules.md)
- [Privacy Policy](references/privacy_policy.md)
- [Version Management](references/version_management.md)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown guidance with JSON tool-call arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and TENCENT_MEETING_TOKEN; configured for the Tencent Meeting HTTPS MCP endpoint.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
