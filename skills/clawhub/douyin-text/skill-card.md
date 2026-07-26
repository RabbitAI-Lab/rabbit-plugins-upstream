## Description: <br>
Extracts spoken text from a Douyin video link, then produces a corrected, segmented Chinese transcript with key takeaways. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiao2769433](https://clawhub.ai/user/xiao2769433) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to turn Douyin video speech into a readable Chinese Markdown transcript. It runs extraction and Whisper transcription first, then uses the agent session to proofread, segment, summarize, and write the final document. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can import browser cookies for Douyin access, which may expose sensitive session data to local extraction code. <br>
Mitigation: Prefer --no-cookies for public videos, use a cookies.txt file only when necessary, and review the local extraction script before allowing browser-cookie access. <br>
Risk: The artifact references extract.py at a hard-coded local Windows skill path, but the script itself is not included in the artifact evidence. <br>
Mitigation: Confirm extract.py exists in the installed skill directory and inspect that script before running the skill. <br>
Risk: Whisper transcription and agent proofreading can introduce recognition or correction errors in the final transcript. <br>
Mitigation: Preserve the raw transcription section, compare corrections against source context, and avoid adding information not present in the transcript. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/xiao2769433/douyin-text) <br>
- [ClawHub skill page](https://clawhub.ai/xiao2769433/skills/douyin-text) <br>
- [Publisher profile](https://clawhub.ai/user/xiao2769433) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown file with transcript sections, raw transcription, corrected prose, key takeaways, and a short final response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Douyin URL; optional Whisper model, description-only mode, cookie source, no-cookie mode, and yt-dlp update flags.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
