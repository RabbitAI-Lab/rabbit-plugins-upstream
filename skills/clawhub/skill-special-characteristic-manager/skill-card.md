## Description: <br>
从用户投喂的杂散材料（图纸图片/客户规范/邮件/Excel清单/口头）中抽取并识别产品与过程的特殊特性（CC/SC），判定级别、翻译客户符号、生成纯文字特性清单与传递矩阵，并标注材料缺口。面向 APQP 特殊特性清单编制、接单评审、审核应对。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality engineers, design engineers, and APQP teams use this skill to identify critical and significant product or process characteristics from unstructured drawings, customer specifications, emails, Excel/FMEA lists, and verbal notes. It supports APQP special-characteristic list preparation, order review, audit response, symbol translation, and material-gap tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process confidential customer drawings, specifications, FMEA sheets, and emails supplied by the user. <br>
Mitigation: Use it only with materials the user is authorized to share in the agent environment. <br>
Risk: Referenced rules or report-rendering files may be absent from the release artifact, which can limit functionality. <br>
Mitigation: Verify the required supporting files are supplied elsewhere before relying on the generated report workflow. <br>
Risk: The generated characteristic classification is a recommendation and may affect APQP, audit, or customer-review work if accepted without review. <br>
Mitigation: Require responsible enterprise reviewers to confirm final CC/SC classifications, symbol mappings, and unresolved material gaps. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-special-characteristic-manager) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-special-characteristic-manager) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Pure-text Markdown report with characteristic lists, symbol mappings, transmission matrix, control suggestions, and material gaps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation of the report outline before the final report; final special-characteristic decisions require enterprise review.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
