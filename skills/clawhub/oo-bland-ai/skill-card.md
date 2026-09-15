## Description:

Bland AI connector skill for searching and reading account, call, transcript, and voice data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Bland AI account status, call details, transcript phrases, and voice information through the oo CLI after connecting a Bland AI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Bland AI account details, call metadata, transcripts, and voice information through a connected OOMOL account.

Mitigation: Install and use it only when OOMOL is trusted for this account, and review the requested action before exposing sensitive call or transcript data.

Risk: First-time setup documentation includes remote installer commands that execute downloaded scripts directly.

Mitigation: Prefer installing the oo CLI through a verified official method or inspect installer scripts before running them.

## Reference(s):

- [Bland AI homepage](https://www.bland.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bland-ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown instructions with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing connector requests.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
