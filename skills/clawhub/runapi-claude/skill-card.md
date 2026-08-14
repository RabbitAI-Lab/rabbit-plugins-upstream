## Description:

Call Claude models through RunAPI using the Anthropic Messages protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure agents or compatibility clients for Claude requests through RunAPI, including chat, streaming, vision, tool use, reasoning controls, token counting, and result verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, files, images, and tool inputs sent through configured clients are transmitted to RunAPI.

Mitigation: Install only when routing Claude requests through RunAPI is intended, verify ANTHROPIC_BASE_URL before use, and avoid sending data that should not leave the approved provider path.

Risk: Using the wrong protocol shape, model ID, or retry behavior can produce failed or ambiguous API results.

Mitigation: Follow the primary Anthropic Messages recipe, require final text, stop reason, and authoritative usage, and apply only the documented single shape correction or safe pre-response transport retry.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-claude)
- [RunAPI Claude Documentation](https://runapi.ai/models/claude.md)
- [RunAPI Anthropic Provider Documentation](https://runapi.ai/providers/anthropic.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [RunAPI Claude Homepage](https://runapi.ai/models/claude)
- [Claude Compatibility Protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, configuration]

**Output Format:** [Markdown guidance with code snippets, environment variable configuration, and protocol verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL for configured clients; actual token usage from the provider remains authoritative.]

## Skill Version(s):

0.2.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
