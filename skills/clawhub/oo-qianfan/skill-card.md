## Description:

Helps agents read, create, update, and delete Baidu Qianfan data through OOMOL's oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to invoke Baidu Qianfan actions through OOMOL, including chat and completion, embeddings, reranking, file and batch workflows, image and video generation tasks, and OCR or document processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of a remote installer script for the OOMOL CLI.

Mitigation: Review the installer path before installing, and prefer a pinned or package-manager install with checksum or signature verification.

Risk: Some Baidu Qianfan actions can write data, upload files, start generation tasks, cancel jobs, or delete stored responses.

Mitigation: Require explicit confirmation for the exact payload and target before write, upload, generation, cancellation, or deletion actions.

## Reference(s):

- [ClawHub Baidu Qianfan skill page](https://clawhub.ai/oomol/skills/oo-qianfan)
- [Baidu Qianfan homepage](https://qianfan.cloud.baidu.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses live connector schemas before action execution and requires explicit confirmation for write, upload, generation, cancellation, or deletion actions.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
