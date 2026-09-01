## Description:

Alibaba's flagship Qwen reasoning model (2.4T-parameter MoE), strong at complex reasoning, code engineering and long-context analysis, with text and image input support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's hosted Qwen 3.8 Max CLI for text generation, reasoning, code engineering, long-context analysis, and image-informed prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly provided media files are sent to dLazy-hosted endpoints for processing.

Mitigation: Use the skill only for data appropriate for the dLazy service, and avoid passing sensitive local files unless the user has approved that upload.

Risk: The dLazy CLI stores an API key in the local user configuration when persistent authentication is used.

Mitigation: Use per-invocation environment variables or npx for one-off use when persistent local configuration is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists a third-party executable on the system.

Mitigation: Prefer the pinned npx invocation for temporary use, or review the referenced package and source metadata before global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON responses from the dLazy CLI, with agent-facing text or markdown summaries as appropriate]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt input, up to 10 image references, dry-run cost estimates, asynchronous task IDs, timeout control, and optional result saving.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
