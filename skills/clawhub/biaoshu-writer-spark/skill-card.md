## Description:

标书智能制作 helps agents analyze tender documents, generate editable bid documents, draft bid responses, and review bid files for disqualification and compliance risks through the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to analyze tender files, generate editable bid documents, and review submitted bid files for compliance, similarity, and disqualification risks. The skill should be used only when the user provides local tender or bid files and asks for interpretation, generation, or compliance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected tender and bid documents are uploaded to the 百炼®标书 cloud service and may contain commercial, pricing, or personal information.

Mitigation: Confirm the user understands and agrees to cloud processing before upload, and process only files the user explicitly provides for the requested task.

Risk: The skill stores an App Key locally in config.json, and that key controls access to the user's service account.

Mitigation: Keep the App Key out of chat, store it only in the local config.json file, use file permissions that restrict access, and delete the file or use logout when the credential is no longer needed.

Risk: Custom service endpoint or output-directory settings could redirect requests or place generated files somewhere unexpected.

Mitigation: Review any ZCM_BASE, ZCM_HOME, or ZCM_OUTPUT_DIR settings before use and prefer the default service endpoint and output location unless the user intentionally overrides them.

Risk: Generated bid documents and compliance findings may be incomplete or unsuitable for final submission without review.

Mitigation: Have qualified bid staff review generated documents, compliance findings, evidence, and manual-check items before relying on them for submission decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-spark)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](artifact/references/api.md)
- [Usage reference](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Agent-facing Markdown guidance and command plans; user-facing outputs include analysis summaries, editable .docx bid documents, and HTML or Word reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied local tender or bid files and a locally stored App Key; selected documents are uploaded to the 百炼®标书 cloud service.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
