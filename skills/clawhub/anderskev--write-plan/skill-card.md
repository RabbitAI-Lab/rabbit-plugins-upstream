## Description: <br>
Use when you have a finalized brainstorm-beagle spec at `.beagle/concepts/<slug>/spec.md` and need a bite-sized, TDD-driven implementation plan before any code is written. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anderskev](https://clawhub.ai/user/anderskev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn a finalized brainstorm-beagle specification into a concise, task-by-task TDD implementation plan before code is written. It is intended for planning implementation work, not for brainstorming specs or executing the implementation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads project specs and relevant repository files to draft a plan. <br>
Mitigation: Use it only with projects and specs the user is willing to expose to the agent session. <br>
Risk: A generated plan could contain incorrect or misleading implementation guidance. <br>
Mitigation: Review the draft, use the built-in self-review flow, and approve the plan before it is written. <br>
Risk: The skill writes a plan file after approval. <br>
Mitigation: Confirm the intended `.beagle/concepts/<slug>/plan.md` target before approving the write; the skill does not execute the implementation. <br>


## Reference(s): <br>
- [Write Plan on ClawHub](https://clawhub.ai/anderskev/skills/write-plan) <br>
- [Plan Document Reviewer Prompt Template](references/plan-reviewer.md) <br>
- [Plan Document Template](references/plan-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown plan document with inline code snippets and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes `.beagle/concepts/<slug>/plan.md` only after user approval and may provide an optional execution handoff prompt.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
