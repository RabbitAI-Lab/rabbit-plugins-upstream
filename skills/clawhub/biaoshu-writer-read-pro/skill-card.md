## Description:

Uploads tender and bid documents to the 百炼®标书 service so an agent can interpret tender requirements, generate .docx bid documents, review bid compliance, and compare 2-3 bid files for similarity risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement and bid-preparation users can use this skill to analyze tender files, create bid-document drafts, review bid risks, and run similarity checks before submission. It is intended for workflows where users can provide local tender or bid files, configure their own 百炼®标书 API key, and accept cloud processing and account-based billing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential tender and bid documents are uploaded to the 百炼®标书 service for processing and retained under the user's account for about 7 days.

Mitigation: Use the skill only after confirming the user is comfortable with that cloud processing and retention; avoid uploading documents the user is not authorized to process.

Risk: The skill depends on an API key and the security summary flags account credentials as a review concern.

Mitigation: Have the user configure the API key directly in the local config file; do not ask for, echo, or store API keys, SMS codes, phone numbers, or credential-bearing links in chat.

Risk: Local output paths and cached project records may expose sensitive procurement filenames.

Mitigation: Keep outputs in a dedicated project or output folder and review or clear ~/.zcm/projects.json when filenames are sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read-pro)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API overview](references/api.md)
- [Authentication, jobs, and billing](references/api-auth.md)
- [Interpretation and bid-document workflow API](references/api-bid-workflow.md)
- [Bid compliance review API](references/api-compliance.md)
- [Bid similarity check API](references/api-duplicate.md)
- [Execution guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Agent-facing instructions plus generated JSON summaries, HTML or Word reports, short-lived download links, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include locally written reports under biaoshu-bailian-files/ and cloud-hosted results that expire after about 7 days.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
