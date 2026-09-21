## Description:

Baidu Qianfan (qianfan.cloud.baidu.com). Use this skill for ANY Baidu Qianfan request - reading, creating, updating, and deleting data. Whenever a task involves Baidu Qianfan, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Baidu Qianfan through an OOMOL-connected account for chat, completion, responses, embeddings, reranking, AI search, OCR, image generation, video generation, file, and batch workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports cloud actions that can upload files, create generation or batch jobs, cancel jobs, and delete stored responses.

Mitigation: Require explicit user confirmation for write or destructive actions and confirm the target payload before execution.

Risk: The first-time setup path may install the oo CLI from an external installer script.

Mitigation: Install only when needed, use a trusted or verified oo CLI install source, and review the installer source where possible.

Risk: Request payloads can become inaccurate if connector schemas change.

Mitigation: Inspect the live action schema before constructing payloads for Baidu Qianfan actions.

## Reference(s):

- [Baidu Qianfan homepage](https://qianfan.cloud.baidu.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Baidu Qianfan skill page](https://clawhub.ai/oomol/skills/oo-qianfan)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI qianfan connector and should inspect the live action schema before execution.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
