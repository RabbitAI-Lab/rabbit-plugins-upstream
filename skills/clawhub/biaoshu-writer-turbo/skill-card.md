## Description:

标书自动撰写工具通过 App Key 接入百炼®标书开放 API，拆解招标文件中的资格条件、评分办法与废标条款，生成技术标和商务标 .docx 成品，并执行合规审查以提示格式与实质性偏差。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement and bidding teams use this skill to interpret Chinese tender documents, generate bid-document drafts, and review submitted bid files for compliance issues. It is intended for mainland-China bidding workflows and requires the user to provide local tender or bid files and a 百炼®标书 App Key.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain sensitive business, pricing, and personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Use the skill only after the user understands and accepts the upload; submit only the intended local files.

Risk: The App Key is an account credential stored in a local config.json file.

Mitigation: Have the user create and manage the credential file locally, avoid pasting the App Key into chat, and delete the local config when the credential should no longer be retained.

Risk: Service responses can include links containing credential-like bind_key parameters during insufficient-balance flows.

Mitigation: Do not forward parameterized recharge or bind links; direct the user to the normal platform recharge page instead.

Risk: Generated results and uploaded files may remain associated with the user's 百炼®标书 account for a limited period.

Mitigation: Confirm that account-level retention is acceptable and direct users to manage history through the platform when needed.

Risk: Bid-document generation can consume account points, and retrying a long-running task may create duplicate work.

Mitigation: Check balance before submission, track job IDs, and resume or fetch existing jobs rather than resubmitting after a timeout.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-turbo)
- [Publisher Profile](https://clawhub.ai/user/chichihaixiaojian666)
- [Execution Guide](artifact/references/usage.md)
- [API Contract Reference](artifact/references/api.md)
- [百炼®标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Agent-facing guidance plus local HTML, Word .docx, JSON summaries, and generated bid-document .docx files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs and progress messages are primarily Simplified Chinese; generated files are written to a local output directory and may also be available through the user's 百炼®标书 account.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
