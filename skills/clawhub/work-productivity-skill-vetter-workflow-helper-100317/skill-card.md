## Description: <br>
Helps agent users, skill authors, maintainers, and teams create Skill Vetter-style workflows for bug fixing, setup hardening, safety improvements, reliability checks, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent users, skill authors, maintainers, and teams use this skill to turn Skill Vetter-style demand into practical workflows, checklists, implementation plans, or decision support. It is intended for local-hardware-friendly work on bug fixing, setup hardening, safety, reliability, and adjacent skill creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms such as security, GitHub, and bug fix may cause the skill to activate for unrelated requests. <br>
Mitigation: Prefer explicit invocation or narrow the trigger wording before relying on implicit activation. <br>
Risk: The skill produces workflow guidance that may be incomplete or mismatched to a user's repository, toolchain, or security posture. <br>
Mitigation: Review generated plans and checklists against the user's stated constraints and validate the result before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper-100317) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub skill demand: SkillScan](https://clawhub.ai/skills/skillscan) <br>
- [Hacker News demand signal: DGX Spark inference server](https://news.ycombinator.com/item?id=49014048) <br>
- [Hacker News demand signal: AI-orchestrated publishing workflow](https://news.ycombinator.com/item?id=49009663) <br>
- [Hacker News demand signal: agent negotiation games](https://news.ycombinator.com/item?id=49019165) <br>
- [GitHub issue demand signal: kana-dojo](https://github.com/lingdojo/kana-dojo/issues/25825) <br>
- [GitHub issue demand signal: WivWav](https://github.com/NoAccountNeeded-Lab/WivWav/issues/913) <br>
- [GitHub issue demand signal: my-agentic-workflows](https://github.com/lfarci/my-agentic-workflows/issues/7) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or structured text, with code, shell commands, or configuration snippets when useful] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tailored artifacts, reusable checklists or workflows, and validation notes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
