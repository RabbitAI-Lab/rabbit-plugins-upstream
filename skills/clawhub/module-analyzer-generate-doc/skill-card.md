## Description: <br>
Java/Maven single-module deep documentation generator that generates L3 file-level to L2 module-level business logic docs for a specified module with multi-subagent parallel processing, context compression, checkpoint resume, and auto-retry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endcy](https://clawhub.ai/user/endcy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to generate detailed L3 file-level and L2 module-level documentation for a single Java/Maven module, focused on business logic, workflows, dependencies, and design intent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated documentation may summarize source code or configuration details into local .ai-doc files. <br>
Mitigation: Review generated documentation for secrets and sensitive implementation details before sharing it. <br>
Risk: Package scripts or shell examples may be run in a local project during documentation workflows. <br>
Mitigation: Inspect scripts before running them and keep execution limited to reviewed documentation-generation steps. <br>


## Reference(s): <br>
- [Task Execution Guide](references/task-execution-guide.md) <br>
- [L3 File Template](references/l3-file-template.md) <br>
- [L2 Module Template](references/l2-module-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown documentation files and concise text progress reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes L3 file-level and L2 module-level docs under .ai-doc for a selected Java/Maven module; source code is not modified.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence and changelog, released 2026-07-16) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
