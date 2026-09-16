## Description:

Baidu Qianfan lets agents read, create, update, and delete Baidu Qianfan resources through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Baidu Qianfan workflows through the oo CLI, including chat and completion tasks, embeddings, reranking, AI search, image and video generation, files, batches, models, stored responses, and OCR or document processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts in a shell.

Mitigation: Review setup steps before installation and prefer a verified, versioned, or signed oo CLI release path.

Risk: Write actions can create, cancel, upload, or otherwise change Baidu Qianfan resources.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Destructive actions can remove stored Baidu Qianfan data.

Mitigation: Confirm the target identifier and get explicit user approval before running destructive actions.

## Reference(s):

- [Baidu Qianfan homepage](https://qianfan.cloud.baidu.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Baidu Qianfan ClawHub release](https://clawhub.ai/oomol/skills/oo-qianfan)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
