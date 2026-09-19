## Description:

KIE.AI lets agents operate the KIE.AI connector through an OOMOL-connected account to check account credits and convert generated file URLs into temporary direct download URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to run KIE.AI connector actions through the oo CLI on an intended OOMOL-connected account. It is primarily useful for checking remaining KIE.AI credits and converting generated KIE.AI file URLs into temporary direct download URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that run downloaded scripts.

Mitigation: Review setup before installation, prefer an official verified package or separately downloaded installer with integrity checks, and avoid running installers in an administrator shell unless required.

Risk: Connector commands operate on the connected KIE.AI account.

Mitigation: Use the skill only for explicit KIE.AI connector tasks on the intended account, and confirm payloads and effects before running any action that changes or deletes data.

## Reference(s):

- [KIE.AI homepage](https://kie.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kie-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; action responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
