## Description:

Use Speko to transcribe audio, synthesize speech, and pick the model for each leg of a voice pipeline from measured benchmarks instead of a hardcoded vendor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speko](https://clawhub.ai/user/speko)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route speech-to-text, text-to-speech, and LLM requests through Speko with benchmark-based model selection, dry-run route previews, language-aware choices, spend ceilings, and failover.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using live transcription, synthesis, or LLM routing can send audio, text, and routing metadata to Speko.

Mitigation: Use the skill only when that data sharing is acceptable under the active SPEKO_API_KEY and applicable data-handling policies.

Risk: Voice routing can incur spend or select an unexpected provider if key policy and request headers are not reviewed.

Mitigation: Use the routing preview endpoint and Speko key policy controls, including objective and price-ceiling settings, before live transcription or synthesis.

Risk: Unsupported languages, incompatible audio containers, or mismatched host credentials can cause failed or misleading voice workflow results.

Mitigation: Check the route preview, use supported router languages, prefer WAV output for speech, let curl set multipart boundaries for transcription, and verify the key is for api.speko.ai.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/speko/skills/speko)
- [Speko API base URL](https://api.speko.ai/v1)
- [Speko routing preview endpoint](https://api.speko.ai/v1/routing/preview?stage=tts&language=en&objective=quality)
- [Speko speech synthesis endpoint](https://api.speko.ai/v1/audio/speech)
- [Speko audio transcription endpoint](https://api.speko.ai/v1/audio/transcriptions)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request examples, route-selection explanations, transcription text, speech file commands, and configuration guidance for SPEKO_API_KEY, curl, and jq.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
