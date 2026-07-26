## Description: <br>
Manage Proton Pass vaults, items, passwords, SSH agent integration, and secret injection workflows through Proton Pass CLI guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kakatkarakshay](https://clawhub.ai/user/kakatkarakshay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and power users use this skill for Proton Pass CLI workflows, including vault and item management, SSH key handling, password generation, TOTP retrieval, and secret injection into commands or templates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill covers powerful password-manager actions, including viewing, sharing, deleting, transferring ownership, importing SSH keys, and injecting secrets into commands or files. <br>
Mitigation: Require explicit approval before high-impact or secret-revealing actions, keep secret masking enabled, and review generated commands before execution. <br>
Risk: Installer and key-storage choices can affect local security posture. <br>
Mitigation: Verify the installer source or use Homebrew/package-manager installation where practical, and avoid less-secure storage modes unless the environment requires them. <br>
Risk: Rendered or injected secrets can be written to files or exposed in process environments. <br>
Mitigation: Avoid writing secrets to broadly readable files, use restrictive file permissions, and prefer file-based secret inputs over plain-text environment values when available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kakatkarakshay/skills/proton-pass) <br>
- [Proton Pass CLI installer for macOS and Linux](https://proton.me/download/pass-cli/install.sh) <br>
- [Proton Pass CLI installer for Windows](https://proton.me/download/pass-cli/install.ps1) <br>
- [Proton Pass account security settings](https://account.proton.me/pass/security) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command examples that operate on sensitive vault, item, SSH key, and secret-injection workflows.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
