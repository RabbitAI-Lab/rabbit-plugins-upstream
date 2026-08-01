## Description: <br>
Helps agent users, skill authors, maintainers, and teams create SkillScan-style workflows for bug fixing, setup hardening, safety checks, reliability improvements, and adjacent skill planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, skill authors, maintainers, and agent users use this skill to turn security, reliability, bug-fix, and SkillScan-style workflow requests into actionable plans, checklists, code changes, or decision support. It is designed for practical local execution using scripts, templates, small-model workflows, or CPU-safe processes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may trigger the skill on ordinary security, bug-fix, or workflow requests in a multi-skill environment. <br>
Mitigation: Prefer explicit invocation or narrow the trigger terms before enabling the skill broadly. <br>
Risk: Generated plans, checklists, or code suggestions may be incorrect or incomplete for the user's environment. <br>
Mitigation: Review outputs against the stated success criteria and scan or test changes before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [Published ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper-080414) <br>
- [SkillScan Demand Signal](https://clawhub.ai/skills/skillscan) <br>
- [Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter) <br>
- [Self-Improving Agent Demand Signal](https://clawhub.ai/skills/self-improving-agent) <br>
- [Ask HN Workflow Demand Signal](https://news.ycombinator.com/item?id=48979474) <br>
- [Privacy-Safe Receipt Masking Issue](https://github.com/enocperez-spec/POS-Printer-Emulator-ESC-POS/issues/34) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, checklists, and concise verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce reusable workflows, templates, automation outlines, decision aids, or implementation support tailored to the user's request.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
