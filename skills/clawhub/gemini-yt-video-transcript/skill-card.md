## Description: <br>
Create a verbatim transcript for a YouTube URL using Google Gemini (speaker labels, paragraph breaks; no time codes). Use when the user asks to transcribe a YouTube video or wants a clean transcript (no timestamps). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to generate clean YouTube video transcripts with speaker labels and paragraph breaks from a provided YouTube URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The selected YouTube URL, video content, and possibly the video title are sent to Google/YouTube services for transcription. <br>
Mitigation: Use only videos where that external processing is acceptable, and avoid private or sensitive videos unless the data handling is approved. <br>
Risk: The generated transcript is saved locally and may contain sensitive content from the video. <br>
Mitigation: Choose an appropriate output location, protect generated transcript files, and delete them when they are no longer needed. <br>
Risk: The skill requires a Gemini API key. <br>
Mitigation: Provide GEMINI_API_KEY through a secret-aware environment and avoid exposing it in logs, shared shells, or committed files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/odrobnik/skills/gemini-yt-video-transcript) <br>
- [Google AI Studio API keys](https://aistudio.google.com/apikey) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Plain text transcript file and chat document or attachment] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and GEMINI_API_KEY; accepts a YouTube URL and optional --out path.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
