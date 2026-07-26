## Description: <br>
Transcribe audio files via OpenRouter using audio-capable models (Gemini, GPT-4o-audio, etc). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[obviyus](https://clawhub.ai/user/obviyus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to transcribe user-selected audio files into text through OpenRouter audio-capable chat completion models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Chosen audio files, prompts, and request metadata are sent to OpenRouter and the selected model provider for transcription. <br>
Mitigation: Use an API key intended for this workflow, monitor usage and billing, and avoid sensitive recordings unless third-party processing is approved by policy. <br>


## Reference(s): <br>
- [OpenRouter Documentation](https://openrouter.ai/docs) <br>
- [ClawHub Skill Page](https://clawhub.ai/obviyus/skills/openrouter-transcribe) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text transcript emitted to stdout or written to a file, with markdown usage guidance in the skill instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENROUTER_API_KEY and local curl, ffmpeg, base64, and jq binaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
