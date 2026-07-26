## Description: <br>
Safely applies OpenClaw configuration changes with backups, post-restart health checks, automatic rollback on failure, and commands for patching, restoring, listing backups, diffing, validation, and doctor checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emberdesire](https://clawhub.ai/user/emberdesire) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators who manage OpenClaw gateways use this skill to preview and apply configuration patches, maintain backups, validate configuration files, check gateway health, and restore a previous configuration when a change fails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool can modify local OpenClaw configuration and restart the gateway. <br>
Mitigation: Review patches before applying them and use --dry-run to preview changes when possible. <br>
Risk: Configuration backups may contain provider keys or other private settings from openclaw.json. <br>
Mitigation: Protect and periodically review ~/.openclaw/config-backups, and apply the same access controls used for the live OpenClaw configuration. <br>
Risk: Array values are replaced wholesale during patching. <br>
Mitigation: When patching arrays, include the complete intended array rather than only the changed elements. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/emberdesire/skills/jasper-configguard) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Jasper ConfigGuard Product Page](https://exohaven.online/products/jasper-configguard) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce patch previews, configuration diffs, backup identifiers, validation results, health-check status, and rollback results.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
