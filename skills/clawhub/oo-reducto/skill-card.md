## Description:

Reducto lets agents use an OOMOL-connected Reducto connector to extract structured data, parse documents, and split documents into sections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Reducto document-processing actions through an OOMOL-connected account, including extracting structured JSON, parsing documents into chunks and metadata, and splitting documents into named sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes one-line remote installer commands.

Mitigation: Review installer contents before execution, prefer official package-manager installation when available, and avoid elevated shells.

Risk: Document-processing requests may send user-selected files or URLs to Reducto through the connected account.

Mitigation: Confirm that documents are appropriate for the connected Reducto account and inspect the live action schema before submitting payloads.

## Reference(s):

- [ClawHub Reducto skill page](https://clawhub.ai/oomol/skills/oo-reducto)
- [Reducto homepage](https://reducto.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
