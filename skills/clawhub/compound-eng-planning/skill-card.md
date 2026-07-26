## Description: <br>
Software implementation planning with file-based persistence (.plan/) for code changes that touch multiple files, have ambiguous scope, or require architectural decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this workflow to turn implementation requests into concrete, verifiable plans before coding. It is aimed at multi-file changes, ambiguous scopes, and work that benefits from persistent session notes in `.plan/`. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Starting a new plan can overwrite existing `.plan` files in the current workspace. <br>
Mitigation: Review or preserve existing `.plan` files before initializing a new plan when those files contain work that must be kept. <br>


## Reference(s): <br>
- [ia-planning Specification](SPEC.md) <br>
- [Execution & Decomposition Patterns](references/execution-and-methodology.md) <br>
- [Operational Patterns](references/operational-patterns.md) <br>
- [Plan Deepening](references/plan-deepening.md) <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-planning) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown planning files and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local `.plan/` files and add `.plan/` to `.gitignore` when the initialization script is used.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
