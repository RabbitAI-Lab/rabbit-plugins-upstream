## Description: <br>
Generates .ogg Opus voice-message audio from text or SSML using Speechify API with Edge TTS fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rickkbarbosa](https://clawhub.ai/user/rickkbarbosa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to turn generated text or SSML into Opus .ogg voice-message files for messaging workflows, with configurable voices and provider fallback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text sent for synthesis may be processed by external TTS providers. <br>
Mitigation: Do not submit secrets, credentials, private chats, regulated data, or other sensitive content for synthesis. <br>
Risk: API keys and helper command paths are read from the environment. <br>
Mitigation: Keep SPEECHIFY_API_KEY, EDGE_TTS_CMD, and VAULT_RESOLVER controlled by the deploying user or runtime. <br>
Risk: Generated audio is written to caller-selected filesystem paths. <br>
Mitigation: Write output to a dedicated temporary or media directory and review paths before using generated files in downstream messaging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rickkbarbosa/skills/speechfy) <br>
- [Speechify API Docs](https://docs.sws.speechify.com/) <br>
- [Edge TTS](https://github.com/rany2/edge-tts) <br>
- [SSML W3C Specification](https://www.w3.org/TR/speech-synthesis11/) <br>
- [Voices Reference](references/voices.md) <br>
- [Architecture Diagram](docs/diagrama.svg) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Opus .ogg audio file path with Markdown and bash usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires text or SSML input; output path and voices are configurable through environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
