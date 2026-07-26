## Description: <br>
Code Workflow guides agents through a staged code-change process covering research, planning, user review, test-driven implementation, and optional pull request evidence capture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering agents use this skill to structure non-trivial code changes, preserve research and plan artifacts, require explicit review before implementation, and apply TDD-oriented implementation and verification steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A hook resource is described as advisory but can block execution when undecided plan markers are detected. <br>
Mitigation: Review the hook behavior before enabling it, and either make the hook warning-only or document and accept its blocking behavior. <br>
Risk: Broad plan and research search rules can read unrelated local planning documents into the agent context. <br>
Mitigation: Limit searches to task-relevant issue numbers, explicit domain keywords, and configured project plan directories. <br>
Risk: Strict workflow gates can slow or interrupt small changes when applied too broadly. <br>
Mitigation: Use the skill for moderate or complex code changes, and rely on the documented trivial-task exception for simple one- or two-line edits. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/code-workflow) <br>
- [Skill manifest](SKILL.md) <br>
- [Workflow steps](steps.md) <br>
- [Implementation guidance](implement.md) <br>
- [PR workflow](pr.md) <br>
- [Release changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command snippets, workflow checklists, and file-oriented instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation of research and plan Markdown files, test code, Git commands, and pull request evidence when explicitly requested.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata and CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
