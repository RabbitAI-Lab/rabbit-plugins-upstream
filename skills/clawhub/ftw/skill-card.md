## Description: <br>
Piv orchestrates a Plan, Implement, Validate workflow for multi-phase software development, including discovery, PRD and PRP creation, codebase analysis, execution, validation, and debugging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smokealot420](https://clawhub.ai/user/smokealot420) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use Piv to structure feature work into discovery, planning, implementation, independent validation, and targeted debugging phases. It is intended for repository-based software projects where an agent may create planning documents, propose code changes, run validation commands, and prepare commits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can actively modify repositories, run project commands, and prepare commits. <br>
Mitigation: Run it only in the intended project, keep a clean git state or backup, and review generated documents, diffs, commands, and commits before accepting them. <br>
Risk: Discovery and planning output can contain incomplete or incorrect assumptions about project requirements. <br>
Mitigation: Review PRDs, PRPs, phase plans, and validation findings before implementation, especially when the skill fills gaps from its own expertise. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smokealot420/skills/ftw) <br>
- [Project homepage](https://github.com/SmokeAlot420/ftw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file paths, code-oriented plans, shell commands, validation summaries, and generated project documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update repository files such as PRDs, PRPs, workflow trackers, implementation changes, validation reports, and commits when used in a project.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
