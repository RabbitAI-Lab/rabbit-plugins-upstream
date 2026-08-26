## Description:

标书智能制作工具，凭 App Key 调用开放 API 完成招标文件解读、评分点应答、投标文件生成、排版和合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid-writing teams use this skill to analyze tender files, identify scoring criteria and disqualification risks, generate editable bid documents, and review bid submissions for compliance. The skill is intended for cases where the user explicitly provides local tender or bid files and understands they will be processed by the vendor cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain sensitive business, pricing, and personal information and are uploaded to the vendor cloud service.

Mitigation: Confirm user awareness and consent before upload, use only user-provided local files, and disclose that files and generated results are handled under the App Key account.

Risk: The App Key is a full account credential and local config file access could expose it.

Mitigation: Keep the App Key out of chat, store it only in the local skill config, avoid echoing credential-bearing links, and review the credential file location before use.

Risk: Generated bid documents may consume account points and long-running generation can continue after a local tool timeout.

Mitigation: Check account balance before generation, explain that document generation consumes points, and resume existing jobs rather than resubmitting duplicate generation requests.

Risk: Generated bid content, compliance findings, and knowledge-base field matches may be incomplete or require business judgment.

Mitigation: Review generated documents and reports before submission, preserve unknown fields as placeholders, and do not infer missing company, financial, pricing, signature, or seal information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-radar)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge-base field guide](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Human-facing guidance plus generated DOCX and HTML or Word report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include bid interpretation summaries, compliance findings, local report paths, generated .docx bid files, progress updates, and account point balance notices.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
