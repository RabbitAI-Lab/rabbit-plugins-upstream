## Description:

Operate OpenRouter through an OOMOL-connected account using the oo CLI for read and write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect OpenRouter action schemas, run OpenRouter connector actions, and retrieve account, model, provider, generation, and credit information through an OOMOL-connected account. Write actions require confirmation of the exact payload and effect before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of a remote installer.

Mitigation: Install only from a trusted OOMOL source and inspect or verify the installer before running it.

Risk: Write actions can create completions, messages, charges, or otherwise affect the connected OpenRouter account.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running any write action.

## Reference(s):

- [ClawHub OpenRouter Skill](https://clawhub.ai/oomol/skills/oo-openrouter)
- [OpenRouter Homepage](https://openrouter.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the oo CLI, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
