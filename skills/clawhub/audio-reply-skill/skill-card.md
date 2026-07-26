## Description: <br>
Generates local spoken audio replies from public URL content or conversational prompts using text-to-speech. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matrixy](https://clawhub.ai/user/matrixy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Claude Code users use this skill to convert selected responses, public web pages, or short conversational answers into local audio playback on macOS with Apple Silicon. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: URL reading can expose private, authenticated, signed, or internal resources if the guardrails are widened. <br>
Mitigation: Use only public, non-sensitive http(s) URLs; reject local, private-network, credentialed, signed, authenticated, or sensitive links. <br>
Risk: Local TTS execution runs uv and downloads or uses model dependencies on the user's machine. <br>
Mitigation: Install uv from a trusted source, verify it before use, and review generated shell commands before execution. <br>
Risk: Generated audio files are temporary, but source text or audio content may still persist in chat history. <br>
Mitigation: Avoid processing private or sensitive material and prefer redacted public links or pasted excerpts. <br>


## Reference(s): <br>
- [Audio Reply on ClawHub](https://clawhub.ai/matrixy/skills/audio-reply-skill) <br>
- [MLX Audio](https://github.com/Blaizzy/mlx-audio) <br>
- [chatterbox-turbo-fp16 model](https://huggingface.co/mlx-community/chatterbox-turbo-fp16) <br>
- [MLX](https://github.com/ml-explore/mlx) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and local audio playback] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs local TTS through uv, plays generated audio, and cleans up temporary audio files.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
