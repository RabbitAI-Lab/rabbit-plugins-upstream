## Description: <br>
Transcribes short-video share links from Douyin, TikTok, YouTube, and Xiaohongshu through Videosays, and can check Videosays balance or transcription history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xwchris](https://clawhub.ai/user/xwchris) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn supported short-video share links into transcript text, including multilingual transcription requests. It also helps users run Videosays account setup, balance checks, and transcription history queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video links and the user's Videosays API key are sent to the Videosays service for transcription. <br>
Mitigation: Install and use the skill only if that data flow is acceptable, and avoid submitting sensitive or unauthorized video links. <br>
Risk: The skill executes the external Videosays npm package through npx. <br>
Mitigation: Apply normal dependency trust practices, review the package source or publisher as needed, and keep API-token hygiene in place. <br>
Risk: Transcribing content without rights or permission can create policy or legal exposure. <br>
Mitigation: Use the skill only for videos the user owns, created, or has permission to process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xwchris/skills/douyin-to-text) <br>
- [Videosays API documentation](https://videosays.com/zh/docs?utm_source=dy_caption_skill&utm_medium=agent_skill&utm_campaign=douyin_to_text_skill&utm_content=api_docs) <br>
- [Videosays website](https://videosays.com/zh?utm_source=dy_caption_skill&utm_medium=agent_skill&utm_campaign=douyin_to_text_skill) <br>
- [Videosays npm package](https://www.npmjs.com/package/videosays) <br>
- [Videosays agent tools](https://github.com/xwchris/videosays-agent-tools) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text transcription results with command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return transcript text, account balance, transcription history, or setup instructions from the Videosays CLI.] <br>

## Skill Version(s): <br>
1.1.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
