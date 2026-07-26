## Description: <br>
专业对话稿生成助手。把视频/音频转成带说话人标注的专业对话稿，支持 B 站音频下载、腾讯云 ASR 说话人分离、Clean Verbatim 可读性重排、金句高亮和公众号内联样式排版。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shengbinxu](https://clawhub.ai/user/shengbinxu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, editors, and content teams use this skill to turn Bilibili videos or audio files into readable, speaker-labeled Chinese dialogue transcripts for interviews, podcasts, meetings, and WeChat public-account publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio sent to Tencent Cloud ASR and COS may contain sensitive or private speech. <br>
Mitigation: Use the skill only with recordings appropriate for cloud processing, avoid private or sensitive recordings, and confirm consent and data-handling requirements before upload. <br>
Risk: Tencent Cloud SecretId, SecretKey, bucket, and region values are required and could be exposed if pasted into chat or committed in config files. <br>
Mitigation: Prefer environment variables, keep any private config file out of public repositories, and rotate any key that appears in chat, logs, or files. <br>
Risk: Downloaded audio and generated transcript files can overwrite or expose local output paths. <br>
Mitigation: Choose explicit project output directories and review generated paths before running download, ASR, rescue, or build commands. <br>
Risk: ASR diarization and LLM speaker mapping can misattribute speech or produce inaccurate readable edits. <br>
Mitigation: Review the raw ASR detail, validate speaker mapping against the source audio, preserve intermediate transcript versions, and manually verify final Clean Verbatim and highlight outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shengbinxu/skills/bilibili-subtitle) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/shengbinxu) <br>
- [Bilibili video information API used by the skill](https://api.bilibili.com/x/web-interface/view?bvid={bvid}) <br>
- [Bilibili playback URL API used by the skill](https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&fnval=16&fnver=0&fourk=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands plus generated text, JSON, TXT, HTML, and audio files from helper scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Bilibili audio downloads, Tencent Cloud ASR result JSON/TXT files, speaker-labeled dialogue TXT/HTML, optional Clean Verbatim revisions, and highlighted HTML suitable for WeChat public-account editing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
