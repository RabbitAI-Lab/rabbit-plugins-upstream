## Description:

Generate MP3 speech with OpenAI TTS through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate one-off MP3 speech artifacts through the RunAPI CLI or to integrate OpenAI TTS into applications through a target-language SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TTS prompts are sent through third-party RunAPI/OpenAI services and may contain sensitive text.

Mitigation: Review request.json before submission and avoid sending sensitive content unless the user accepts that external processing.

Risk: RunAPI/OpenAI requests may incur API charges.

Mitigation: Submit only once per authorized request, retry only when evidence shows no task or billing occurred, and ask for user authorization before another paid submission.

Risk: Using the third-party RunAPI CLI requires local trust in its installed binary and authentication path.

Mitigation: Confirm the user accepts the RunAPI CLI dependency, prefer RUNAPI_API_KEY or saved CLI credentials, and use browser login only on explicit request.

## Reference(s):

- [RunAPI OpenAI TTS model overview](https://runapi.ai/models/openai-tts.md)
- [RunAPI OpenAI provider overview](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI OpenAI TTS homepage](https://runapi.ai/models/openai-tts)
- [RunAPI OpenAI TTS SDK](https://github.com/runapi-ai/openai-tts-sdk)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-openai-tts)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce and verify MP3 audio deliverables, preserve response evidence, and report terminal service failures without repeat paid submissions.]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
