## Description:

This skill operates OpenRouter through an OOMOL-connected account for reading, creating, and updating OpenRouter data without calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect OpenRouter connector schemas and run OpenRouter actions for chat completions, Anthropic-format messages, model and provider discovery, generation metadata, credit balance, and API key metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that may execute downloaded code.

Mitigation: Review the installer before use, prefer a pinned signed release or package manager when available, and avoid elevated shells during installation.

Risk: Write actions can change OpenRouter account state or affect credit and billing workflows.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [OpenRouter homepage](https://openrouter.ai)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub OpenRouter skill page](https://clawhub.ai/oomol/skills/oo-openrouter)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes schema-first connector usage, setup recovery steps, and confirmation requirements for write actions.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
