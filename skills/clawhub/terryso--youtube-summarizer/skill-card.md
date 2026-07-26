## Description: <br>
Downloads YouTube video transcripts and helps an agent generate structured summaries with key viewpoints, notable quotes, topic analysis, and localized section labels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terryso](https://clawhub.ai/user/terryso) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they provide a YouTube URL and need a transcript-backed summary or content insights. It is especially suited for producing concise Chinese summaries by default, while supporting a user-requested output language. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may contact YouTube to fetch transcripts or video metadata. <br>
Mitigation: Use approved YouTube URLs and run it only in environments where that network access is acceptable. <br>
Risk: The workflow may install or use Python tools such as youtube-transcript-api and yt-dlp. <br>
Mitigation: Review dependency installation commands first, or preinstall approved versions in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terryso/skills/youtube-summarizer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summary with transcript text or JSON from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults to Chinese unless the user requests another language; quotes remain in the original spoken language, and timestamps can be included when requested.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
