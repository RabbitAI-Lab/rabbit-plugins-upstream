## Description: <br>
Use when a user wants to add single, batch, stdin, file, or interactive items to Bring! shopping lists with dry-run preview and JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darkdevelopers](https://clawhub.ai/user/darkdevelopers) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to add items to Bring! shopping lists from a command-line workflow, including single-item, batch, stdin/file, and interactive modes. It can preview planned changes and emit JSON for automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bring! credentials are required for the CLI and could be exposed through shell history, scripts, CI logs, or committed files. <br>
Mitigation: Treat BRING_EMAIL and BRING_PASSWORD as secrets, use a trusted local environment, and prefer a password manager or short-lived local setup. <br>
Risk: Items may be added to the wrong shopping list if the default or requested list is not checked. <br>
Mitigation: Use the lists command and --dry-run preview to confirm the target list before making changes. <br>
Risk: Dependency versions may change because package.json allows an unpinned Bring! client dependency. <br>
Mitigation: Review and pin dependencies when reproducible installs are required. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/darkdevelopers/skills/bring-add) <br>
- [README](README.md) <br>
- [Skill Definition](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18 or newer and Bring! account credentials provided through local environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
