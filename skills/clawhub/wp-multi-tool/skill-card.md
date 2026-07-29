## Description: <br>
WP Multitool helps agents audit and optimize WordPress sites with WP-CLI diagnostics, database cleanup guidance, autoload tuning, slow query review, wp-config management, image controls, frontend speed checks, and server diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marcindudekdev](https://clawhub.ai/user/marcindudekdev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External WordPress site owners, developers, and operations engineers use this skill to run WP-CLI diagnostics, inspect WP Multitool plugin data when available, and prepare or execute confirmed cleanup and configuration commands for site performance work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write operations can delete or modify WordPress data, database tables, wp-config.php, or plugin options. <br>
Mitigation: Require explicit user confirmation before cleanup, optimization, wp-config, frontend toggle, or plugin option commands, and recommend a database export before destructive cleanup. <br>
Risk: The artifact includes a plugin activation command that changes site state without the same explicit confirmation framing as other write operations. <br>
Mitigation: Treat plugin activation as a write operation and require user approval before running it, especially on production sites. <br>
Risk: Commands executed against production WordPress sites may affect availability or performance during database optimization or cleanup. <br>
Mitigation: Review the target environment before installation or execution, prefer maintenance windows for locking operations, and inspect command scope before running WP-CLI writes. <br>


## Reference(s): <br>
- [WP Multitool homepage](https://wpmultitool.com) <br>
- [ClawHub skill listing](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [WP-CLI commands may be read-only diagnostics or confirmed write operations; plugin-specific commands require WP Multitool to be installed and active.] <br>

## Skill Version(s): <br>
1.9.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
