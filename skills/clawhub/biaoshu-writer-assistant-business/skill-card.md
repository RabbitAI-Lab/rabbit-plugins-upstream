## Description:

This skill helps agents use the 百炼®标书 service to interpret tender files, draft editable commercial bid documents, and review bid submissions for compliance after the user supplies local files and confirms upload to the service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and their agents use this skill to analyze tender documents, generate editable commercial bid .docx files, and review bid submissions for compliance before filing. It is intended for workflows where users can provide local tender or bid files, manage their own App Key, and accept upload to the 百炼®标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential business, pricing, or personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Confirm user consent before upload and use only the stated service domain for these workflows.

Risk: The App Key is an account credential that can expose service access or account credits if shared in chat.

Mitigation: Have the user store the App Key locally in the skill config file and never paste, echo, or transmit it in conversation.

Risk: Bid generation uses account credits and can create editable content that may require human validation before submission.

Mitigation: Check balance and user intent before generation, then have qualified staff review generated bid documents and compliance reports before filing.

Risk: Generated outputs and service-side task results may remain associated with the user's account for a limited retention period.

Mitigation: Tell users that uploaded files and outputs are processed under their account and should be managed through the service when retention or deletion matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-business)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [Usage guide](artifact/references/usage.md)
- [API contract reference](artifact/references/api.md)
- [Knowledge-base field reference](artifact/references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain-text agent responses with local HTML, Word, and DOCX output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces bid interpretation summaries and reports, editable commercial bid documents, compliance review reports, progress updates, and credential setup guidance.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
