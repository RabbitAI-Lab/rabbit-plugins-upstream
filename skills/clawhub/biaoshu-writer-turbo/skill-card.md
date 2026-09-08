## Description:

上传招标/投标文件后，该 skill 可调用百炼®标书云端服务完成招标解读、投标文件生成、标书审查和 2-3 份投标文件查重。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and business users use this skill to process authorized tender and bid documents, including tender interpretation, bid document generation, compliance review, and duplicate-risk review. It is intended for workflows where the user accepts cloud processing by the 百炼®标书 service under their own API-key account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Install and use only when users are authorized to process the files, accept cloud processing, and have reviewed the provider's retention and account controls.

Risk: The API key controls the user's 百炼®标书 account and can expose account access if pasted into chat or shared in links.

Mitigation: Keep the API key out of conversation logs and store it only in the local config file managed by the user.

Risk: Duplicate-risk and compliance outputs can be mistaken for legal determinations.

Mitigation: Treat outputs as internal review signals and require human or legal review before relying on them for bid submission decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-turbo)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract reference](artifact/references/api.md)
- [Execution guide](artifact/references/usage.md)
- [Knowledge fields reference](artifact/references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Chinese text summaries, JSON results, and generated HTML, Word, or DOCX files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents and reports may include local file paths or short-lived download links; outputs require user review before submission or business reliance.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
