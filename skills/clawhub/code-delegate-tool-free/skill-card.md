## Description: <br>
Delegates programming tasks to a local code CLI with asynchronous workflows and single-task debugging iteration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to delegate coding, debugging, and test-verification tasks to a local code CLI while keeping the primary agent responsive. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delegated CLI runs can automatically edit local files. <br>
Mitigation: Run only in isolated project directories, confirm delegated commands before execution, and avoid automatic permission bypass. <br>
Risk: Project context may be processed by an external LLM through the delegated code CLI. <br>
Mitigation: Do not use on sensitive repositories unless external LLM processing is approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-delegate-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-shaped status examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Delegated runs may execute local CLI commands, edit project files, and send project context to an external LLM.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
