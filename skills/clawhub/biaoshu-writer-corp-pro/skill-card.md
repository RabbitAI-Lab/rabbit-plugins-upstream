## Description:

A bid-document assistant that uses the BaiLian bid-document API to interpret tender files, generate editable bid drafts, format responses, and review bid submissions for disqualification and compliance risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External proposal and tender teams use this skill to analyze tender documents, draft bid files, and check bid submissions before filing. It is intended for users who provide local tender or bid files and accept that the files are processed by the BaiLian service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain confidential commercial, pricing, and personal information and are uploaded to the BaiLian service for processing.

Mitigation: Use the skill only after the user confirms they understand and accept the upload, server processing, and account-linked retention described by the release evidence.

Risk: The App Key is a full account credential stored locally in config.json.

Mitigation: Keep config.json private, never paste the App Key into chat, and use logout or delete the credential file when local credential retention is no longer desired.

Risk: Bid generation consumes account points and long-running generation jobs can continue after a local client timeout.

Mitigation: Confirm generation intent before submitting, monitor progress, and resume result retrieval by job identifier instead of resubmitting the same generation request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-corp-pro)
- [Usage manual](artifact/references/usage.md)
- [BaiLian bid API contract reference](artifact/references/api.md)
- [BaiLian bid-document service](https://biaoshu.zhiliaobiaoxun.com/)
- [BaiLian open API base](https://biaoshu.zhiliaobiaoxun.com/api/open/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated HTML reports and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include progress updates, result summaries, and absolute paths for generated reports or bid documents.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
