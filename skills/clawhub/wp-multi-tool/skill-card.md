## Description: <br>
WordPress site health audit, performance optimization, database cleanup, autoload tuning, slow query detection, wp-config management, image size control, frontend speed fixes, and server diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marcindudekdev](https://clawhub.ai/user/marcindudekdev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site owners, and WordPress operators use this skill to inspect site health, diagnose performance bottlenecks, and apply WP-CLI based optimization or cleanup actions with confirmation for writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: WP-CLI commands can inspect or change a live WordPress site. <br>
Mitigation: Use the skill only on sites where the operator is authorized to run WP-CLI, and review proposed commands before execution. <br>
Risk: Cleanup, configuration edits, frontend toggles, or plugin activation can modify data or site behavior. <br>
Mitigation: Require explicit user confirmation for write operations and take a database backup before destructive cleanup commands. <br>


## Reference(s): <br>
- [WP Multitool Homepage](https://wpmultitool.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool) <br>
- [Publisher Profile](https://clawhub.ai/user/marcindudekdev) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with WP-CLI command blocks and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only diagnostics can be proposed directly; write operations require user confirmation.] <br>

## Skill Version(s): <br>
1.8.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
