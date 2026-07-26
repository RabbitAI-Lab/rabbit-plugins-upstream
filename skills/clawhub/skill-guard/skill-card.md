## Description: <br>
Scan ClawHub skills for security vulnerabilities before installing them, using mcp-scan pre-flight checks to detect prompt injections, malware payloads, hardcoded secrets, and related threats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jamesouttake](https://clawhub.ai/user/jamesouttake) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users can use this skill when installing ClawHub skills to stage the target skill, scan it before installation, and block or quarantine it when issues are detected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan verdict is suspicious because the install script can stage, delete, move, and install skill directories. <br>
Mitigation: Review the script before running it, use normal ClawHub skill slugs, and avoid --force unless overwriting an existing skill is intended. <br>
Risk: The script exposes a --skip-scan option and depends on locally available command-line tools. <br>
Mitigation: Do not use --skip-scan for untrusted skills, and install dependencies such as clawhub and uv through verified package-manager sources where possible. <br>


## Reference(s): <br>
- [skill-guard on ClawHub](https://clawhub.ai/jamesouttake/skills/skill-guard) <br>
- [mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown instructions with shell commands and terminal status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Installs clean staged skills, leaves flagged skills quarantined for review, and returns exit codes for clean, error, or threat-detected outcomes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
