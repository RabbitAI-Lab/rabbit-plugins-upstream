## Description: <br>
Run quantum_lab Python scripts and demos inside a configured Qiskit virtual environment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bramdo](https://clawhub.ai/user/bramdo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use Quantum Lab to run local quantum_lab scripts, demos, notebooks, and server commands from an existing Qiskit virtual environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local shell commands against a specific local repository and virtual environment. <br>
Mitigation: Review the exact command before execution and install only when the local quantum_lab repository and Qiskit virtual environment are trusted. <br>
Risk: Notebook execution and dependency installation can run code from local files or packages. <br>
Mitigation: Review notebooks and pip install commands before running them. <br>
Risk: Remote chat requests through Telegram or OpenClaw could trigger local command execution if trusted blindly. <br>
Mitigation: Do not let untrusted Telegram or OpenClaw requests trigger local commands. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands depend on a local quantum_lab repository and Qiskit virtual environment.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
