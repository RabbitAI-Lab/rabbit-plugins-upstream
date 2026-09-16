## Description:

ConvertAPI (convertapi.com) supports ConvertAPI requests through an OOMOL-connected account, including converting public PDF URLs to DOCX files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run ConvertAPI connector actions through the oo CLI, especially converting publicly accessible PDF files into DOCX outputs and receiving temporary download URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified internet installer scripts, which may introduce installation risk if run without validation.

Mitigation: Review the setup path before installing; prefer a verified package manager or a downloaded installer with a published checksum or signature.

Risk: Connector actions should only be used for intended ConvertAPI tasks.

Mitigation: Inspect the live action schema before running connector actions and confirm payloads for actions that change state.

## Reference(s):

- [ConvertAPI homepage](https://www.convertapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub ConvertAPI skill page](https://clawhub.ai/oomol/skills/oo-convertapi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return temporary download URLs for converted files through the ConvertAPI connector.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
