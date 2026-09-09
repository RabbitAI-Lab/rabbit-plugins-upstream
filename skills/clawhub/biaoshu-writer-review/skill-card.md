## Description:

AI-assisted tender and bid workflow skill for interpreting tender files, generating bid documents, reviewing bid compliance, and checking similarity risks between bid files through the 百炼标书 cloud API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to upload tender and bid documents for tender interpretation, compliance review, bid document generation, and bid similarity checks. The skill is intended for Chinese-language procurement and bidding workflows that can use the 百炼标书 vendor service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, personal, or confidential information and are processed and retained by the vendor service.

Mitigation: Use only documents the user is authorized to upload, obtain explicit consent before upload, and review the vendor service's retention expectations before processing sensitive material.

Risk: API keys, phone numbers, and SMS codes could be exposed if users paste credentials or registration data into chat.

Mitigation: Do not ask users to paste API keys, SMS codes, or phone numbers into chat; users should manage credentials directly in the local configuration file and vendor website.

Risk: Server security evidence reports under-disclosed file writes and recommends avoiding outputs outside the intended directory until path containment is fixed.

Mitigation: Keep generated files inside the intended output directory and review any requested output path before allowing the skill to write there.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review)
- [百炼标书 Open API overview](references/api.md)
- [Authentication, tasks, and word entitlement API](references/api-auth.md)
- [Tender interpretation and bid document workflow API](references/api-bid-workflow.md)
- [Bid compliance review API](references/api-compliance.md)
- [Bid similarity check API](references/api-duplicate.md)
- [Knowledge base fields](references/knowledge-fields.md)
- [Usage and operating guidance](references/usage.md)
- [百炼标书 Open API base URL](https://biaoshu.zhiliaobiaoxun.com/api/open/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance and progress updates, structured JSON results, HTML or Word reports, and DOCX bid document outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local user-provided documents, vendor API tasks, short-lived download links, and an output directory for generated reports and documents.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
