## Description:

Manage OpenAI files, assistants, vector stores, batches, fine-tuning jobs, and model resources via the OpenAI API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hith3sh](https://clawhub.ai/user/hith3sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage OpenAI platform resources through ClawLink, including assistants, files, vector stores, batches, fine-tuning jobs, generations, model resources, and related API workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and allowlists an unpinned third-party plugin that handles OpenAI API credentials and broad account actions.

Mitigation: Install only if the publisher and ClawLink plugin are trusted; prefer a dedicated OpenAI project or limited API key with spending limits and audit logging.

Risk: The skill can perform destructive or costly OpenAI account operations, including deletion, cancellation, fine-tuning, batch, image, audio, and video workflows.

Mitigation: Confirm the target resource and intended effect before write operations, and monitor asynchronous jobs until completion.

## Reference(s):

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Assistants API Overview](https://platform.openai.com/docs/assistants/overview)
- [Fine-tuning Documentation](https://platform.openai.com/docs/guides/fine-tuning)
- [Batch API](https://platform.openai.com/docs/guides/batch)
- [ClawLink OpenClaw Docs](https://docs.claw-link.dev/openclaw)
- [ClawLink](https://claw-link.dev/?utm_source=clawhub&utm_medium=referral&utm_content=openai-ai)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell commands and JSON API parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected OpenAI account through ClawLink; write, destructive, costly, and asynchronous operations should be confirmed and monitored.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
