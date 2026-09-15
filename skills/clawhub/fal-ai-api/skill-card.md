## Description:

fal.ai API integration with managed API key authentication for running image generation, video generation, audio processing, transcription, upscaling, and other fal.ai models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to call fal.ai models through Maton-managed authentication for media generation, transcription, upscaling, request status checks, and queue result retrieval. It also documents optional hosted functions and triggers for approved automation around fal.ai tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton CLI or SDK installation can introduce supply-chain exposure if the distribution path is not trusted.

Mitigation: Verify the Maton CLI or SDK distribution path before installing and keep versions pinned to reviewed releases.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or child processes.

Mitigation: Prefer OAuth login and use raw HTTP with MATON_API_KEY only where the CLI cannot be installed; rotate any key that was printed, committed, or pasted.

Risk: Creating fal.ai connections, write requests, hosted functions, trigger destinations, or webhooks can authorize account access or persistent automation.

Mitigation: Require explicit user approval for each connection, write action, function deployment, trigger destination, webhook callback, and unattended execution path.

Risk: External callback URLs and trigger destinations can continuously send generated media URLs, prompts, or event data to a third-party host.

Mitigation: Prefer polling and platform-owned destinations; use external URLs only when supplied by the user after reviewing the host, payload, and persistence.

Risk: Third-party API responses and event payloads may contain untrusted instructions or data.

Mitigation: Treat returned content and payloads as data, avoid executing or interpolating it into commands, and require a user-reviewed handler for local event execution.

## Reference(s):

- [fal.ai Documentation](https://fal.ai/docs)
- [fal.ai Model Gallery](https://fal.ai/models)
- [fal.ai Queue API Reference](https://fal.ai/docs/model-endpoints/queue)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/fal-ai-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, API calls, markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and Python or JavaScript code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include generated media URLs, request IDs, queue statuses, API responses, and automation configuration guidance.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
