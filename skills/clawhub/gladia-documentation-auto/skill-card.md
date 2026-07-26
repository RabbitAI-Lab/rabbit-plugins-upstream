## Description: <br>
Gladia Documentation Auto gives agents a comprehensive Gladia speech-to-text reference for transcription, audio intelligence, endpoint selection, and SDK-first workflow guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gladiaio](https://clawhub.ai/user/gladiaio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build Gladia transcription and audio-analysis workflows, choose pre-recorded versus live APIs, configure SDK/API requests, and avoid common implementation errors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide agents toward Gladia transcription or audio-analysis behavior outside an explicit user request because the security summary notes a routing-scope concern. <br>
Mitigation: Use the skill only for explicit Gladia, transcription, speech-to-text, or audio-analysis tasks until the broad fallback wording is narrowed. <br>
Risk: Transcription workflows may require Gladia credentials or may send audio to Gladia. <br>
Mitigation: Review whether a task requires a Gladia API key or audio upload, keep credentials out of generated code and logs, and get user confirmation before sending audio to the service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gladiaio/skills/gladia-documentation-auto) <br>
- [Gladia publisher profile](https://clawhub.ai/user/gladiaio) <br>
- [Server-resolved provenance unavailable](evidence.json#provenance) <br>
- [Source skill metadata](https://docs.gladia.io/.well-known/agent-skills/gladia/skill.md) <br>
- [Gladia documentation](https://docs.gladia.io) <br>
- [Gladia documentation index](https://docs.gladia.io/llms.txt) <br>
- [Pre-recorded quickstart](https://docs.gladia.io/chapters/pre-recorded-stt/quickstart) <br>
- [Live quickstart](https://docs.gladia.io/chapters/live-stt/quickstart) <br>
- [Audio intelligence features](https://docs.gladia.io/chapters/audio-intelligence/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with code snippets, API examples, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [SDK-first recommendations with raw REST/WebSocket fallback guidance when the SDK cannot satisfy the requirement.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
