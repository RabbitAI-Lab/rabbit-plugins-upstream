## Description: <br>
Use when crafting TTS, music, or bed prompts for any generative audio model - director style, song structure, and post-production layering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent operators use this skill to draft structured prompts for TTS narration, songs, instrumental beds, and audio/video layering decisions across generative audio workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested related skills or commands may lead to paid API calls or uploads of generated or user audio. <br>
Mitigation: Review related skill installs, credentials, upload targets, and costs before making Pruna or Replicate-backed calls. <br>
Risk: Audio-led video workflows can truncate narration when clips exceed model duration limits. <br>
Mitigation: Probe TTS length, keep per-scene audio within documented limits, and split longer narration into separate scene rows. <br>


## Reference(s): <br>
- [TTS style prompting](references/tts-style-prompting.md) <br>
- [Music and bed prompting](references/music-and-bed-prompting.md) <br>
- [Audio post-production](references/audio-post-production.md) <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/audio-prompting) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with prompt examples, checklists, and optional install or workflow commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces prompt-writing and workflow guidance; it does not execute audio generation directly.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
