## Description: <br>
AI 标书生成工具，使用 App Key 调用百炼标书开放 API，帮助解读招标文件、生成投标文件 .docx，并进行废标与合规审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business or procurement teams use this skill to analyze tender files, draft technical and commercial bid documents, and run pre-submission compliance checks through the 百炼标书 service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents can contain commercial, pricing, and personal information and are uploaded to the 百炼标书 service for processing. <br>
Mitigation: Confirm user consent before the first upload, send only user-provided local files, and make the service retention and account visibility expectations clear before use. <br>
Risk: The local App Key controls access to the user's account and paid generation credits. <br>
Mitigation: Have the user store the App Key locally, never ask them to paste it into chat, avoid forwarding key-bearing links, and advise reset or logout if exposure is suspected. <br>
Risk: Bid generation consumes account credits and long-running jobs can continue after the agent session changes. <br>
Mitigation: Check balance before paid generation, avoid duplicate submissions, track job identifiers, and report generated file paths and remaining balance when available. <br>
Risk: Generated bid documents and compliance findings may be incomplete or unsuitable for final submission without professional review. <br>
Mitigation: Require human review of generated documents, risk findings, and tender evidence before relying on them for procurement decisions or bid submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-ace) <br>
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage reference](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown and text summaries with generated HTML, Word, and .docx files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce bid interpretation reports, finished bid documents, compliance review reports, account setup guidance, and local file paths for generated artifacts.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
