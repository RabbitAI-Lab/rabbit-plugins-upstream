## Description:

Create Gemini Omni voice resources, character resources, and Flash Preview or multimodal text-to-video tasks through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create or manage Gemini Omni audio voice resources, character resources, and video generation tasks through RunAPI. It helps choose the CLI path for one-off work and SDKs for application or backend integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI credentials may be needed for authenticated CLI or SDK use.

Mitigation: Confirm the agent is allowed to use RunAPI, prefer environment auth or saved CLI configuration, and avoid exposing RUNAPI_API_KEY in logs or generated files.

Risk: Generated media URLs are temporary and may expire before downstream use.

Mitigation: Download generated audio, video, images, or other files into durable storage controlled by the user within the stated 7-day window.

Risk: Provider pricing or rate limits may affect production use.

Mitigation: Check current provider pricing and rate limits before running production workloads or high-volume generation.

Risk: Using the CLI as a production integration layer can make application behavior brittle.

Mitigation: Use RunAPI SDKs for application, backend, worker, webhook, or production integrations; reserve the CLI for one-off generation, debugging, smoke tests, and manual runs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/runapi-ai/skills/runapi-gemini-omni)
- [RunAPI Gemini Omni documentation](https://runapi.ai/models/gemini-omni.md)
- [RunAPI Gemini Omni homepage](https://runapi.ai/models/gemini-omni)
- [Gemini Omni Flash Preview documentation](https://runapi.ai/models/gemini-omni/flash-preview.md)
- [RunAPI Google provider documentation](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill guidance](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may result in RunAPI CLI calls, SDK integration code, request JSON, and instructions for storing generated media.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
