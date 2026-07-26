## Description: <br>
Checks whether a local system and Python environment are ready for AI/ML and RAG development, including tools, packages, workspace structure, and configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Tilannlou](https://clawhub.ai/user/Tilannlou) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers use this skill to audit an AI/ML or RAG development environment, identify missing system tools or Python packages, and receive environment-readiness reports or installation-oriented guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package is presented mainly as an environment checker but also includes code running, arbitrary local command execution, possible elevation paths, and package installation behavior. <br>
Mitigation: Install only when the full development-skills bundle is intended; review or disable code-runner, permission-manager, universal-command, Docker, Ollama, and elevated-command paths before use. <br>
Risk: Package installation and generated code execution can alter the local environment or run untrusted code. <br>
Mitigation: Use a virtual environment or sandbox and require explicit human approval for every package install, generated-code run, Docker or Ollama action, and sudo or administrator path. <br>
Risk: The bundle can store, modify, or delete local knowledge files through the included RAG management behavior. <br>
Mitigation: Limit filesystem access to a dedicated workspace and review file write or delete actions before execution. <br>


## Reference(s): <br>
- [CHECK ClawHub page](https://clawhub.ai/Tilannlou/check) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON reports with Markdown guidance, code snippets, and shell-command proposals] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose package installation, generated code execution, local file operations, or command execution depending on which bundled skill behavior is invoked.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
