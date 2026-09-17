## Description:

Amilia lets agents search and read Amilia activities and programs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve Amilia program and activity data without calling the Amilia API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could run arbitrary local code.

Mitigation: Review before installing; avoid curl|bash or irm|iex unless the installer source is independently trusted and verified. Prefer a pinned package or checksum/signature-verified install path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-amilia)
- [Amilia homepage](https://www.amilia.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action responses are JSON returned by the oo CLI for read-only Amilia retrieval and listing tasks.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
