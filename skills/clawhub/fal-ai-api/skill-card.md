## Description:

fal.ai API integration with managed API key authentication for running AI models for image generation, video generation, audio processing, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to call fal.ai model endpoints through Maton for image, video, and audio generation workflows, including request submission, polling, cancellation, and result retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a connected fal.ai account for generation, cancellation, deletion, webhook, or other operations that may change state or incur cost.

Mitigation: Prefer read and list calls first, confirm account and connection IDs, and require explicit user approval before any state-changing or cost-incurring operation.

Risk: Long-lived API keys or provider-issued tokens could be exposed if printed, logged, exported, or persisted.

Mitigation: Prefer OAuth through Maton and do not print, log, export, persist, or inspect credentials; use `maton whoami` to verify authentication state.

Risk: Multiple Maton profiles or fal.ai connections can route requests to an unintended account.

Mitigation: Specify the intended profile or connection when ambiguity exists and verify connection status before making calls.

## Reference(s):

- [fal.ai Documentation](https://fal.ai/docs)
- [fal.ai Model Gallery](https://fal.ai/models)
- [fal.ai Queue API Reference](https://fal.ai/docs/model-endpoints/queue)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, API request paths, and request payload examples; state-changing or cost-incurring operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
