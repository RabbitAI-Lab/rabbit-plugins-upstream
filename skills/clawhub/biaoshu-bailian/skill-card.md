## Description:

Uploads tender and bid documents to the 百炼®标书 cloud service to interpret tender requirements, generate bid documents, review compliance risks, and compare 2-3 bid files for similarity or duplicate-content risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams, procurement-support staff, and proposal writers use this skill to analyze tender files, generate editable bid documents, produce compliance review reports, and check legally held bid files for similarity risks before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Use the skill only after confirming the user understands and accepts cloud processing and account-level result retention.

Risk: The API key grants access to the user's 百炼®标书 account.

Mitigation: Keep the API key out of chat and store it only in the local config file described by the skill.

Risk: Similarity checking of bid documents can involve sensitive files and may be misread as a legal determination.

Mitigation: Confirm the user has authority to process all files and present similarity results as internal risk indicators, not legal conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-bailian)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge fields reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance and command orchestration that can produce JSON results, HTML or Word reports, and DOCX bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents consume account word balance; uploaded documents and results are retained by the third-party service under the user's API-key account.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
