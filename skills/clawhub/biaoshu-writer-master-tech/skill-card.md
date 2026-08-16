## Description:

基于百炼®标书开放 API，帮助用户解读招标文件、生成技术标投标文件，并对投标文件进行合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and proposal teams use this skill to process local tender and bid documents through the 百炼®标书 service, producing tender interpretation, technical bid drafts, and compliance review outputs. It is intended for user-approved bidding workflows where files may be uploaded to the disclosed service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain commercial, pricing, and personal information and are uploaded to the disclosed 百炼®标书 service.

Mitigation: Install and run the skill only after confirming the user understands and approves the upload and server-side processing.

Risk: The App Key is an account credential for the service.

Mitigation: Keep the App Key out of chat, store it only in the local config.json credential file, and avoid forwarding service links that include credential parameters.

Risk: Generated bid documents can consume account points.

Mitigation: Check account balance before generation and make the user aware that bid-document generation is the billable step.

Risk: A modified API base could send files to an unintended endpoint.

Mitigation: Confirm the configured API base is the intended biaoshu.zhiliaobiaoxun.com domain before processing sensitive documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-tech)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](artifact/references/api.md)
- [Usage guide](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance, terminal output, JSON API results, HTML or Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local tender or bid files, writes reports and bid documents under the configured output directory, and uses a local App Key credential file.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
