## Description: <br>
Piper TTS Pro helps agents generate local text-to-speech audio with voice selection, long-text splitting and merging, batch generation, SSML-style controls, and WAV or MP3 output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn text, articles, dialogue, and batch prompts into local speech outputs for voice messages, audio content, accessibility reading, and localization workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documentation mixes local-only claims with callback URLs and external message delivery, which can expose source text or generated audio outside the local environment. <br>
Mitigation: Use only non-sensitive text unless local-only operation is confirmed, avoid callback_url, and explicitly control Telegram, Discord, or other external delivery. <br>
Risk: Referenced execution scripts are not included in the artifact, so their behavior cannot be reviewed from this release package alone. <br>
Mitigation: Inspect and scan the referenced scripts before installation or use, especially in privacy-sensitive environments. <br>
Risk: Voice setup can require network access for first-time model downloads despite later offline inference. <br>
Mitigation: Pre-download and approve required voice files in a controlled environment before using the skill for production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/beware-piper-tts) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, audio file paths, and voice-message markup.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce MP3 or WAV files through referenced local scripts; generated audio can be delivered through external channels when configured.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
