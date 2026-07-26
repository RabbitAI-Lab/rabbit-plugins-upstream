## Description: <br>
Guides agents through a mandatory design-first workflow that explores user intent, requirements, and design before implementation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivansslo](https://clawhub.ai/user/ivansslo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn feature or behavior-change ideas into approved designs and written specs before implementation. It supports collaborative planning in existing or new projects, including clarification, approach comparison, design approval, spec review, and handoff to implementation planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enforces a strict design-before-code workflow that can slow quick edits or exploratory work. <br>
Mitigation: Use it when a formal design gate is desired, and decline or override the workflow when a quick edit is more appropriate. <br>
Risk: The skill may create and commit a design specification in the repository. <br>
Mitigation: Review the proposed spec path and commit before proceeding, especially when repository changes are not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivansslo/skills/brainstorming-10) <br>
- [Server-resolved GitHub source](https://github.com/ivansslo/Supwrs/tree/main/skills/brainstorming) <br>
- [Publisher profile](https://clawhub.ai/user/ivansslo) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands] <br>
**Output Format:** [Conversational text and Markdown design specifications, with shell commands when repository inspection, spec creation, or git commits are needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user approval before implementation and before handoff to implementation planning.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
