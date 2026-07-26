## Description: <br>
Use when an approved spec or design needs to become a commit-ready implementation plan before any code is written. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[escoffier-labs](https://clawhub.ai/user/escoffier-labs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agentic coding workers use this skill to convert an already-approved spec or design into an executable implementation plan. The plan is intended to include file maps, task checklists, test code, shell commands, expected outputs, and commit steps so a fresh implementer can proceed without additional design decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording could activate the skill when the user intended a different kind of planning task. <br>
Mitigation: Confirm there is an approved spec or design and that the user wants a detailed implementation plan before applying the skill. <br>
Risk: The skill can direct an agent to create and commit a plan file in the repository. <br>
Mitigation: Review the generated plan file and commit command before execution, and avoid committing unless repository policy and user intent allow it. <br>
Risk: A plan may encode incorrect implementation details or misleading guidance if the underlying spec or code reading is incomplete. <br>
Mitigation: Require the agent to read the touched files, validate spec coverage, include expected test output, and scan for placeholders before handoff. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/escoffier-labs/recipe) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/escoffier-labs) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown implementation plan with inline code blocks, checklist items, commands, expected outputs, and file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to save the plan under docs/plans and commit it when used as written.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
