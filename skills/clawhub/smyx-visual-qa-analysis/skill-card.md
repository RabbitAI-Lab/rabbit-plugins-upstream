## Description:

Conducts open-ended Q&A on image content based on computer vision and large language models, supporting any questions to receive natural language responses. | 大模型视觉问答（VQA）技能，基于计算机视觉和大语言模型对图片内容进行开放式问答，支持任意提问得到自然语言回答

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and end users can use this skill to ask natural-language questions about images or image URLs and receive visual question-answering analysis. It also supports retrieving prior cloud-hosted visual question-answering reports when history-related requests are made.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, videos, and questions may be sent to the configured cloud service for visual analysis.

Mitigation: Use the skill only with content appropriate for that service and review the configured service endpoint before deployment.

Risk: The skill can create or reuse a local account identity and store tokens in a workspace SQLite database.

Mitigation: Run it in a controlled workspace and review local token and database retention practices before use.

Risk: Broad history-related triggers can retrieve cloud report history and report links automatically.

Mitigation: Confirm that history retrieval is intended for the user context before exposing returned history or report links.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](artifact/references/api_doc.md)
- [Supplemental API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON visual question-answering results, with optional saved text output and Markdown tables for history results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured answers, report links, cloud history listings, and guidance to verify model-generated answers before important use.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
