## Description:

上传招标或投标文件后，协助完成招标解读、投标文件生成、标书审查和投标文件相似度查重。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to interpret tender files, generate editable bid documents, review bid compliance risks, and compare bid documents for similarity before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain business, pricing, and personal data and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm user consent and processing rights before upload, use only user-provided local files, and review the service retention and account controls.

Risk: The skill depends on an API key stored locally for the user's 百炼®标书 account.

Mitigation: Keep the API key out of chat and logs, store it only in the local configuration file, and reset it through the service if exposure is suspected.

Risk: Generated bid documents, compliance reviews, and similarity checks can miss issues or require professional judgment.

Mitigation: Review generated documents and risk reports before submission, and treat similarity results as internal review signals rather than legal determinations.

## Reference(s):

- [Usage Guide](references/usage.md)
- [Open API Contract](references/api.md)
- [Knowledge Base Fields](references/knowledge-fields.md)
- [百炼®标书 Service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-craft)
- [Publisher Profile](https://clawhub.ai/user/chichihaixiaojian666)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Natural-language responses, JSON summaries, HTML/Word reports, and .docx bid-document files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local report paths, short-lived document download links, risk summaries, and editable bid-document artifacts.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
