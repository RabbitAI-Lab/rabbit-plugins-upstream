## Description:

Operate Canonry through the cnry/canonry CLI for answer engine optimization, including visibility sweeps, technical audits, search and analytics integrations, server-side traffic evidence, reporting, and guarded content or marketing operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and site operators use this skill to operate Canonry projects from an agent session: configure projects, connect analytics and search sources, run AEO sweeps and audits, interpret mention and citation coverage, and prepare approved fixes or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canonry can access configured business, analytics, CMS, traffic, and ads accounts through local credentials.

Mitigation: Use read-only or project-scoped keys where possible, keep ~/.canonry/config.yaml private with restrictive file permissions, and do not paste credentials or config contents into chat.

Risk: Write-capable keys can expose mutation surfaces such as project changes, CMS edits, indexing submissions, schedules, traffic activation, and guarded ads operations.

Mitigation: Require explicit operator approval for mutations and quota-consuming sweeps, use dry-run previews when supported, and do not switch credentials to bypass a missing tool or 403 response.

Risk: Server-side traffic integrations may process production request logs or route events through a Worker or log integration.

Mitigation: Review privacy implications before enabling production traffic collection, scope credentials to the needed source, and inspect backlog or sync status before changing schedules.

Risk: Generated reports and analysis can include client-specific domains, visibility metrics, or competitor findings.

Mitigation: Keep client data private, avoid posting real domains or credential-derived outputs in public issues, and lead reports with measured mention and citation data rather than fabricated or inferred results.

## Reference(s):

- [Canonry ClawHub listing](https://clawhub.ai/arberx/skills/canonry)
- [Canonry website](https://canonry.ai)
- [Canonry documentation repository](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis](references/aeo-analysis.md)
- [Indexing Workflows](references/indexing.md)
- [Server-side Traffic](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 22.14+ and a globally installed @canonry/canonry runtime with canonry-mcp on PATH.]

## Skill Version(s):

4.168.0+a49e71a (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
