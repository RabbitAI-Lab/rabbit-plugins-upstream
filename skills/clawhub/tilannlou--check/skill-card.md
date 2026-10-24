## Description:

CHECK helps agents inspect AI/ML development environments, verify tools and Python packages, manage related development helper workflows, and install missing dependencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tilannlou](https://clawhub.ai/user/tilannlou)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use CHECK to assess local AI/ML and RAG development readiness, generate or test code snippets, organize RAG content, and troubleshoot package or command permission issues. Because it can execute commands, install packages, write files, and delete files, it is best used in controlled development environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary states that this skill gives agents broad host command execution, package installation, code execution, file mutation, and automatic privilege attempts without clear safety gates.

Mitigation: Install and run it only in a disposable or tightly sandboxed development environment with no sensitive files, credentials, Docker access, passwordless sudo, or shared Python environments.

Risk: The artifact can install Python packages and run generated or user-supplied code, which can change the local environment or execute untrusted behavior.

Mitigation: Review requested installs, generated code, tests, and command output before allowing execution; prefer isolated virtual environments or containers.

Risk: The artifact includes permission-management behavior that may retry commands with alternate strategies, including sudo on Linux or WSL.

Mitigation: Do not grant elevated privileges unless the command is explicitly reviewed and expected; avoid use on machines with administrative access to important systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tilannlou/skills/check)

## Skill Output:

**Output Type(s):** [text, JSON, code, shell commands, configuration, guidance]

**Output Format:** [JSON results and human-readable guidance, sometimes including generated code and shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include environment reports, command results, generated code, test results, dependency installation results, and permission recommendations.]

## Skill Version(s):

1.0.0 (source: release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
