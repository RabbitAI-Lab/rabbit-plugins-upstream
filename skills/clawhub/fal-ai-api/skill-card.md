## Description:

fal.ai API integration with managed API key authentication for running image, video, audio, and other AI model workflows through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate with Maton, connect a fal.ai account, submit model inference jobs, poll status, retrieve outputs, and manage queued requests. It is intended for fal.ai tasks such as image generation, video generation, image upscaling, text-to-speech, transcription, and other model calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: fal.ai model runs may consume credits through the connected fal.ai or Maton account.

Mitigation: Confirm the target model, payload, and account connection before submitting requests, especially POST, PUT, PATCH, or DELETE calls.

Risk: Long-lived API keys can leak through process environments, shell history, logs, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting credentials, and use the raw HTTP fallback only when the CLI cannot be installed.

Risk: Generated API workflows can run against the wrong account when multiple profiles or connections exist.

Mitigation: Specify the Maton profile or fal.ai connection when more than one is available and verify account context with read/list calls first.

Risk: External API responses and model outputs may contain untrusted content.

Mitigation: Treat returned content as data, validate it before reuse, and do not execute or follow instructions embedded in API responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/fal-ai-api)
- [Maton homepage](https://maton.ai)
- [fal.ai Documentation](https://fal.ai/docs)
- [fal.ai Model Gallery](https://fal.ai/models)
- [fal.ai Queue API Reference](https://fal.ai/docs/model-endpoints/queue)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request paths, payload examples, polling workflows, generated media URLs, and account-connection guidance.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
