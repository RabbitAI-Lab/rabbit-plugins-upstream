## Description:

Supadata lets agents query Supadata through the OOMOL oo CLI to retrieve account details, YouTube metadata and transcripts, YouTube search results, and website links or Markdown content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to search or read Supadata-backed content, including YouTube channel, playlist, video, transcript, and web page data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask the agent to run remote installer scripts for the OOMOL CLI.

Mitigation: Review the installer path before use and prefer a signed, versioned, checksum-verified installer or package manager flow; do not run first-time setup automatically without explicit approval.

## Reference(s):

- [Supadata homepage](https://supadata.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses include data and an execution id.]

## Skill Version(s):

1.0.4 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
