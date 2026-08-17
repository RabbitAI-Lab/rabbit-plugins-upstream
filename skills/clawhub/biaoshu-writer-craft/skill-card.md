## Description:

投标文件自动生成 helps users with provided tender or bid files by using 百炼®标书 to interpret tender requirements, generate .docx bid documents, and produce compliance review reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and procurement-support users use this skill when they have tender or bid files and need cloud-assisted tender interpretation, bid document generation, or compliance review. It is not intended for general tender advice when no file is provided.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to 百炼标书 for processing.

Mitigation: Use the skill only after confirming the user understands and accepts the external file upload and service-side processing.

Risk: The App Key is an account credential and could be exposed if pasted into chat or shared through credential-bearing links.

Mitigation: Have the user create the local config.json credential file themselves, do not ask them to paste the key, and use logout or delete config.json when the credential should no longer remain on disk.

Risk: Changing the API endpoint can send documents or credentials to a different service.

Mitigation: Keep the default 百炼标书 endpoint unless the user intentionally trusts another endpoint.

Risk: Generated bid documents and compliance findings can affect real procurement decisions.

Mitigation: Review generated documents, compliance reports, and risk findings before submission or business use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-craft)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage reference](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown-facing guidance and status text, JSON API results, HTML or Word reports, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and bid documents are written to local output paths; App Key values should not be exposed in chat.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
