## Description:

Lacuna helps agents search and read Lacuna's machine-learning research map, including papers, research directions, authors, venues, institutions, and generated hypotheses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use Lacuna to search machine-learning research and retrieve paper, author, direction, and hypothesis context through OOMOL's oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute code with local user permissions.

Mitigation: Install the oo CLI through a trusted package manager or a verified, pinned installer, and avoid piping remote scripts directly into a shell unless OOMOL's installer path is trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lacuna)
- [Lacuna homepage](https://lacuna.tiptreesystems.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented Lacuna connector actions; agents should inspect live action schemas before requests.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
