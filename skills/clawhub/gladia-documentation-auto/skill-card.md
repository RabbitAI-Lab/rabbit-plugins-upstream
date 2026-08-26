## Description:

Comprehensive Gladia speech-to-text reference for agents that need broad guidance on Gladia capabilities, endpoints, model selection, SDK-first workflows, and fallback REST or WebSocket usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gladiaio](https://clawhub.ai/user/gladiaio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to build Gladia speech-to-text integrations for pre-recorded transcription, live transcription, diarization, translation, audio intelligence features, CLI usage, and SDK-first implementation decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI installation examples execute remote installer scripts.

Mitigation: Review installer scripts before running them and prefer trusted package or release channels when available.

Risk: Gladia API keys could be exposed if copied into client-side code or shared transcripts.

Mitigation: Keep API keys server-side or in protected environment variables and avoid exposing the x-gladia-key header in frontend code.

Risk: Generated transcription guidance can be incorrect if model, duration, language, or webhook constraints are ignored.

Mitigation: Validate model choice, audio limits, callback reachability, and error handling against Gladia documentation before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gladiaio/skills/gladia-documentation-auto)
- [Gladia Agent Skill Source](https://docs.gladia.io/.well-known/agent-skills/gladia/skill.md)
- [Gladia Documentation](https://docs.gladia.io)
- [Gladia Documentation Index](https://docs.gladia.io/llms.txt)
- [Pre-recorded STT Quickstart](https://docs.gladia.io/chapters/pre-recorded-stt/quickstart)
- [Live STT Quickstart](https://docs.gladia.io/chapters/live-stt/quickstart)
- [Gladia API Reference](https://docs.gladia.io/api-reference)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code, API endpoint references, shell commands, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SDK-first recommendations with REST, WebSocket, and CLI fallback guidance]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
