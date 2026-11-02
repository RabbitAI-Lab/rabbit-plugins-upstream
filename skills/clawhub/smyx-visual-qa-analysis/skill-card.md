## Description:

Conducts open-ended Q&A on image content based on computer vision and large language models, supporting any questions to receive natural language responses. | 大模型视觉问答（VQA）技能，基于计算机视觉和大语言模型对图片内容进行开放式问答，支持任意提问得到自然语言回答

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People who provide an image file or image URL can ask open-ended questions about its contents and receive a natural-language answer. They can also request a Markdown list of their cloud-hosted question and answer history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically registers service accounts and stores account tokens on disk.

Mitigation: Wait for clearer account controls, keep user workspaces separate, and account for tokens remaining on disk.

Risk: Cloud analysis may run even when the export-only option is selected, sending media to the service.

Mitigation: Use only media you approve sending to Life Emergence and wait for the export-only behavior to be fixed.

Risk: The --api-url option may not change or constrain the service destination.

Mitigation: Do not rely on --api-url to change or limit the destination.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Natural-language answers, structured JSON reports, and Markdown tables for history results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model-generated answers; verify important information.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
