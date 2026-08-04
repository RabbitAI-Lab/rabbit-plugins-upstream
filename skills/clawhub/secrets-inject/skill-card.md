## Description: <br>
HIGH-PRIVILEGE companion to secrets-manager that substitutes encrypted secrets into command strings and materializes them as executable shell scripts or prints them to stdout. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they must pass secrets from the secrets-manager store into shell commands. It is intended for deliberate, opt-in secret injection workflows where the user accepts plaintext exposure risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated temp scripts and stdout output can expose plaintext secrets. <br>
Mitigation: Install only for workflows that require shell command injection, avoid shared or CI hosts, and run --cleanup-tmp after use. <br>
Risk: Resolved commands may place secrets into logs, terminal scrollback, or shell history. <br>
Mitigation: Use stdout mode only with explicit confirmation and prefer file-based secret handling when the target command supports it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/secrets-inject) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, shell commands, code, configuration] <br>
**Output Format:** [CLI text output, generated shell script files, and resolved command strings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated temp scripts contain plaintext secrets, use chmod 0600, and require manual cleanup.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
