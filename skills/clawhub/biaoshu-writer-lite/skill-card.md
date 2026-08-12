## Description:

小晓投标文件生成 helps users process local tender and bid files through the 百炼标书 cloud service to interpret tender requirements, generate editable bid documents, and produce compliance review reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users, proposal teams, and bid-document operators use this skill when they have local tender or bid files and need assisted tender interpretation, bid-document generation, or compliance review. The skill is not intended for general procurement advice when no files are provided.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the 百炼标书 cloud service for processing.

Mitigation: Confirm user consent before uploading files and make clear that uploaded files and generated results are retained under the App Key account.

Risk: The App Key is an account credential stored locally by the skill.

Mitigation: Have the user create the local config.json file themselves, keep file permissions restrictive, and never paste the App Key into chat or command arguments.

Risk: Changing ZCM_BASE can redirect requests away from the default service endpoint.

Mitigation: Use the default service endpoint unless the user intentionally trusts the alternate target.

Risk: Bid-document generation consumes the App Key account's credits.

Mitigation: Check the account balance before submission and tell the user that generation is the credit-consuming step.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-lite)
- [Publisher Profile](https://clawhub.ai/user/chichihaixiaojian666)
- [Usage Guide](references/usage.md)
- [API Contract Reference](references/api.md)
- [百炼标书 Service](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼标书 Open API](https://biaoshu.zhiliaobiaoxun.com/api/open/v1)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration guidance]

**Output Format:** [Human-facing text or Markdown summaries, generated .docx bid documents, HTML or Word reports, and JSON task results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files are written under biaoshu-bailian-files/ by default or to a user-selected output path.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
