## Description:

Uploads tender and bid files to 百炼®标书 to interpret procurement requirements, generate editable bid documents, review compliance risks, and compare 2-3 bid files for similarity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, and bid writers use this skill to analyze tender files, generate bid documents, review bid compliance, and run pre-submission similarity checks through the 百炼®标书 cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain confidential business, pricing, personal, or client information and are uploaded to 百炼®标书 for processing.

Mitigation: Use the skill only when the user is authorized to upload those files to the vendor service and has acknowledged the data handling.

Risk: The API key is an account credential.

Mitigation: Keep the API key only in the local config.json file and do not ask users to paste or repeat it in chat.

Risk: The background progress checker can call the vendor service too frequently.

Mitigation: Raise progress-stream polling to a sane interval such as several seconds before using it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-smart-pro)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge-base field reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON summaries, HTML/DOCX reports, and DOCX bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local config.json API key and uploads user-provided tender or bid files to 百炼®标书 for processing.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
