## Description:

Assists with Chinese tender and bid workflows by uploading user-provided tender or bid documents to 百炼标书 for interpretation, bid-document generation, compliance review, and duplicate/similarity risk checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to interpret tender requirements, generate draft bid documents, review submitted bid files for compliance issues, and compare bid files for similarity risk before submission. It is intended for workflows where the user has authority to upload the documents to the 百炼标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Use the skill only with documents the user is authorized to process, confirm comfort with cloud upload before first use, and avoid uploading material that should not leave the user's environment.

Risk: API keys, phone numbers, SMS codes, or bind-key URLs could expose a paid account if shared in chat.

Mitigation: Have the user create and store the API key themselves, do not request or echo credentials, and provide only non-credentialed platform URLs for account or billing actions.

Risk: Generated outputs and project metadata may persist locally, including project metadata under ~/.zcm/projects.json until removed.

Mitigation: Review output locations before running tasks and remove cached metadata, generated files, or the skill-local config file when they are no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-check-assistant)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API dispatcher](references/api.md)
- [Authentication, jobs, and word entitlements API](references/api-auth.md)
- [Tender interpretation and bid-document generation API](references/api-bid-workflow.md)
- [Bid compliance review API](references/api-compliance.md)
- [Bid duplicate/similarity API](references/api-duplicate.md)
- [Knowledge-base field guide](references/knowledge-fields.md)
- [Execution usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Chinese-language chat guidance, JSON task results, HTML or Word reports, short-lived download links, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local report paths, generated-document paths, progress summaries, compliance issue lists, duplicate-risk evidence, and account word-balance notices.]

## Skill Version(s):

3.1.0 (source: release evidence and bundled CLI constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
