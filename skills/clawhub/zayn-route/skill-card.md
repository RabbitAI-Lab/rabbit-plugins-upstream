## Description: <br>
分析复杂职场问题，判断应先使用哪个 Skill，并规划调用顺序、参数传递、停止条件和最终输出 Skill。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and workplace agents use this skill to decide whether a complex Chinese-language workplace request needs one skill or a short sequence of skills, with explicit parameter handoff and stopping conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill could over-route a simple workplace request into an unnecessary chain. <br>
Mitigation: Apply the documented single-skill-first rule and keep recommended chains to no more than five skills unless the evidence clearly supports more. <br>
Risk: The skill could continue routing when key facts are missing or disputed. <br>
Mitigation: Stop when required parameters are missing, preserve conflicts and unverified facts, and state what information is needed before continuing. <br>
Risk: The skill is primarily documented for Chinese-language workplace routing, which may reduce reviewer clarity in bilingual or English-only environments. <br>
Mitigation: Review the release with Chinese-language competence or request bilingual documentation before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-route) <br>
- [Publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown routing analysis with tables and concise next-step guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs identify parameter completeness, candidate skill sequence, handoff fields, stopping conditions, current next action, and final output skill.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
