## Description: <br>
Code-workflow guides agents through a four-stage code-change process covering research, planning, user review, TDD implementation, and optional PR capture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to structure non-trivial code changes, create research and plan artifacts, gate implementation on explicit user review, run TDD-oriented verification, and prepare PRs with visual evidence when requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives agents broad code, Git, GitHub, and workflow-control authority. <br>
Mitigation: Set explicit approval rules before use for pushes, PR creation, issue comments, RAG dispatch, and hook installation. <br>
Risk: Approval and blocking behavior may be unclear in some workflows. <br>
Mitigation: Require explicit user confirmation before implementation, publishing actions, or workflow-control changes, and review generated plans before execution. <br>
Risk: The bundled hook script may have an exit-code mismatch. <br>
Mitigation: Review and fix the hook script behavior before installing or relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/code-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown research and plan files, code changes, shell commands, commit guidance, PR body text, and review summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create workspace-local research and plan files under llm-wiki/outputs/ and PR visual evidence when explicitly requested.] <br>

## Skill Version(s): <br>
0.5.1 (source: server release metadata and CHANGELOG; SKILL.md metadata lists 0.1.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
