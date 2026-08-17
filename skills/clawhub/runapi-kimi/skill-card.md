## Description:

Call the Kimi API (kimi-k3, kimi-k2.7-code, kimi-k2.6, kimi-k2.5) through RunAPI using OpenAI-compatible Chat Completions. Use for Kimi text chat, streaming, or an existing compatibility client that needs the conditional reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call Kimi models through RunAPI with OpenAI-compatible Chat Completions, including streaming and compatibility-client setup when required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached content are sent to an external provider when using RunAPI.

Mitigation: Use this skill only for approved RunAPI workloads, and do not send secrets or regulated data unless that use is approved.

Risk: Project environment variables can route compatible clients to RunAPI unintentionally.

Mitigation: Scope OPENAI_API_KEY and OPENAI_BASE_URL to the project that should use RunAPI, and review those settings before execution.

## Reference(s):

- [Kimi on RunAPI documentation](https://runapi.ai/models/kimi.md)
- [Moonshot AI provider page](https://runapi.ai/providers/moonshot-ai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Kimi compatibility protocols](references/compatibility-protocols.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-kimi)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline Python examples and environment variable configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are guidance for using external RunAPI endpoints; prompts and attached content may be sent to the provider.]

## Skill Version(s):

0.2.3 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
