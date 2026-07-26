## Description: <br>
投标文件智能生成 is a bid-document assistant that uses the 百炼®标书 open API to interpret tender files, generate editable .docx bid documents, and review draft bids for compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid teams and external users use this skill to upload local tender documents, understand bidding requirements, generate editable bid files, and review completed bid drafts before submission. It requires a 百炼®标书 App Key and uses the named cloud service to process selected documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service for processing. <br>
Mitigation: Confirm user consent before upload and use only the documented service domain for processing. <br>
Risk: The App Key is a full account credential and bid generation consumes account credits. <br>
Mitigation: Keep the App Key out of chat, store it only in the local config file, and check the account balance before paid generation. <br>
Risk: Generated bid content and compliance findings can be incomplete or require business judgment before submission. <br>
Mitigation: Review generated documents and findings before relying on them for a real bid. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-bid-gen) <br>
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [百炼®标书 open API contract](references/api.md) <br>
- [Execution and usage guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [User-facing text with generated .docx bid documents and HTML or Word reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include tender interpretation, bid-document files, compliance findings, report file paths, progress updates, and account-credit status.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
