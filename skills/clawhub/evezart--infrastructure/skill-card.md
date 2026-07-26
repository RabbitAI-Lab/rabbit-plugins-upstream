## Description: <br>
Design, provision, and connect cloud resources across servers, networks, and services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evezart](https://clawhub.ai/user/evezart) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to choose deployment patterns, provider commands, and backup practices for small-to-scaling cloud applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud provisioning examples can create, expose, or modify infrastructure if run without review. <br>
Mitigation: Review each command, region, firewall rule, account, and credential environment before execution; prefer listing or dry-run behavior where available. <br>
Risk: Backup retention and restore examples can delete or overwrite data when adapted incorrectly. <br>
Mitigation: Confirm bucket and prefix values, keep versioned or otherwise recoverable backups, and test restores before automating retention cleanup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/evezart/infrastructure) <br>
- [Architecture patterns](artifact/patterns.md) <br>
- [Cloud provider reference](artifact/providers.md) <br>
- [Backup strategies](artifact/backups.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [User-run commands; cloud credentials remain in the user's environment.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
