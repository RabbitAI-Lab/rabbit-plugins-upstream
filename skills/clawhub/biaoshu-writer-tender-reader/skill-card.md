## Description:

招标文件智能解读 helps agents analyze user-provided tender documents through the 百炼标书 API, produce structured interpretation reports, generate editable bid documents, and review bid files for compliance risks after user consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to interpret tender documents, identify disqualification red lines, scoring criteria, key requirements, commercial terms, and control-risk signals. The same workflow can generate editable bid documents and compliance review reports for user-provided bid files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Install and use the skill only after confirming the user understands and accepts this cloud processing and account-level retention model.

Risk: The App Key controls the user account and can expose account access if pasted into chat or shared in parameterized links.

Mitigation: Keep the App Key in the local config file only, never echo it in conversation, and avoid forwarding links that contain credential parameters.

Risk: Generated bid documents and compliance findings may be incomplete or unsuitable for submission without domain review.

Mitigation: Require human review of generated bid documents, compliance issues, evidence, and any retained待填项 before procurement submission.

Risk: Bid document generation may consume account credits.

Mitigation: Check account balance and obtain user intent before starting generation workflows that can charge credits.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-tender-reader)
- [百炼标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API Contract Reference](references/api.md)
- [Usage Guide](references/usage.md)
- [Knowledge Base Field Guide](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Conversational guidance plus generated HTML, Word, DOCX, and JSON-backed report artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces structured tender interpretations, compliance summaries, editable bid documents, local report files, and progress/status messages.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
