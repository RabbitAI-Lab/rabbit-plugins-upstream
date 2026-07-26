## Description: <br>
Videosays helps agents submit video links or share text to the Videosays service and retrieve transcript text, subtitles, task status, credit balance, and transcription history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xwchris](https://clawhub.ai/user/xwchris) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to transcribe one or more online video links or share-text inputs, retrieve subtitles, and manage task status, credit balance, history, and batch continuation through the Videosays CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video links, share text, and Videosays authentication are sent to the Videosays service. <br>
Mitigation: Use the skill only with links and account data you are comfortable sharing with Videosays, and avoid private or sensitive media unless the service and account setup are trusted. <br>
Risk: Repeated submissions can create additional transcription tasks or batches. <br>
Mitigation: Use the returned task or batch status commands, check history after ambiguous network failures, and get confirmation before creating replacement submissions. <br>
Risk: API keys could be exposed if echoed in command output or conversation. <br>
Mitigation: Pass API keys through environment variables and do not print or reveal them. <br>


## Reference(s): <br>
- [Videosays Website](https://videosays.com/?utm_source=videosays_skill&utm_medium=agent_skill&utm_campaign=videosays_agent_skill) <br>
- [Videosays API Docs](https://videosays.com/docs?utm_source=videosays_skill&utm_medium=agent_skill&utm_campaign=videosays_agent_skill&utm_content=api_docs) <br>
- [Videosays CLI](https://www.npmjs.com/package/videosays) <br>
- [ClawHub Skill Page](https://clawhub.ai/xwchris/skills/videosays) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with CLI commands and transcript or subtitle text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can preserve requested transcript formats such as timeline, SRT, and VTT; batch workflows return task or batch status before final transcript content.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
