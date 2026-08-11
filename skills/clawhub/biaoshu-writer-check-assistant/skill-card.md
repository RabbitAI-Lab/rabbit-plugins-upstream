## Description:

Checks tender and bid documents through the Bailian Biaoshu API, producing tender interpretations, bid-document drafts, compliance reports, and risk findings after user consent to upload files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, proposal, and bid teams use this skill to interpret tender files, generate bid-document drafts, and run pre-submission compliance checks on local tender and bid documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user consent before upload, process only user-selected local files, and install only when this third-party processing is acceptable.

Risk: The App Key is a credential for the user's Bailian Biaoshu account.

Mitigation: Keep the App Key out of chat, store it only in the local config file with restricted permissions, and reset it through the service if exposure is suspected.

Risk: Full bid-document generation consumes credits from the App Key account.

Mitigation: Confirm credit use before generating a full bid document and review account balance or billing expectations first.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-check-assistant)
- [Bailian Biaoshu platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage reference](references/usage.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with background shell commands and local HTML, Word, and DOCX artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents consume the App Key account's credits; uploaded files and generated results are processed by the third-party service.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
