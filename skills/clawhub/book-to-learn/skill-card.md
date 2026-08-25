## Description:

把任意一本书分解成日常学习任务，每日推送一张知识点卡片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to turn books into structured daily learning workflows, including knowledge-point extraction, card generation, progress tracking, and scheduled delivery through configured channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Book text, generated cards, images, and selected attachments can leave the local machine through IMA, Feishu, configured webhooks, and Catbox in Feishu webhook image mode.

Mitigation: Use non-sensitive books first, avoid Feishu webhook image mode for private content, and install only when those external transfers are acceptable.

Risk: The skill can download links from book data and send generated or downloaded files to external services with limited safeguards.

Mitigation: Review items.json relatedLinks and image fields before scheduling automated pushes.

Risk: Push modes depend on configured credentials and service accounts.

Mitigation: Prefer explicitly configured paths and credentials with least-privilege IMA, Feishu, and webhook accounts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sedey999/skills/book-to-learn)
- [Project homepage listed by the skill](https://github.com/sedey999/book-to-learn)
- [IMA API key page](https://ima.qq.com/agent-interface)
- [Feishu Open Platform app setup](https://open.feishu.cn/app)
- [book-to-skill reference project](https://github.com/virgiliojr94/book-to-skill)
- [react-paper-memo design reference](https://github.com/JustinChia/react-paper-memo)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON data files, and generated learning-card artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate PDF, PNG, HTML, and JSON files and may send generated cards, images, or attachments to configured IMA, Feishu, webhook, or Catbox endpoints.]

## Skill Version(s):

1.4.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
