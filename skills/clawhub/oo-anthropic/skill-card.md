## Description:

Anthropic (anthropic.com) skill for reading Anthropic information and creating non-streaming messages through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Anthropic connector schemas, count message tokens, create non-streaming messages, and retrieve model information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Anthropic requests, prompts, files, and payloads are routed through OOMOL as an additional processor.

Mitigation: Install and use this skill only when OOMOL-mediated Anthropic access is intentional, and avoid sending data that should not be exposed to OOMOL.

Risk: First-time setup includes remote curl-to-bash and PowerShell Invoke-Expression installer commands.

Mitigation: Prefer a verified, version-pinned oo CLI installation path and review installer contents before execution.

Risk: The create_message action can submit a write request to Anthropic.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-anthropic)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Anthropic homepage](https://www.anthropic.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI connector actions that return JSON data and an execution identifier.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
