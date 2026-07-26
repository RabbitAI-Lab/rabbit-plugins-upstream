## Description: <br>
dy-caption helps agents transcribe short-video links from Douyin, TikTok, YouTube, Xiaohongshu, and similar platforms, and can check Videosays balance or transcription history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xwchris](https://clawhub.ai/user/xwchris) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators can ask an agent to extract captions or spoken text from supported short-video links, choose a supported language, and check their Videosays account balance or transcription history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video links and the Videosays API key are sent to the Videosays service for processing. <br>
Mitigation: Use the skill only when the user is comfortable sharing those links and credentials with Videosays. <br>
Risk: The skill can process videos that may be owned by someone else. <br>
Mitigation: Process only videos the user owns, created, or has permission to process. <br>
Risk: The skill runs an external npm CLI through npx. <br>
Mitigation: Review the Videosays package source and package provenance before deployment, and run it in an environment appropriate for third-party CLI tools. <br>
Risk: The Videosays API key is stored locally in ~/.videosays. <br>
Mitigation: Protect the local user profile, restrict filesystem access, and rotate the API key if the host or account is exposed. <br>


## Reference(s): <br>
- [Videosays website](https://videosays.com/zh?utm_source=dy_caption_skill&utm_medium=agent_skill&utm_campaign=douyin_to_text_skill) <br>
- [Videosays API documentation](https://videosays.com/zh/docs?utm_source=dy_caption_skill&utm_medium=agent_skill&utm_campaign=douyin_to_text_skill&utm_content=api_docs) <br>
- [videosays npm package](https://www.npmjs.com/package/videosays) <br>
- [ClawHub skill page](https://clawhub.ai/xwchris/skills/dy-caption) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and returned transcript text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include transcript text, account balance, or transcription history returned by Videosays.] <br>

## Skill Version(s): <br>
1.1.3 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
