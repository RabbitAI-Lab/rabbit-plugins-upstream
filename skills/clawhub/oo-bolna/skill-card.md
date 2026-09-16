## Description:

Bolna helps agents search and read data from Bolna through the OOMOL-connected oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Bolna connector schemas and retrieve read-only voice agent, execution, raw log, workspace user, and agent execution history data from an authenticated Bolna workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes mutable remote installer commands for the oo CLI without artifact-level integrity verification.

Mitigation: Install the OOMOL CLI through a trusted process, prefer a pinned release with integrity verification, and do not allow an agent to run installer commands automatically.

## Reference(s):

- [ClawHub Bolna Skill](https://clawhub.ai/oomol/skills/oo-bolna)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Bolna Homepage](https://www.bolna.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated OOMOL account, installed oo CLI, and connected Bolna provider.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
