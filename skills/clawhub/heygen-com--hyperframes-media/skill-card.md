## Description: <br>
Produces audio and media assets for HyperFrames compositions with a shared audio engine for text-to-speech, background music, sound effects, transcription, background removal, and caption authoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and media workflow authors use this skill to generate and coordinate voiceover, music, sound effects, transcription, captions, and background removal assets for HyperFrames compositions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use local credentials and cloud media providers for speech, music, sound effects, and transcription workflows. <br>
Mitigation: Run the documented preflight, choose cloud or local generation deliberately, and upload private audio only when permitted. <br>
Risk: The workflow may download runtime packages or models and launch detached background music generation. <br>
Mitigation: Review dependency and cache requirements before use, run the BGM wait step before assembly, and monitor generated status files for failures or timeouts. <br>
Risk: Credential discovery can read shared or nearby environment configuration. <br>
Mitigation: Use the documented shared authentication flow and avoid running the skill in directories that contain untrusted parent .env files. <br>


## Reference(s): <br>
- [Hyperframes Media release page](https://clawhub.ai/heygen-com/skills/hyperframes-media) <br>
- [Background music (BGM)](references/bgm.md) <br>
- [Text To Speech](references/tts.md) <br>
- [Sound effects (SFX)](references/sfx.md) <br>
- [Transcription](references/transcribe.md) <br>
- [TTS to Captions](references/tts-to-captions.md) <br>
- [Background Removal](references/remove-background.md) <br>
- [Caption Authoring](references/captions/authoring.md) <br>
- [Transcript Guide](references/captions/transcript-handling.md) <br>
- [Dynamic Caption Techniques](references/captions/motion.md) <br>
- [Requirements and Caches](references/requirements.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation of media request files and execution of local or provider-backed media generation commands.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
