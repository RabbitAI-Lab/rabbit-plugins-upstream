## Description: <br>
Danger Guard intercepts dangerous commands before execution, requires sudo/admin verification, and sends alerts when destructive activity is attempted through a compromised account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaszhou22](https://clawhub.ai/user/thomaszhou22) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI-tool users use Danger Guard to add command safety rules, tool configuration, optional shell wrapping, and git hook protection around destructive operations. It is intended to reduce the chance that a compromised messaging or AI-agent account can trigger file deletion, disk formatting, unsafe git operations, destructive Docker commands, or risky SQL changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for a sudo/admin password and persist a password-derived SHA-256 verifier. <br>
Mitigation: Review the installation flow before use; prefer a version that avoids OS-password collection and uses native authorization. Remove any stored verifier during uninstall. <br>
Risk: The optional shell wrapper can modify shell startup files, install aliases/hooks, and change normal command behavior. <br>
Mitigation: Install shell-level protection only after reviewing the exact files and aliases it changes, keep uninstall steps available, and test in a non-critical environment first. <br>
Risk: Interception logs and alerts can include sensitive command details. <br>
Mitigation: Use clear log redaction and retention controls, restrict alert destinations, and avoid sending secrets or sensitive paths in incident notifications. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thomaszhou22/skills/danger-guard) <br>
- [README](artifact/README.md) <br>
- [Installation guide](artifact/INSTALL.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Claude Code configuration](artifact/configs/claude-code/settings.json) <br>
- [Codex agent instructions](artifact/configs/codex/AGENTS.md) <br>
- [Git pre-push hook](artifact/configs/git-hooks/pre-push) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown instructions with JSON configuration snippets, shell commands, and hook/configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent safety rules, deny-list configuration, shell-wrapper setup guidance, alerting guidance, and git hook guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
