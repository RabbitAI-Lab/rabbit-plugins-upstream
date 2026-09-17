## Description:

Docparser (docparser.com) skill for reading, creating, and updating parser data through the OOMOL Docparser connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Docparser through an OOMOL-connected account, including listing parsers, retrieving document results and status, importing public documents, and uploading document content when confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote pipe-to-shell installer commands for the oo CLI.

Mitigation: Review setup before installing; prefer manually installing the oo CLI from a verified, versioned source instead of letting an agent run installer pipelines automatically.

Risk: Docparser write actions can upload document content or otherwise change service state.

Mitigation: Confirm the exact parser, document, payload, and expected effect with the user before running uploads or other state-changing actions.

## Reference(s):

- [ClawHub Docparser skill page](https://clawhub.ai/oomol/skills/oo-docparser)
- [Docparser homepage](https://docparser.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Docparser action schemas before constructing payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
