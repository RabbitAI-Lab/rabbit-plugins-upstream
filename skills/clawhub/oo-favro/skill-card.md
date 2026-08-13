## Description:

Favro routes agent requests for reading, creating, and updating Favro data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Favro organizations, collections, widgets, boards, and cards, and to create or update cards through an OOMOL-connected Favro account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update Favro cards in the connected account.

Mitigation: Confirm the exact target board or card and payload before running write actions.

Risk: First-time CLI installation or account connection changes the user's local setup and account linkage.

Mitigation: Proceed with installation, sign-in, or Favro connection only when the user trusts OOMOL's connector flow.

## Reference(s):

- [ClawHub Favro Skill](https://clawhub.ai/oomol/skills/oo-favro)
- [Favro Homepage](https://www.favro.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
