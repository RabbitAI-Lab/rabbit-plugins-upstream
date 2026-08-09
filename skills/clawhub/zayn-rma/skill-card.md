## Description: <br>
面向硬件、设备、备件和二手产品，依据型号、序列号、测试、保修、供应商窗口、退运和清关条件判断是否接受 RMA，并明确运费、时限和退回检测路径；一般产品退换、服务重做或退款补救使用 zayn-general-rma。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer support, aftersales, and operations teams use this skill to decide whether an RMA should be accepted, what evidence is missing, how return shipping and customs constraints should be handled, and what inspection path applies after receipt. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Operators may treat the skill's RMA recommendation as authority to grant refunds, replacements, legal positions, or management decisions. <br>
Mitigation: Use the output as decision support and require approval from authorized personnel before making customer commitments. <br>
Risk: The skill is a Chinese-language workflow and may be misunderstood by teams that cannot review the criteria precisely. <br>
Mitigation: Deploy it only where reviewers can understand the Chinese-language policy text or provide an approved translation before operational use. <br>
Risk: Incomplete or conflicting serial number, warranty, evidence, return shipping, customs, or supplier-window information can lead to unsupported RMA conclusions. <br>
Mitigation: Require the skill's minimum operating conditions before formal analysis, and keep incomplete, conflicting, or unverified information clearly marked as preliminary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-rma) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [examples.md](examples.md) <br>
- [tests.md](tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Structured Markdown with parameter status, RMA decision, required evidence, return requirements, freight boundaries, inspection path, deadlines, and customer-facing wording.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Decision-support output only; it must not authorize refunds, replacements, legal positions, or management decisions by itself.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact documents current rule version as v0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
