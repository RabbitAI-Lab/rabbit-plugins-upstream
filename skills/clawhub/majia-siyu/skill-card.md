## Description: <br>
A Chinese-language private-domain marketing assistant that routes /siyu requests into copywriting, group messaging, welcome-script, customer-file, reporting, update, and operational diagnosis workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Marketing and operations teams use this skill to turn private-domain marketing questions into Chinese-language action plans, customer-facing copy, compliance checks, saved notes, and follow-up reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer or business notes may be saved as unencrypted local plaintext under ~/.siyu. <br>
Mitigation: Redact sensitive customer details before saving, restrict local filesystem access, and avoid storing regulated personal data in saved notes. <br>
Risk: The skill can update itself from the publisher's GitHub project when a user explicitly requests an update. <br>
Mitigation: Approve updates only when the source and version are expected, then rescan or review the updated skill before operational use. <br>
Risk: Generated private-domain marketing copy can affect customer communications and platform compliance. <br>
Mitigation: Review outputs before publishing and use the bundled compliance checks for redlines such as absolute claims, inducement mechanics, and unauthorized sensitive-data requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-siyu) <br>
- [新手教程](references/新手教程.md) <br>
- [整盘怎么搭-老板版](references/整盘怎么搭-老板版.md) <br>
- [朋友圈合规前置扫描](modules/siyu-pyq/references/合规前置扫描.md) <br>
- [群发合规前置扫描](modules/siyu-qunfa/references/合规前置扫描.md) <br>
- [话术合规前置扫描](modules/siyu-huashu/references/合规前置扫描.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Chinese-language Markdown and plain text, with occasional shell command snippets and local Markdown files for saved customer notes or reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include customer-facing marketing copy, compliance scan findings, operational diagnoses, local customer note files under ~/.siyu, and update commands only when explicitly requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
