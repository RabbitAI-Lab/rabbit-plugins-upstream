## Description: <br>
Transform YouTube videos into podcast-style voice summaries using ElevenLabs TTS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[franciscoandsam](https://clawhub.ai/user/franciscoandsam) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to turn YouTube links into short podcast-style audio summaries, with an optional text-only summary path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends video content or transcripts to external services for transcription, summarization, and speech generation. <br>
Mitigation: Avoid private, confidential, or regulated videos unless processing by Supadata, OpenRouter/Cerebras, and ElevenLabs is acceptable. <br>
Risk: The required backend and npm dependencies run outside the skill package. <br>
Mitigation: Review the referenced backend repository and dependencies before deployment. <br>
Risk: API keys for ElevenLabs, Supadata, and OpenRouter are required and may incur usage costs. <br>
Mitigation: Protect required API keys and set spending limits where the services support them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/franciscoandsam/skills/youtube-voice-summarizer-elevenlabs) <br>
- [Backend repository referenced by artifact](https://github.com/Franciscomoney/elevenlabs-moltbot) <br>
- [ElevenLabs](https://elevenlabs.io) <br>
- [Supadata](https://supadata.ai) <br>
- [OpenRouter](https://openrouter.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with curl commands and returned audio or text summary data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return an MP3 audio URL, teaser text, full summary, and key takeaways when the backend job completes.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, skill.json, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
