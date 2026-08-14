## Description:

Generate multi-speaker speech with Gemini TTS through RunAPI. Use when the user asks an agent to synthesize dialogue or integrate Gemini TTS. Use the RunAPI CLI for one-off generation and the language SDK for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate one-off Gemini TTS speech outputs through the RunAPI CLI or integrate Gemini TTS into applications with the RunAPI SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text and referenced media for speech generation may be sent to RunAPI and its provider path.

Mitigation: Use the skill only with content approved for that service path, and review request.json before submission.

Risk: RunAPI task submission can be billable and can create task, response, and downloaded output artifacts.

Mitigation: Authenticate explicitly, submit only once unless authorized, preserve task.json and result.json, and review generated artifacts before sharing.

Risk: The skill may need API credentials for authenticated RunAPI access.

Mitigation: Prefer RUNAPI_API_KEY or explicit token import, and use interactive browser login only when the user requests it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-gemini-tts)
- [RunAPI Gemini TTS Homepage](https://runapi.ai/models/gemini-tts)
- [Gemini TTS Model Overview, Pricing, and Rate Limits](https://runapi.ai/models/gemini-tts.md)
- [Google Provider Overview](https://runapi.ai/providers/google.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [SDK Integration](https://github.com/runapi-ai/gemini-tts-sdk)
- [Gemini 2.5 Pro TTS Variant](https://runapi.ai/models/gemini-tts/gemini-2.5-pro-tts.md)
- [Gemini 3.1 Flash TTS Variant](https://runapi.ai/models/gemini-tts/gemini-3.1-flash-tts.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown instructions with shell commands, JSON request and response files, SDK guidance, and downloaded audio deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create request.json, task.json, result.json, and downloaded audio files after contract and MIME-type verification.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
