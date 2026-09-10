## Description:

投标文件智能制作 helps agents use the 百炼®标书 service to interpret tender documents, generate finished bid documents, review compliance risks, and compare bid-document similarity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams, proposal writers, and procurement-response specialists use this skill to analyze tender requirements, prepare bid documents, check submission risks, and compare bid files before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Install and use the skill only when the user is authorized to process those files and accepts upload to that service.

Risk: The skill uses a billable API key and includes account setup flows involving phone numbers or SMS codes.

Mitigation: Keep API keys, SMS codes, and phone numbers out of chat; configure credentials only in the local config file and confirm billing expectations before use.

Risk: The security summary flags under-disclosed persistent-storage behavior.

Mitigation: Review the local metadata storage behavior before installation and remove stored project metadata if it is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-smart-pro)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com)
- [API overview](references/api.md)
- [API authentication](references/api-auth.md)
- [Bid workflow API](references/api-bid-workflow.md)
- [Compliance API](references/api-compliance.md)
- [Duplicate check API](references/api-duplicate.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Text and Markdown guidance, local configuration instructions, generated report files, JSON results, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and documents may be stored locally or retrieved through short-lived platform download links.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
