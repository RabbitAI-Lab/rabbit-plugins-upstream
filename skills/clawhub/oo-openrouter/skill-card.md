## Description:

OpenRouter lets an agent use an OOMOL-connected OpenRouter account to inspect schemas, run connector actions, and read or create OpenRouter data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access OpenRouter through an OOMOL-connected account for chat completions, messages, usage, credits, models, providers, endpoints, and routing-related discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenRouter access is mediated through OOMOL.

Mitigation: Install and use this skill only when the user intends to use an OOMOL-connected OpenRouter account.

Risk: Some actions can spend credits, create charges, or change account-related data.

Mitigation: Confirm the exact payload and expected effect before running write actions or account-affecting operations.

Risk: First-time setup may require installing the oo CLI and connecting an OpenRouter account.

Mitigation: Verify the oo CLI installer source and run setup steps only after an authentication or connection failure indicates they are needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openrouter)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OpenRouter homepage](https://openrouter.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write actions require confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
