## Description:

This skill helps agents interpret mainland-China tender documents, generate bid documents, and review bid files for compliance through the BaiLian tender API after user consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents working on mainland-China bidding workflows use this skill to analyze tender documents, produce editable bid document files, and review one or more bid files for compliance risks. It is most useful when the user has supplied local tender or bid files and has configured their own BaiLian App Key.

### Deployment Geography for Use:

Mainland China bidding workflows

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the BaiLian cloud API for processing.

Mitigation: Confirm user consent before uploads and use the skill only with files the user explicitly provides.

Risk: The App Key is a full account credential for BaiLian operations.

Mitigation: Keep the App Key out of chat and store it only in the local skill config file as described by the release evidence.

Risk: Endpoint override settings can redirect processing away from the disclosed BaiLian service.

Mitigation: Leave endpoint overrides unset unless the user intentionally trusts the target service.

Risk: Generated bid documents and compliance reports can affect bidding decisions and may include incomplete or incorrect findings.

Mitigation: Review generated documents and risk findings before submission, especially high-risk, partial, or semantic-review results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-tender-reader)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [BaiLian tender platform](https://biaoshu.zhiliaobiaoxun.com/)
- [BaiLian open API reference](references/api.md)
- [Usage and operational guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus generated report files, Word documents, JSON summaries, and local file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs and report headings are primarily Simplified Chinese for mainland-China procurement workflows.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
