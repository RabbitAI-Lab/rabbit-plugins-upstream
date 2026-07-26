## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical SkillScan-style workflows for bug fixing, setup hardening, reliability improvement, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn security, SkillScan, bug-fix, setup-hardening, reliability, or related productivity requests into concise plans, checklists, implementation support, and validation notes. It is intended for practical workflow assistance rather than running scanners or deploying services itself. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad implicit triggers may cause the skill to activate for ordinary security or productivity requests where a SkillScan-style workflow is not needed. <br>
Mitigation: Prefer explicit invocation or narrow trigger terms before deployment, and confirm the user's intended workflow scope at the start of use. <br>
Risk: Workflow suggestions could produce incomplete or misleading hardening, reliability, or skill-development guidance if the user's constraints are underspecified. <br>
Mitigation: State assumptions, success criteria, validation steps, and remaining risks in the output; review security-sensitive recommendations before applying them. <br>


## Reference(s): <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper-035207) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/kyro-ma) <br>
- [SkillScan Demand Signal](https://clawhub.ai/skills/skillscan) <br>
- [Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter) <br>
- [Ask HN: Line by Line Agentic Coding](https://news.ycombinator.com/item?id=48754327) <br>
- [End Every Work Session with One Note](https://news.ycombinator.com/item?id=48743102) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, often with checklists, plans, validation notes, and optional code or shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's stated outcome and should include assumptions, limits, success criteria, and remaining risks when useful.] <br>

## Skill Version(s): <br>
0.20260702.35207 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
