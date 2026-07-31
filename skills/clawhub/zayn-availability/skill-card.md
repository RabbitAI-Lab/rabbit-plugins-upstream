## Description: <br>
区分现货、可调货、预计可供、待锁货和信息过期等货源状态，并给出可对外使用的库存表述。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, quotation, and inventory users use this Chinese-language skill to classify inventory availability, separate confirmed stock from tentative or stale information, and produce customer-facing availability wording. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tentative supplier feedback, historical supply, or expected arrival information could be overstated as confirmed stock. <br>
Mitigation: Use the required availability labels and disallowed-wording checks, and do not present unverified or historical information as a confirmed current fact. <br>
Risk: Incomplete, stale, or conflicting availability inputs could lead to misleading customer-facing wording. <br>
Mitigation: Require product model, source, update time, and current-versus-historical distinction before formal analysis; otherwise mark the result as preliminary or stop for missing information. <br>
Risk: Chinese-only documentation and output labels may not match every team's workflow. <br>
Mitigation: Confirm language expectations before deployment and review or translate labels for teams that need non-Chinese outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-availability) <br>
- [Skill rules](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Usage template](artifact/examples.md) <br>
- [Test requirements](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language output with parameter completeness, a parameter status table, current inventory status, evidence source, allowed and disallowed external wording, next confirmation actions, and information validity.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence; artifact documentation describes v0.1 draft rules) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
