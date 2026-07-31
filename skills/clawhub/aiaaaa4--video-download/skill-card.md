## Description: <br>
Downloads permitted public video or audio with yt-dlp and FFmpeg after confirmation, saving the selected media, original thumbnail, hidden audio, and at most one source subtitle for downstream translation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aiaaaa4](https://clawhub.ai/user/aiaaaa4) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect media formats, choose quality and file naming, and download permitted public media with reusable inputs for subtitle translation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-supplied media URLs and remote metadata may contain untrusted text or unsafe filenames. <br>
Mitigation: Inspect fixed technical fields only, keep downloads scoped to explicit http or https URLs, use --no-playlist by default, and sanitize titles before proposing local filenames. <br>
Risk: The workflow can download copyrighted or otherwise restricted media. <br>
Mitigation: Ask for confirmation before downloading and remind users to save or use only content they have permission to download. <br>
Risk: Combined translation mode can send audio, temporary links, or subtitle text to OkFile, Alibaba Fun-ASR, qwen-mt-plus, or the current agent model service. <br>
Mitigation: Use combined mode only after the user agrees to the disclosed external processing and configures credentials locally rather than sharing them in chat. <br>
Risk: Hidden audio and subtitle preparation may create reusable files inside the project folder. <br>
Mitigation: Store reusable inputs under PROJECT_DIR/.work/input and report their presence in the final response so users can review or remove them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aiaaaa4/skills/video-download) <br>
- [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) <br>
- [Video translation workflow documentation](https://github.com/aiaaaa4/ai-landing-skills/blob/main/docs/video-translate/%E8%A7%86%E9%A2%91%E7%BF%BB%E8%AF%91%E5%B7%A5%E4%BD%9C%E6%B5%81%E8%AF%B4%E6%98%8E%E4%B9%A6.md) <br>
- [OkFile API keys](https://www.okfile.com/en/account/api-keys) <br>
- [Alibaba Cloud Fun-ASR HTTP API](https://help.aliyun.com/zh/model-studio/fun-asr-recorded-speech-recognition-http-api) <br>
- [Alibaba Cloud Model Studio API key guide](https://help.aliyun.com/zh/model-studio/get-api-key) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with confirmation prompts and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local media, thumbnail, hidden audio, and hidden subtitle files when the agent executes the reviewed commands.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
