## Description:

Guides an agent to operate Dune through the OOMOL `oo` CLI for inspecting schemas, executing saved queries, checking execution status, retrieving results, and listing account queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to access Dune data through an OOMOL-connected account without handling raw Dune API credentials directly. It supports reading query metadata, running saved queries, polling status, and retrieving JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts executed directly in a shell.

Mitigation: Review before installing and prefer a verified package-manager path or pinned installer for the oo CLI.

## Reference(s):

- [Dune homepage](https://dune.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Dune skill page](https://clawhub.ai/oomol/skills/oo-dune)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects live action schemas to be inspected before constructing request payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
