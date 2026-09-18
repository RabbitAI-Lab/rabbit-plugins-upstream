## Description:

FullContact helps an agent use OOMOL-connected FullContact actions for company enrichment, person enrichment, and identity verification instead of calling the FullContact API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to enrich company or person records and verify identity signals through a connected FullContact account. It is intended for FullContact lookup and verification workflows where credentials are managed through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that pipe scripts directly into a shell.

Mitigation: Use trusted OOMOL distribution paths, prefer package-manager or signed release instructions when available, inspect installers before execution, and avoid piping remote scripts directly into a shell.

Risk: FullContact requests flow through OOMOL-connected account infrastructure.

Mitigation: Use the skill only when the organization trusts OOMOL's CLI distribution path and credential handling model for FullContact data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-full-contact)
- [FullContact homepage](https://www.fullcontact.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect the live connector schema before sending each action payload.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
