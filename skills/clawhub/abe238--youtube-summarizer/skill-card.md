## Description: <br>
Automatically fetch YouTube video transcripts, generate structured summaries, and send full transcripts to messaging platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abe238](https://clawhub.ai/user/abe238) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to summarize YouTube videos from shared URLs, extract available transcript text, and receive concise structured takeaways. In Telegram contexts, the skill can also attach the full transcript as a text file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and runs an external, unpinned transcript-fetching dependency. <br>
Mitigation: Review or pin mcp-server-youtube-transcript before installing, especially on shared or privileged hosts. <br>
Risk: Full transcripts may be saved under /root/clawd/transcripts and sent to Telegram as file attachments. <br>
Mitigation: Use the skill only where transcript storage and forwarding are acceptable, and delete transcript files after use when retention is not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/abe238/skills/youtube-summarizer) <br>
- [MCP YouTube Transcript dependency](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summary with optional transcript text file and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include video metadata, key insights, takeaways, local transcript file paths, and Telegram file attachments.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, package.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
