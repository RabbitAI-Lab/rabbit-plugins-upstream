## Description: <br>
Skill创作发明家 helps agents create, optimize, audit, and prepare AI agent skills using an 8-stage workflow and a 53-item quality model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[muippt](https://clawhub.ai/user/muippt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to draft new agent skills, improve existing SKILL.md content, audit quality gates, optimize trigger wording, and prepare release materials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Skill-related requests may activate this workflow broadly. <br>
Mitigation: Review whether the request is actually about creating, optimizing, auditing, or preparing an agent skill before following the workflow. <br>
Risk: The audit script can scan multiple local skill directories when no target is supplied. <br>
Mitigation: Pass explicit skill names or set the skill base deliberately when you only want a focused audit. <br>
Risk: Generated or edited skill instructions can affect future agent behavior. <br>
Mitigation: Run the included audit checks and manually review generated SKILL.md, reference files, and release materials before publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-skill-creator) <br>
- [Quality gates reference](references/quality-gates.md) <br>
- [Publish workflow reference](references/publish-workflow.md) <br>
- [Collaboration guide](references/collaboration-guide.md) <br>
- [Landing page](https://muippt.github.io/mu-skill-creator/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, skill files, reference documents, and audit output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a local Bash audit script that can scan one or more skill directories.] <br>

## Skill Version(s): <br>
3.7.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
