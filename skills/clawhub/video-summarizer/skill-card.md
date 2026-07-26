## Description: <br>
将 B 站、YouTube、小红书和抖音视频转换为结构化总结，并可归档到 Obsidian 或 Notion。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajayhao](https://clawhub.ai/user/ajayhao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to turn supported online videos into structured notes, transcripts, screenshots, and summaries for local Obsidian archives or optional Notion publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video transcripts, metadata, audio when Groq is configured, screenshots, and cover images may be sent to user-configured cloud AI, storage, and publishing services. <br>
Mitigation: Avoid sensitive or confidential videos, review configured service endpoints, and use a private dedicated OSS bucket. <br>
Risk: Required API keys and optional Bilibili cookies can grant access to external services or authenticated subtitle retrieval. <br>
Mitigation: Use dedicated least-privilege keys, restrict OSS and Notion permissions to the intended resources, and remove the Bilibili cookie file when authenticated access is no longer needed. <br>
Risk: Generated summaries and screenshots may be written to local Obsidian storage or optional Notion databases. <br>
Mitigation: Confirm the target vault, database, and sharing settings before running the skill on private material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ajayhao/skills/video-summarizer) <br>
- [Security and privacy notes](artifact/references/security.md) <br>
- [Platform support details](artifact/references/platforms.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries, JSON analysis artifacts, local files, and optional Notion or Obsidian records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create transcripts, screenshots, cover images, OSS image URLs, logs, and platform metadata files.] <br>

## Skill Version(s): <br>
1.1.3 (source: evidence release and artifact changelog, released 2026-06-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
