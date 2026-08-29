## Description:

This skill helps agents use the Bailian Biaoshu Open API to interpret tender files, generate technical bid documents, and review bid-document compliance after the user provides local files and an App Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding and proposal teams use this skill to analyze tender documents, generate editable technical bid documents, and review completed bid files for compliance risks. It is intended for workflows where users explicitly provide local tender or bid files and understand that files are processed by the Bailian Biaoshu service.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Use only after the user understands and accepts the upload, and avoid providing files that should not be processed by the third-party service.

Risk: The App Key authorizes actions under the user's Bailian Biaoshu account.

Mitigation: Keep the App Key out of chat and store it only in the local configuration file managed by the user.

Risk: Bid generation can consume account credits.

Mitigation: Confirm generation intent before creating bid documents and check account balance when appropriate.

Risk: Generated bid documents and compliance reports may influence formal tender submissions.

Mitigation: Have a qualified reviewer inspect generated files, compliance findings, and remaining placeholders before submission.

Risk: Uploaded results may remain available on the service for a limited time.

Mitigation: Retrieve needed outputs promptly and manage or remove account history through the service where available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-tech)
- [Skill Instructions](artifact/SKILL.md)
- [Usage Guide](artifact/references/usage.md)
- [API Contract Reference](artifact/references/api.md)
- [Knowledge Fields Reference](artifact/references/knowledge-fields.md)
- [Bailian Biaoshu Platform](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [Text, Guidance, Files, Configuration, Shell commands]

**Output Format:** [Agent guidance plus structured text summaries, generated .docx bid documents, and HTML or Word compliance and interpretation reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs use Simplified Chinese procurement labels where they mirror the upstream platform, and generated files are reported to the user by absolute path.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
