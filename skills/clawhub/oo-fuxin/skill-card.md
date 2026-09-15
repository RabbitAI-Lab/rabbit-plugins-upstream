## Description:

Enables an agent to operate Foxit Cloud API through OOMOL's oo CLI for PDF conversion, OCR, upload, download, task tracking, quota checks, and document manipulation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Foxit Cloud API document-processing workflows through an OOMOL-connected account. It supports PDF conversion, creation, compression, merge and split operations, OCR, extraction, comparison, watermarking, protection, upload, download, quota checks, and task-status tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can expose users to unsafe automatic installation commands if an agent runs installer pipelines without review.

Mitigation: Install the OOMOL oo CLI only from official, verified instructions and review any installation script before execution.

Risk: Document conversion, OCR, watermarking, page manipulation, protection, upload, download, and related jobs may process user files or change remote service state.

Mitigation: Require user confirmation for the exact payload and expected effect before submitting document-processing or state-changing actions.

Risk: Foxit Cloud API actions depend on the user's connected OOMOL credential and service quota.

Mitigation: Handle authentication, connection, credential-expiration, and billing failures as user-visible setup or account issues before retrying.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-fuxin)
- [Foxit Cloud API Homepage](https://cloudapi.fuxinsoft.cn)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
