## Description:

链企投标文件生成 helps agents interpret mainland-China tender documents, draft bid documents, and run compliance reviews through the 百炼®标书 cloud API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and agents use this skill to analyze Chinese tender documents, generate editable bid-document files, and review bid submissions for disqualification or compliance risks. Use requires an App Key and user consent to upload tender or bid files to the 百炼®标书 service.

### Deployment Geography for Use:

Mainland China bidding workflows

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, or personal data and are uploaded to the 百炼®标书 cloud service.

Mitigation: Confirm user consent before upload, submit only files the user explicitly provides, and disclose that uploaded files and generated results may remain available under the App Key owner's account for a limited period.

Risk: The API base URL can be overridden, which could redirect sensitive uploads and the App Key away from the stated official service.

Mitigation: Before use, verify that ZCM_BASE is unset and config.json does not contain a custom base value; use the official 百炼®标书 endpoint.

Risk: The App Key is a full account credential stored locally.

Mitigation: Have the user write the key directly to the local config file, keep file permissions restricted, never paste or echo the key in chat, and delete the local credential when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-ace)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [Usage manual](artifact/references/usage.md)
- [API contract reference](artifact/references/api.md)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown text plus generated .docx bid documents and HTML or Word reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and product labels are primarily Simplified Chinese; bid generation consumes the App Key owner's account credits.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
