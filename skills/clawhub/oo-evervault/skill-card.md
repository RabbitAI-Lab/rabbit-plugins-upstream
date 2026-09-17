## Description:

Evervault (evervault.com). Use this skill for ANY Evervault request -- searching and reading data. Whenever a task involves Evervault, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Evervault through an OOMOL-connected account, including encrypting and decrypting JSON-compatible values and inspecting encrypted-token metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes pipe-to-shell installer commands from remote URLs.

Mitigation: Review before installing and prefer a pinned or independently verified oo CLI installation method outside the agent session.

Risk: Evervault operations are routed through an OOMOL-connected account.

Mitigation: Use the skill only when that routing is acceptable, and confirm payloads before executing actions that could change state or expose sensitive values.

## Reference(s):

- [Evervault homepage](https://evervault.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-evervault)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector results with data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
