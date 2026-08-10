## Description:

Conducts open-ended Q&A on image content based on computer vision and large language models, supporting any questions to receive natural language responses. | 大模型视觉问答（VQA）技能，基于计算机视觉和大语言模型对图片内容进行开放式问答，支持任意提问得到自然语言回答

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask natural-language questions about images or image URLs and receive visual Q&A answers, structured analysis, and report/history links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, URLs, questions, and report/history requests are sent to lifeemergence.com cloud services.

Mitigation: Review the cloud account, retention, and deletion model before use, and avoid sensitive media unless that data handling is acceptable.

Risk: The skill silently creates or reuses a local identity and stores local workspace data such as smyx-api-key.txt and SQLite database records.

Mitigation: Control access to the workspace data directory, rotate or remove local identity artifacts when needed, and review stored history before sharing the workspace.

Risk: Model-generated visual answers may be incomplete, incorrect, or misleading for important decisions.

Mitigation: Treat answers as reference material and verify important findings against source media or trusted domain expertise.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown or JSON text from CLI execution, with optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs visual Q&A answers, structured analysis content, report links, or history lists based on an image/video file or URL and a user question.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
