## Description: <br>
Evaluate Claude skill quality through auditing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to audit Claude skills for structure, quality, token efficiency, trigger behavior, tool integration, and improvement opportunities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Under-scoped active tool-execution and benchmarking examples may encourage running discovered tools in an unsafe context. <br>
Mitigation: Use the skill only in trusted development workspaces, and skip or sandbox active tool-execution and benchmarking examples before applying them. <br>
Risk: Broad triggers may activate the skill outside explicit audit tasks. <br>
Mitigation: Narrow activation triggers so the skill is invoked only for clear skill-audit, evaluation, or improvement requests. <br>
Risk: Third-party tool declarations or untrusted skills may carry installation or execution risk. <br>
Mitigation: Review the skill before installation and scan untrusted skill artifacts before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skills-eval) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline command examples, checklists, rubrics, and report outlines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces audit and improvement guidance for skill quality, performance, trigger isolation, integration testing, pressure testing, and troubleshooting.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
