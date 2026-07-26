## Description: <br>
Cold-start unpacker for vague boss or business requirements that helps product managers produce confirmation questions, scenario narrowing, scope skeletons, readiness scores, risk flags, and stakeholder reply scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chris1wang3](https://clawhub.ai/user/chris1wang3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers and product operators use this skill when a stakeholder gives only a vague direction, chat excerpt, meeting-note sentence, or oral request. It turns incomplete input into a PM alignment pack with prioritized questions, conservative assumptions, delivery level, MoSCoW scope, flow/state outline, readiness score, risk flags, and reply language. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for broad Chinese-language requirement-unpacking requests. <br>
Mitigation: Confirm the user's intent, delivery level, and output format before collecting more details or generating the full alignment pack. <br>
Risk: Users may enter confidential business requirements into the intake flow. <br>
Mitigation: Use the skill only in trusted host environments and avoid highly confidential details unless the organization has approved that environment. <br>
Risk: The output can be mistaken for a final PRD or delivery commitment. <br>
Mitigation: Keep unknown facts marked as pending confirmation and review the alignment pack before sharing it as scope, schedule, or engineering guidance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chris1wang3/skills/vague-requirement-unpacker) <br>
- [Source Homepage](https://github.com/Chris1Wang3/HammerRoom-Skills/tree/master/vague-requirement-unpacker) <br>
- [Support Issues](https://github.com/Chris1Wang3/HammerRoom-Skills/issues) <br>
- [Unpacking Playbook](references/unpacking-playbook.md) <br>
- [Scoring Engine](references/scoring-engine-deterministic.md) <br>
- [User Templates](references/user_templates.md) <br>
- [HTML Report Template](references/report-template-pro.html) <br>
- [Intake Form](assets/intake-form.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown or HTML alignment report, with optional structured intake JSON and stakeholder reply scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires confirmed output format before generating a full pack; HTML output uses the bundled report template.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release and claw.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
