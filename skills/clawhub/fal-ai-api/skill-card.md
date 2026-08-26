## Description:

fal.ai API integration with managed API key authentication for running image generation, video generation, audio processing, and other AI models through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate through Maton and call fal.ai queue APIs for model inference tasks such as image generation, video generation, image upscaling, transcription, and text-to-speech. The skill guides safe account connection handling, request submission, status polling, and result retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: fal.ai model runs may consume credits or incur costs.

Mitigation: Confirm the target model, request payload, and intended effect before any POST or other mutating call.

Risk: Creating or deleting Maton/fal.ai connections changes account access.

Mitigation: Require explicit user confirmation before connection creation or deletion, and specify the intended account or connection when more than one exists.

Risk: Long-lived API keys can leak through logs, shell history, environment inheritance, or files.

Mitigation: Prefer OAuth and the Maton or OS credential store; if raw HTTP is unavoidable, avoid command-line secrets and send the key only to api.maton.ai.

Risk: External API responses may contain untrusted content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands, and validate identifiers before follow-up calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/fal-ai-api)
- [Maton homepage](https://maton.ai)
- [fal.ai Documentation](https://fal.ai/docs)
- [fal.ai Queue API Reference](https://fal.ai/docs/model-endpoints/queue)
- [fal.ai Model Gallery](https://fal.ai/models)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [api-gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with shell commands, JSON examples, and Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance; generated fal.ai media URLs may be temporary and model outputs vary by endpoint.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact metadata version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
