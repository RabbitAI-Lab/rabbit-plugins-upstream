## Description: <br>
Automate YouTube video editing workflow: download or read videos, transcribe with Whisper, analyze with GPT-4o, and generate Korean SEO metadata plus thumbnail assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeong-wooseok](https://clawhub.ai/user/jeong-wooseok) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Creators and developers use this skill to turn YouTube URLs or local video files into production assets: transcripts, subtitles, Korean SEO titles, descriptions, tags, and thumbnail imagery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video audio and transcript-derived text may be sent to OpenAI for transcription and content analysis. <br>
Mitigation: Use only content approved for third-party API processing and configure limited, revocable API keys. <br>
Risk: Optional AI thumbnail generation depends on the separate nano-banana-pro skill. <br>
Mitigation: Review nano-banana-pro independently before enabling AI image generation. <br>
Risk: Local media and browser tooling runs on user-supplied video and avatar inputs. <br>
Mitigation: Use trusted media paths, keep ffmpeg and browser tooling updated, and avoid untrusted avatar file paths until the HTML escaping issue identified in security guidance is fixed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jeong-wooseok/skills/youtube-editor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance and local output files such as .srt subtitles, .txt transcripts, .md metadata, and .png thumbnails] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENAI_API_KEY; NANO_BANANA_KEY is optional for AI thumbnail generation.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
