## Description:

腾讯会议 helps an agent manage Tencent Meeting workflows, including scheduling, updating, canceling and querying meetings, managing participants and invitees, accessing recordings, transcripts and AI meeting minutes, applying for recording permissions, and reporting tool feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wemeeting](https://clawhub.ai/user/wemeeting)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and agents use this skill to operate Tencent Meeting accounts through authorized meeting-management, recording, transcript, minutes, invitee, and in-meeting-control workflows. It is intended for users who have configured a Tencent Meeting token and need meeting actions or meeting-content retrieval performed with confirmation for sensitive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the user's Tencent Meeting token to read meeting data and perform meeting actions.

Mitigation: Install and configure it only for accounts where that access is intended, and keep the token in the documented environment variable rather than embedding it in prompts or shared files.

Risk: Meeting updates, cancellations, invitee replacement, recording permission requests, in-meeting calls, and kicks can affect other users or meeting access.

Mitigation: Require clear previews and explicit user confirmation before executing these sensitive operations.

Risk: Recordings, transcripts, AI minutes, contact lookups, phone numbers, and email addresses may contain sensitive business or personal information.

Mitigation: Return only task-relevant details, follow the bundled masking and confirmation rules, and restrict contact lookup to immediate invite or call workflows.

## Reference(s):

- [Tencent Meeting Skill Page](https://clawhub.ai/wemeeting/skills/tencent-meeting-skill)
- [Tencent Meeting](https://meeting.tencent.com/)
- [Tencent Meeting AI Skill Token Portal](https://meeting.tencent.com/ai-skill)
- [Tencent Meeting MCP Endpoint](https://mcp.meeting.tencent.com/mcp/wemeet-open/v1)
- [API References](references/api_references.md)
- [Error Dictionary](references/error_dictionary.md)
- [Feedback Rules](references/feedback_rules.md)
- [Privacy Policy](references/privacy_policy.md)
- [Version Management](references/version_management.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown and text guidance with shell command examples and MCP tool-call JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and TENCENT_MEETING_TOKEN; tool responses may include Tencent trace identifiers for troubleshooting.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
