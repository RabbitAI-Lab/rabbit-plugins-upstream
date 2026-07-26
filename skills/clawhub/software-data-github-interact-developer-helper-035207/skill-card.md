## Description: <br>
Helps agent users, skill authors, maintainers, and teams handle GitHub-style software workflows on ClawHub, including bug fixing, setup hardening, reliability improvements, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent users, skill authors, maintainers, and teams use this skill to turn GitHub-style workflow requests into concrete artifacts such as implementation plans, code changes, checklists, analyses, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad activation phrases and may be invoked for general software or GitHub-adjacent requests outside the user's intent. <br>
Mitigation: Review the activation phrases before installation and disable implicit invocation when tighter control is required. <br>
Risk: Workflow guidance, code changes, or configuration advice could be incorrect or incomplete for a specific repository. <br>
Mitigation: Review proposed changes and run the included verification or test commands before applying results in a production workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/software-data-github-interact-developer-helper-035207) <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [English Skill Instructions](artifact/SKILL.md) <br>
- [Popular ClawHub Skill Demand: Github](https://clawhub.ai/skills/github) <br>
- [Ask HN: Which GitHub features are needed in a code forge before you can migrate?](https://news.ycombinator.com/item?id=48744529) <br>
- [3 dangers of being locked into a harness. Your context layer is true freedom](https://news.ycombinator.com/item?id=48745664) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown prose with code blocks, checklists, workflow steps, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tailored artifacts, reusable workflows, assumptions, limits, risks, and follow-up notes.] <br>

## Skill Version(s): <br>
0.20260702.35207 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
