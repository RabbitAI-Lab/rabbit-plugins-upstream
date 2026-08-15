## Description:

Set up and operate Canonry AEO projects: inspect mention and citation coverage, diagnose regressions, run technical audits, connect traffic sources, and act through the Canonry CLI or MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing engineers use this skill to run Answer Engine Optimization workflows for tracked brands, including visibility analysis, technical audits, indexing workflows, reporting, and integration setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate against connected sites, analytics properties, ad accounts, and the local Canonry credential file.

Mitigation: Install only where that access is acceptable, protect ~/.canonry/config.yaml, and prefer read-only or project-scoped keys where possible.

Risk: Write-capable workflows can affect WordPress, ads, deletes, schedules, traffic deployments, or quota-consuming operations.

Mitigation: Require explicit approval before those actions and use dry-run or read-only checks when available.

## Reference(s):

- [Canonry ClawHub Skill Page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry Website](https://canonry.ai)
- [Canonry Documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON-oriented command outputs, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run Canonry CLI and MCP-backed workflows, with approval required for mutations and quota-consuming operations.]

## Skill Version(s):

4.160.0+8f9d732 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
