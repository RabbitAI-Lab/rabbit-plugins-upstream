## Description:

This skill helps users upload tender and bid documents to the 百炼 service for AI-assisted tender interpretation, bid-document generation, compliance review, and duplicate-risk checking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement teams use this skill to analyze tender requirements, generate technical bid documents, review bid compliance risks, and compare bid files for similarity or duplicate-risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive procurement documents are uploaded to the 百炼 service for processing.

Mitigation: Use only with documents the user is authorized to process, disclose the upload before first use, and avoid installing if cloud processing of tender or bid documents is unacceptable.

Risk: The workflow relies on a billable API key and references phone-number registration.

Mitigation: Have the user register and configure the API key locally; do not ask users to paste phone numbers, SMS codes, API keys, or credential-bearing links into chat.

Risk: The skill writes generated reports and bid documents to local paths.

Mitigation: Keep outputs in the default known directory unless a trusted custom path is required, and avoid untrusted custom report basenames or output paths.

Risk: The artifact includes response-control instructions that affect how the agent talks to users.

Mitigation: Review the skill before deployment and apply host, platform, and organization policies ahead of any embedded response-control text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-tech)
- [百炼 service website](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API dispatch](artifact/references/api.md)
- [Authentication, jobs, and billing API](artifact/references/api-auth.md)
- [Tender interpretation and bid generation API](artifact/references/api-bid-workflow.md)
- [Bid compliance review API](artifact/references/api-compliance.md)
- [Bid duplicate-risk API](artifact/references/api-duplicate.md)
- [Knowledge-base fields](artifact/references/knowledge-fields.md)
- [Usage guide](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance, JSON/API summaries, HTML reports, Word .docx files, and shell commands executed by the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some workflows upload user-provided files to the 百炼 service, generated bid-document links are short-lived, and billable workflows consume the user's account word balance.]

## Skill Version(s):

3.1.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
