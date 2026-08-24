## Description:

This skill helps agents generate mainland-China business bid documents with the 百炼®标书 API, and also supports tender interpretation and compliance review when users provide local tender or bid files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to interpret Chinese tender documents, generate editable business bid documents, and review bid files for compliance risks before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain confidential business, pricing, or personal information and are uploaded to 百炼®标书 for processing.

Mitigation: Confirm user consent before upload, use only documents approved for third-party processing, and remind users that uploaded files and results are retained by the service for a limited period.

Risk: The security scan reports that the API endpoint can be redirected in code despite the skill's official-service positioning.

Mitigation: Before processing sensitive files, verify that ZCM_BASE and any configured base URL are unset or point only to https://biaoshu.zhiliaobiaoxun.com/.

Risk: Generated bid documents and compliance findings may be incomplete or incorrect for a specific tender.

Mitigation: Require human review of generated documents, unresolved template fields, compliance findings, and final submission materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-business)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance, files]

**Output Format:** [Agent-facing guidance plus generated .docx bid documents and HTML or Word reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local user-provided tender or bid files, a locally stored App Key, and a third-party API workflow; bid generation can consume account points.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
