## Description:

MinerU helps agents operate the MinerU connector through an OOMOL-connected account for creating extraction tasks and batches and retrieving extraction status and result URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run MinerU document extraction workflows from an agent, including creating precise extraction tasks or batches from document URLs and checking their results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Prefer an official version-pinned installer, or inspect and verify the installer before running it.

Risk: Write actions create MinerU extraction tasks or batches from supplied document URLs.

Mitigation: Confirm the exact document URLs and expected effect with the user before creating tasks or batches.

Risk: Connector schemas can change over time.

Mitigation: Inspect the live action schema before constructing or running connector payloads.

## Reference(s):

- [ClawHub MinerU skill page](https://clawhub.ai/oomol/skills/oo-mineru)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [MinerU homepage](https://mineru.net)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MinerU task or batch status, result URLs, and connector execution metadata when returned by the service.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
