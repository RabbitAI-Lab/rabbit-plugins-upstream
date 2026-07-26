## Description: <br>
Search YouTube videos, get channel info, fetch video details and transcripts using YouTube Data API v3 via MCP server or yt-dlp fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[grpaiva](https://clawhub.ai/user/grpaiva) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, researchers, and content-focused users use this skill to search YouTube, inspect video or channel metadata, and retrieve transcripts for analysis or summarization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on third-party packages and tools for YouTube access. <br>
Mitigation: Install only reviewed or pinned versions of zubeid-youtube-mcp-server and yt-dlp from trusted sources. <br>
Risk: A YouTube API key may be exposed through shell history, shared config, or source control. <br>
Mitigation: Store the key outside repositories, restrict it to YouTube Data API v3, and rotate it if exposure is suspected. <br>
Risk: Returned transcripts can be unavailable, incomplete, or auto-generated. <br>
Mitigation: Check transcript availability and verify quoted or decision-relevant content against the source video. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/grpaiva/skills/youtube) <br>
- [Publisher profile](https://clawhub.ai/user/grpaiva) <br>
- [youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) <br>
- [Google Cloud Console](https://console.cloud.google.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and text results from YouTube lookups or transcript retrieval.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a YouTube Data API key and may use the zubeid-youtube-mcp-server package or yt-dlp fallback.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
