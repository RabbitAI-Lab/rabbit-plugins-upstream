## Description:

MC Ecosystem Adaptation Engineer helps Minecraft mod players and modpack creators manage mod searches, environment setup, compatibility scanning, crash analysis and fixes, translation, save sync, licensing, payments, admin workflows, and business reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liang030214](https://clawhub.ai/user/liang030214)

### License/Terms of Use:

MIT-0

## Use Case:

External Minecraft mod players and modpack creators use this skill to inspect mod JARs, find compatible mod versions, build loader/version environments, analyze crashes and migration feasibility, translate assets, and produce reports or repair guidance. Operators can also use its commercial licensing, payment, admin, and business-reporting features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad file, network, download, and write behavior can affect local modpacks, saves, generated reports, and downloaded JARs.

Mitigation: Review actions before execution, limit runs to trusted directories, keep backups, and avoid auto-fix on sensitive modpacks until URL allowlists and download hash checks are in place.

Risk: Licensing state, usage data, and local authorization endpoints may expose operational or account-related information.

Mitigation: Avoid starting the local API around sensitive license data unless authentication and CORS controls are added, and review local authorization storage before deployment.

Risk: Security evidence flags under-disclosed telemetry and external service contact for geolocation and mod metadata.

Mitigation: Provide clear opt-in notices, document outbound services, and disable or isolate telemetry and geolocation calls where they are not needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liang030214/skills/mc-ecosystem-adapt-engine)
- [Modrinth API](https://api.modrinth.com/v2)
- [CurseForge API](https://api.curseforge.com/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, HTML reports, generated files, and command-line output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read local modpacks, crash logs, save data, and authorization state; may write reports, backups, translated resources, repacked mods, payment pages, and auto-fix outputs.]

## Skill Version(s):

1.0.4 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
