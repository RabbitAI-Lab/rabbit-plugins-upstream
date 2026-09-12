## Description:

fal.ai lets agents run fal.ai model inference through Maton-managed authentication for image generation, video generation, audio processing, upscaling, and related AI model tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to authenticate to fal.ai through Maton and run queued model inference workflows such as image generation, video generation, upscaling, text-to-speech, and status or result polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the Maton CLI from an unexpected package source could run unintended software.

Mitigation: Verify the Maton package or Homebrew tap before installation and avoid elevated privileges unless the environment requires them.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or copied output.

Mitigation: Prefer OAuth through the Maton CLI; when an API key is unavoidable, keep it in the process environment, never print or persist it, and rotate it if exposed.

Risk: Connection creation or POST, PUT, PATCH, and DELETE calls may spend credits, alter account state, or cancel running work.

Mitigation: Require explicit user confirmation for the target connection, request payload, and intended effect before creating connections or making write calls.

Risk: The Maton API passthrough can reach endpoints beyond the examples when the connected account is authorized.

Mitigation: Use read or list calls first, apply least privilege during authorization, and specify the target connection when multiple fal.ai connections exist.

Risk: fal.ai responses may include temporary media URLs or user/account data that should not be broadly exposed.

Mitigation: Extract only fields needed for the task and avoid writing raw responses to logs or files unless the user requested it.

## Reference(s):

- [fal.ai Documentation](https://fal.ai/docs)
- [fal.ai Model Gallery](https://fal.ai/models)
- [fal.ai Queue API Reference](https://fal.ai/docs/model-endpoints/queue)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Skill release page](https://clawhub.ai/byungkyu/skills/fal-ai-api)
- [Publisher profile](https://clawhub.ai/user/byungkyu)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces API workflow guidance and command examples; fal.ai responses may include temporary media URLs or account data and should be minimized before display or storage.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
