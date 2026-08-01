## Description: <br>
本地免费一键深度总结小红书视频笔记：yt-dlp 拉取视频、faster-whisper 本地转写、输出元数据和逐字稿，再由 LLM 做结构化深度总结。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanming0007](https://clawhub.ai/user/yuanming0007) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to process Xiaohongshu video links locally, extract metadata, transcribe the audio, and produce a structured deep summary for personal knowledge capture. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tokenized Xiaohongshu links and optional browser cookies can expose sensitive access material. <br>
Mitigation: Use fresh links only for the intended video, avoid providing cookies unless required, and treat any xsec_token or cookie file as sensitive. <br>
Risk: Downloaded videos, transcripts, and metadata may contain platform content or personal information. <br>
Mitigation: Keep processing local, review outputs before storing them, and avoid redistributing downloaded or transcribed platform content without authorization. <br>
Risk: Optional archival to Obsidian or IMA may persist transcripts beyond the immediate task. <br>
Mitigation: Run in local-only mode unless archival is explicitly desired, and confirm the destination knowledge base before saving. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuanming0007/skills/xhs-deep-summary-local) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/yuanming0007) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summary with generated local transcript and JSON metadata files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces xhs_meta.json and xhs_temp.txt locally; temporary media files may be removed after processing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
