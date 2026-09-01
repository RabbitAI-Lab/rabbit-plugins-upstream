## Description:

Configures OpenClaw to use PZERO prepaid inference through an OpenAI-compatible custom provider with a Bearer pzero_ API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeffcryptoo](https://clawhub.ai/user/jeffcryptoo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure OpenClaw chat models to route through PZERO's prepaid OpenAI-compatible API, then smoke-test model discovery and a paid chat completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PZERO_API_KEY could be exposed if copied into checked-in configuration or prompts.

Mitigation: Keep PZERO_API_KEY in environment storage and reference it from configuration rather than hard-coding the key.

Risk: Configured model requests are sent to PZERO's API and may consume prepaid balance.

Mitigation: Review the provider and pricing before installing, and keep only the balance intended for use on the account.

## Reference(s):

- [PZERO Agents](https://pzero.studio/agents)
- [OpenClaw Custom Providers and Base URLs](https://docs.openclaw.ai/gateway/config-tools#custom-providers-and-base-urls)
- [PZERO MCP Documentation](https://docs.pzero.studio/agents/mcp)
- [ClawHub Skill Page](https://clawhub.ai/jeffcryptoo/skills/pzero)

## Skill Output:

**Output Type(s):** [configuration, shell commands, guidance]

**Output Format:** [Markdown with JSON configuration and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PZERO_API_KEY and curl; paid API calls require confirmed USDC balance.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
