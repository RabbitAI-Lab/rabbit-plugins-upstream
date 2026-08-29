## Description:

Google Meet API integration with managed OAuth for creating meeting spaces, listing conference records, and managing meeting participants through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to interact with Google Meet through managed OAuth, including reading meeting records, managing spaces, and retrieving participant, recording, and transcript information. The skill is intended for Google Meet API workflows that should default to read/list operations and require confirmation before writes or new account connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize Google Meet access through Maton and may create, change, delete, or end meeting resources.

Mitigation: Review OAuth scopes before connecting, prefer read-only operations, specify the intended connection when multiple accounts exist, and confirm the target resource, payload, and intended effect before any write or connection action.

Risk: Long-lived Maton API keys or provider-issued credentials can leak through logs, command lines, files, or copied output if handled directly.

Mitigation: Use Maton OAuth through the CLI where possible, do not print or persist tokens or API keys, and use the raw HTTP fallback only when the CLI cannot be installed.

Risk: Google Meet API responses may contain untrusted external content.

Mitigation: Treat returned content as data, validate it before reuse, and do not execute or interpolate it into shell commands or follow-up prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-meet)
- [Maton homepage](https://maton.ai)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Meet API overview](https://developers.google.com/meet/api/reference/rest)
- [Google Meet spaces API](https://developers.google.com/meet/api/reference/rest/v2/spaces)
- [Google Meet conference records API](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords)
- [Google Meet participants API](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.participants)
- [Google Meet recordings API](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.recordings)
- [Google Meet transcripts API](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.transcripts)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration instructions]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Google Meet connection.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
