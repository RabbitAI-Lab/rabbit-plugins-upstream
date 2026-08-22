## Description:

标书合规性审查 helps agents use the 百炼®标书 API to interpret Chinese tender documents, generate bid documents, and review bid files for compliance risks after the user provides local files and an App Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement or bid teams use this skill for mainland-China bidding workflows: tender interpretation, bid document generation, and compliance review of one or more bid files. It is most useful when users provide local tender and bid files and need risk findings, supporting evidence, recommendations, and exportable reports.

### Deployment Geography for Use:

Mainland China bidding workflows

## Known Risks and Mitigations:

Risk: Tender and bid files may contain business, pricing, and personal data and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user consent before upload, send only the files needed for the task, and make the third-party processing boundary clear before first use.

Risk: The App Key is an account credential stored locally and could allow account use if exposed.

Mitigation: Keep the App Key in the local config file, do not paste it into chats or logs, preserve restrictive file permissions, and reset the key if exposure is suspected.

Risk: Bid document generation can consume account credits.

Mitigation: Check user intent and available balance before generation, and distinguish the balance gate from actual credit consumption.

Risk: Compliance findings and generated bid content may require professional review before procurement submission.

Mitigation: Treat generated reports and suggestions as review aids, prioritize high-risk findings, and have qualified staff verify final bid materials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-audit)
- [百炼®标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API Contract Reference](references/api.md)
- [Usage and Operations Guide](references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Files, Configuration instructions]

**Output Format:** [Text summaries with optional HTML reports, Word .docx reports, and generated bid .docx files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts and platform labels are primarily Simplified Chinese; use requires user-provided local files and an App Key.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
