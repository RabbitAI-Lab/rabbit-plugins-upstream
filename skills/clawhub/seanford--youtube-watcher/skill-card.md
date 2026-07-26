## Description: <br>
Fetch and read transcripts from YouTube videos. Use when you need to summarize a video, answer questions about its content, or extract information from it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and analysts use this skill to retrieve YouTube transcripts so an agent can summarize videos, answer questions about their content, or extract specific information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local CLI tooling and makes requests to YouTube. <br>
Mitigation: Install yt-dlp from a trusted package source, review the requested video URL, and run the skill in an environment appropriate for network access. <br>
Risk: Cookie-based fallback can expose browser account context to local tooling for blocked or restricted videos. <br>
Mitigation: Enable browser-cookie fallback only for accounts and videos you are comfortable exposing to yt-dlp, and avoid shared or sensitive browser profiles. <br>
Risk: Videos without captions or auto-generated subtitles may fail to produce a transcript. <br>
Mitigation: Confirm the target video has usable subtitles before relying on the skill for summarization or question answering. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/seanford/skills/youtube-watcher) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text transcript output, with agent-authored Markdown summaries or answers when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires yt-dlp and videos with captions or auto-generated subtitles.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
