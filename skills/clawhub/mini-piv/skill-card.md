## Description: <br>
Lightweight PIV workflow - discovery-driven feature builder. No PRD needed. Asks quick questions, generates PRP, executes with validation loop. For small-to-medium features when you want to skip PRD ceremony. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smokealot420](https://clawhub.ai/user/smokealot420) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to turn a short feature conversation into a PRP, execute the implementation, validate the result, and debug gaps for small-to-medium code changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify code and automatically stage and commit repository changes. <br>
Mitigation: Run it from a clean working tree, review the generated PRP and full diff before the final step, and keep secrets or unrelated untracked files out of the repository while running it. <br>
Risk: Untrusted repositories or unclear feature inputs can lead to incorrect or unwanted implementation changes. <br>
Mitigation: Use trusted project inputs, answer discovery questions precisely, and review validation results before relying on generated changes. <br>


## Reference(s): <br>
- [FTW project homepage](https://github.com/SmokeAlot420/ftw) <br>
- [Codebase Analysis for Feature Planning](references/codebase-analysis.md) <br>
- [Create BASE PRP](references/generate-prp.md) <br>
- [Execute BASE PRP](references/execute-prp.md) <br>
- [PIV Executor Agent](references/piv-executor.md) <br>
- [PIV Validator Agent](references/piv-validator.md) <br>
- [PIV Debugger Agent](references/piv-debugger.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and repository file changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create PRP and planning Markdown files, modify code, run validation commands, and commit reviewed repository changes.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
