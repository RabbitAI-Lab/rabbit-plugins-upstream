## Description: <br>
Generate audiobooks, podcasts, or educational audio content on demand using AI-written scripts and ElevenLabs text-to-speech. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[udiedrichsen](https://clawhub.ai/user/udiedrichsen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to create audiobook, podcast, or educational audio content from a topic or idea, review the generated script, and produce an MP3 after approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or user-approved script text is sent to Anthropic and ElevenLabs, and the resulting MP3 is stored temporarily on disk. <br>
Mitigation: Avoid sensitive, proprietary, or regulated content unless Anthropic and ElevenLabs data-handling terms are acceptable for the intended use. <br>
Risk: The artifact supports fresh content generation and text-to-speech calls that may consume paid API credits. <br>
Mitigation: Review and approve the script before audio generation, and confirm the configured service accounts have appropriate budget controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/udiedrichsen/skills/audio-gen) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files] <br>
**Output Format:** [Markdown response with generated script text, optional shell command invocation, and MEDIA token for an MP3 file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ANTHROPIC_API_KEY and ELEVENLABS_API_KEY; depends on the sag skill for text-to-speech generation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
