## Description:

tl;dv (tldv.io) helps agents read, create, and update tl;dv data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve tl;dv meetings, notes, and transcripts, list meetings with filters, and import publicly accessible recordings after confirming state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands that execute downloaded scripts directly.

Mitigation: Review the oo CLI installation path first; prefer a pinned, signed release or verify the installer before running it.

Risk: Connecting tl;dv may grant the connector access to meetings, notes, and transcripts in the connected account.

Mitigation: Connect only an account and scopes appropriate for the intended use, and confirm write actions such as meeting import before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tldv)
- [tl;dv homepage](https://tldv.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return tl;dv meeting data, notes, transcripts, connector execution metadata, or setup guidance depending on the requested action.]

## Skill Version(s):

1.0.2 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
