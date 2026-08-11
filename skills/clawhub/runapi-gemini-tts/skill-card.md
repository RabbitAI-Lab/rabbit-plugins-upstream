## Description:

Generate multi-speaker speech with Gemini TTS through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide agents that synthesize Gemini TTS dialogue through RunAPI or integrate Gemini TTS into applications using language SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated text, generated audio, and request files may be sent to RunAPI or an upstream provider.

Mitigation: Confirm trust in RunAPI before installation and avoid sending sensitive content unless approved for that service.

Risk: RUNAPI_API_KEY may be exposed if stored directly in prompts, scripts, or shared files.

Mitigation: Store credentials in environment variables or saved CLI configuration and avoid committing secrets.

Risk: Pricing, rate limits, and model availability can affect production use.

Mitigation: Review RunAPI pricing and rate limits for the selected Gemini TTS model before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-gemini-tts)
- [RunAPI Gemini TTS Model Overview](https://runapi.ai/models/gemini-tts)
- [RunAPI Gemini TTS Documentation](https://runapi.ai/models/gemini-tts.md)
- [RunAPI Google Provider Comparison](https://runapi.ai/providers/google.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and code guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference RunAPI CLI authentication, request files, SDK packages, and Gemini TTS model variants.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
