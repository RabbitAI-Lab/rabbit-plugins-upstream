## Description: <br>
Dead Code Cleaner guides an agent through multi-stage dead code detection and cleanup using codebase-memory-mcp knowledge graphs, language-specific verification checks, build validation, and cleanup reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yexinjia](https://clawhub.ai/user/yexinjia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to identify unused source files, duplicate dead-code candidates, orphaned resources, and cascading dead code in single repositories or monorepos before removing them with validation evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can delete repository code and resources. <br>
Mitigation: Run it only in the intended repository from a clean committed or stashed state, then review the candidate deletion list, validation output, and final diff before accepting changes. <br>
Risk: Dead-code detection can miss dynamic, reflective, or cross-project references. <br>
Mitigation: Use the documented language-specific verification layers, cross-repository checks for monorepos, pre-delete build validation, and post-delete build or test validation before considering cleanup complete. <br>
Risk: The skill may configure codebase-memory-mcp and open a local visualization UI. <br>
Mitigation: Install and run it only in environments where codebase-memory-mcp is expected, and confirm local UI exposure is acceptable before enabling visualization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yexinjia/skills/dead-code-cleaner) <br>
- [Server-resolved GitHub provenance](https://github.com/yexinjia/dead-code-cleaner) <br>
- [Publisher profile](https://clawhub.ai/user/yexinjia) <br>
- [Output template](references/output-template.md) <br>
- [Verification patterns](references/verification-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown summary with shell commands, validation results, deletion and modification lists, and risk assessment] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May modify or delete repository files after validation; reports cleanup metrics and verification methods.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
