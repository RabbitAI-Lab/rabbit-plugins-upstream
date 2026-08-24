## Description:

A Simplified Chinese bidding assistant that uses a user-supplied App Key to upload tender and bid documents to the 百炼®标书 service for tender interpretation, bid document generation, compliance review, and similarity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and their agents use this skill when a user provides local tender or bid files and asks for tender interpretation, editable bid document generation, compliance review, or multi-file similarity checks. The workflow is tailored to mainland-China procurement terminology and produces Chinese report artifacts.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, and personal information and are uploaded to a third-party service.

Mitigation: Use the skill only after the user understands and accepts the upload and retention behavior for the 百炼®标书 service.

Risk: The App Key authorizes the user's account and billing balance.

Mitigation: Keep the App Key in the local config.json file, do not paste it into chat, and rotate it on the service if exposure is suspected.

Risk: Endpoint overrides can direct uploaded files and credentials away from the official service.

Mitigation: Use the official biaoshu.zhiliaobiaoxun.com endpoint unless the user intentionally controls and trusts the override target.

Risk: Rapid status polling may hit service rate limits.

Mitigation: Use slower polling or backoff when progress checks return rate-limit responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-guard)
- [Usage guide](artifact/references/usage.md)
- [Open API contract reference](artifact/references/api.md)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown and text responses plus generated HTML, Word, and .docx files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated report labels and procurement terminology remain primarily Simplified Chinese.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
