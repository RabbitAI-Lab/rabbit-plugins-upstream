## Description: <br>
High-quality voice synthesis with 9 personas, 11 languages, and streaming using the Voice.ai API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gizmogremlin](https://clawhub.ai/user/gizmogremlin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use this skill to generate text-to-speech audio with curated Voice.ai personas, multilingual options, streaming, and configurable output files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The required Voice.ai API key may permit voice management actions, not only speech generation. <br>
Mitigation: Use the narrowest available API key and review any voice update or delete action before allowing it. <br>
Risk: Text submitted for synthesis is sent to the Voice.ai API. <br>
Mitigation: Avoid sending confidential, regulated, or sensitive text unless the deployment has approved Voice.ai for that data. <br>
Risk: Generated audio is written to a user-selected output path and could overwrite an important file. <br>
Mitigation: Choose output paths deliberately and review existing files before generating audio. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gizmogremlin/skills/voice-ai-voices) <br>
- [Voice.ai Documentation](https://voice.ai/docs) <br>
- [Voice.ai Text-to-Speech API Reference](https://voice.ai/docs/api-reference/text-to-speech/generate-speech) <br>
- [Voice.ai Voice Library](https://voice.ai/voices) <br>
- [Voice.ai Dashboard](https://voice.ai/dashboard) <br>
- [OpenAPI Specification](voice-ai-tts.yaml) <br>
- [Security Notes](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration] <br>
**Output Format:** [Generated audio files with CLI status text and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+ and VOICE_AI_API_KEY; the CLI writes audio to the selected output path, defaulting to output.mp3.] <br>

## Skill Version(s): <br>
1.1.5 (source: frontmatter, package.json, changelog, released 2026-02-16) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
