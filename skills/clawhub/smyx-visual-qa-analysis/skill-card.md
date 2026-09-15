## Description:

Conducts open-ended Q&A on image content based on computer vision and large language models, supporting any questions to receive natural language responses. | 大模型视觉问答（VQA）技能，基于计算机视觉和大语言模型对图片内容进行开放式问答，支持任意提问得到自然语言回答

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit images or image URLs with open-ended questions and receive visual question-answering responses, structured reports, report links, or historical report lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media and user questions are sent to a remote service for analysis.

Mitigation: Use the skill only when users consent to remote processing, and avoid sensitive media unless the deployment has approved data handling controls.

Risk: The skill can create or reuse persistent identities and retain report history.

Mitigation: Confirm account association behavior and provide clear controls to view, manage, and delete stored identity and report data before production use.

Risk: Evidence.security reports plaintext development HTTP configuration alongside production endpoints.

Mitigation: Require HTTPS production endpoints and override or remove development HTTP settings before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files]

**Output Format:** [Markdown or JSON text, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated answer text, structured report content, report export links, and historical report listings.]

## Skill Version(s):

1.0.16 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
