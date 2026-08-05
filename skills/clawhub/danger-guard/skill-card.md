## Description: <br>
Danger Guard intercepts dangerous agent commands before execution, requires password verification, and sends alerts for suspected compromised-account activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaszhou22](https://clawhub.ai/user/thomaszhou22) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI-agent users use Danger Guard to add command-safety rules, confirmations, alerts, and optional shell or git safeguards around destructive operations such as filesystem deletion, force pushes, Docker pruning, and unsafe SQL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Danger Guard asks for administrator-password-derived hashes as part of its dangerous-command verification flow. <br>
Mitigation: Review carefully before installing and do not provide sudo or administrator passwords to agent-managed prompts unless the exact flow and storage location have been reviewed. <br>
Risk: Danger Guard installs persistent behavior changes across agent and shell environments. <br>
Mitigation: Review the exact MEMORY.md, AGENTS.md, shell alias, and git hook changes before enabling them, and keep removal steps available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thomaszhou22/skills/danger-guard) <br>
- [README.md](README.md) <br>
- [INSTALL.md](INSTALL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown instructions with JSON, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write or append agent safety instructions, shell aliases, git hooks, and password-hash configuration during setup.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
