## Description: <br>
Videosays helps agents submit video links or share text to the Videosays CLI and retrieve transcript text, subtitles, credit balance, or transcription history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wegofuture](https://clawhub.ai/user/wegofuture) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external users use this skill to transcribe one or more online videos through Videosays, check task or batch status, and retrieve transcript or subtitle output without duplicate submissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted video links, share text, and authentication data are sent to the third-party Videosays service. <br>
Mitigation: Use the skill only when Videosays' privacy and retention terms fit the data being submitted, avoid private videos unless appropriate, and never print or reveal API keys. <br>
Risk: Repeating a transcribe or batch submission can create additional tasks or batches and may consume extra credits. <br>
Mitigation: Capture task or batch IDs, use status and history commands to recover ambiguous outcomes, and ask before creating a replacement submission. <br>
Risk: The skill depends on an external npm CLI package and Videosays service availability. <br>
Mitigation: Review the npm package provenance before first use and surface stable CLI errors, network failures, or media access problems to the user instead of treating them as transcript output. <br>


## Reference(s): <br>
- [Videosays Website](https://videosays.com) <br>
- [Videosays API](https://api.videosays.com) <br>
- [Videosays CLI](https://www.npmjs.com/package/videosays) <br>
- [ClawHub Skill Page](https://clawhub.ai/wegofuture/skills/videosays) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and transcript or subtitle text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Videosays task IDs, batch IDs, status messages, transcript text, SRT, VTT, timeline output, balance, history, or error guidance.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
