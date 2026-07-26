## Description: <br>
Google Meet API integration with managed OAuth for creating meeting spaces, listing conference records, and managing meeting participants. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to access Google Meet through Maton-managed OAuth, including meeting spaces, conference records, participants, recordings, and transcripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive Google Meet meeting data through Maton-managed OAuth, including participants, recordings, and transcripts. <br>
Mitigation: Install only when Maton is trusted to broker OAuth access, keep MATON_API_KEY private, and retrieve meeting data only with a legitimate need and appropriate consent. <br>
Risk: Multiple connected Google accounts can cause requests to target the wrong account. <br>
Mitigation: Select the intended connection explicitly with the Maton-Connection header when more than one Google Meet connection is available. <br>
Risk: Create, update, delete, or conference-ending operations can change Google Meet resources. <br>
Mitigation: Confirm the target resource and intended effect with the user before executing any write operation. <br>


## Reference(s): <br>
- [ClawHub Google Meet skill page](https://clawhub.ai/byungkyu/skills/google-meet) <br>
- [Publisher profile](https://clawhub.ai/user/byungkyu) <br>
- [Google Meet API overview](https://developers.google.com/meet/api/reference/rest) <br>
- [Google Meet spaces reference](https://developers.google.com/meet/api/reference/rest/v2/spaces) <br>
- [Google Meet conference records reference](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords) <br>
- [Google Meet participants reference](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.participants) <br>
- [Google Meet recordings reference](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.recordings) <br>
- [Google Meet transcripts reference](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.transcripts) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, API calls, configuration] <br>
**Output Format:** [Markdown with inline HTTP, Python, JavaScript, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and a MATON_API_KEY environment variable.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
