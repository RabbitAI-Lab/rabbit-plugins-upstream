## Description: <br>
Install, repair, or customize this OpenClaw cyberpunk chat and dream theme. Use when the user wants this exact theme, needs compatibility restored after an OpenClaw update, wants to import it into another workspace, or wants to swap the bundled avatars and background images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kasanuowa](https://clawhub.ai/user/kasanuowa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to install, repair, or customize a cyberpunk chat and dream theme, including replacing seven visual asset slots and restoring compatibility after OpenClaw UI updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer persistently patches the live OpenClaw Control UI. <br>
Mitigation: Review the target workspace and Control UI directory before applying, use --skip-apply when you only want files copied first, and keep generated backups for rollback. <br>
Risk: The theme runs UI JavaScript inside OpenClaw. <br>
Mitigation: Install only in a trusted workspace and inspect the bundled CSS and JavaScript before enabling the theme. <br>
Risk: Custom or fallback visual assets may affect the user interface unexpectedly. <br>
Mitigation: Use trusted asset files, keep the documented slot mapping, and rely on the bundled hash checks for downloaded default assets. <br>


## Reference(s): <br>
- [Theme Slots](references/theme-slots.md) <br>
- [Theme Configuration Example](references/theme-config.example.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/kasanuowa/skills/cyberpunk-theme) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may lead the agent to copy theme files, generate an apply script, and patch the live OpenClaw Control UI when the installer is run.] <br>

## Skill Version(s): <br>
1.0.22 (source: release evidence and artifact changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
