## Description:

Foxit Cloud API (cloudapi.fuxinsoft.cn) supports agent requests for reading, creating, and updating data through the Foxit Cloud API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Foxit Cloud API through an OOMOL-connected account for PDF conversion, OCR, compression, extraction, protection, watermarking, task tracking, upload, and download workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User documents may be sent to Foxit Cloud API processing services for conversion, OCR, comparison, compression, page manipulation, password, merge, split, and related workflows.

Mitigation: Use only with documents approved for cloud processing through the connected OOMOL/Foxit account, and confirm sensitive document operations before execution.

Risk: The skill includes CLI installation commands that fetch and execute remote installer scripts.

Mitigation: Review CLI installation commands manually before running them and prefer an already installed, trusted oo CLI when available.

## Reference(s):

- [Foxit Cloud API homepage](https://cloudapi.fuxinsoft.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fuxin)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and return connector responses as JSON.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
