## Description:

Wiza enables agents to read, create, and update Wiza data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check Wiza credits, search prospects, retrieve lists and reveal records, and start individual contact enrichment reveals through a connected Wiza account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance uses downloaded installer scripts executed directly in a shell.

Mitigation: Review the oo CLI installation path before use, prefer verified official packages or inspectable installers, and apply integrity checks where available.

Risk: The Wiza connector includes write actions that can change account state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions such as starting an individual reveal.

## Reference(s):

- [ClawHub Wiza skill page](https://clawhub.ai/oomol/skills/oo-wiza)
- [Wiza homepage](https://wiza.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payload construction; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
