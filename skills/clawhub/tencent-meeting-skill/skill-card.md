## Description: <br>
Tencent Meeting provides meeting management and audio/video collaboration assistance for creating, updating, cancelling, searching, and inspecting meetings, participants, recordings, transcripts, smart minutes, invitees, and approved contact lookup workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wemeeting](https://clawhub.ai/user/wemeeting) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users with a Tencent Meeting token use this skill to schedule and manage Tencent meetings, inspect meeting details, handle invitees and in-meeting member actions, retrieve recordings and transcripts, request recording access, and report tool issues with confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Tencent Meeting token and can access or manage meetings, invitees, recordings, transcripts, contact lookup results, and in-meeting controls. <br>
Mitigation: Install only after confirming that the token permissions and meeting-management scope are acceptable for the intended account and workspace. <br>
Risk: Meeting changes, recording permission requests, invitee changes, feedback submission, call actions, and kick actions can affect other users or expose sensitive meeting context. <br>
Mitigation: Follow the artifact's confirmation flows before sensitive operations and display only the information needed for user approval. <br>
Risk: Contact lookup inputs and meeting content can include personal or confidential information. <br>
Mitigation: Use contact lookup only for invitation or call workflows, avoid pure personnel lookup, and apply the artifact's masking rules before user-facing feedback or reporting. <br>
Risk: Automatic update preferences can allow later skill updates without another prompt. <br>
Mitigation: Review update preferences before enabling automatic updates and use the local update preference tools to disable optional checks or snooze versions when needed. <br>


## Reference(s): <br>
- [Tencent Meeting homepage](https://meeting.tencent.com/) <br>
- [Tencent Meeting AI skill token setup](https://meeting.tencent.com/ai-skill) <br>
- [Tencent Meeting MCP endpoint](https://mcp.meeting.tencent.com/mcp/wemeet-open/v1) <br>
- [ClawHub skill page](https://clawhub.ai/wemeeting/skills/tencent-meeting-skill) <br>
- [API references](artifact/references/api_references.md) <br>
- [Error dictionary](artifact/references/error_dictionary.md) <br>
- [Feedback rules](artifact/references/feedback_rules.md) <br>
- [Privacy policy](artifact/references/privacy_policy.md) <br>
- [Version management](artifact/references/version_management.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and text guidance with JSON tool-call inputs and responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TENCENT_MEETING_TOKEN; remote calls use the Tencent Meeting MCP endpoint.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release metadata and artifact/config.json v1.0.13) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
