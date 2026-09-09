## Description:

fal.ai API integration through Maton for running AI models such as image generation, video generation, upscaling, transcription, and audio workflows with managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to submit, monitor, cancel, and retrieve fal.ai model inference jobs through Maton-managed authentication. It is suited for agent workflows that generate images or video, upscale images, transcribe or synthesize audio, and call other fal.ai queue endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit billable fal.ai model requests through a connected Maton account.

Mitigation: Confirm the model, payload, target connection, and expected effect before submitting inference or other write requests.

Risk: The API passthrough can reach endpoints beyond the examples when the connected account is authorized for them.

Mitigation: Default to read and list calls, use the intended fal.ai endpoint path explicitly, and require user approval for every POST, PUT, PATCH, or DELETE request.

Risk: Raw API-key fallback increases exposure if the CLI cannot be used.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is unavoidable, keep the key in the process environment only, never print or persist it, and send it only to api.maton.ai.

Risk: API responses may include user prompts, generated media URLs, request identifiers, or other sensitive task data.

Mitigation: Return only the fields needed for the user task and avoid logging or storing full raw responses unless the user explicitly requests it.

## Reference(s):

- [fal.ai Documentation](https://fal.ai/docs)
- [fal.ai Model Gallery](https://fal.ai/models)
- [fal.ai Queue API Reference](https://fal.ai/docs/model-endpoints/queue)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request payloads, polling guidance, connection-management steps, and concise result summaries.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
