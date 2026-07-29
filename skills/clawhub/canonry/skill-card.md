## Description: <br>
Set up and operate Canonry AEO projects: inspect mention and citation coverage, diagnose regressions, run technical audits, and act through the Canonry CLI or MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arberx](https://clawhub.ai/user/arberx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and site operators use this skill to measure AI answer-engine mention and citation coverage, diagnose AEO regressions, run technical audits, and apply approved fixes through Canonry CLI workflows and integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide operations that touch analytics, site, ad, traffic-log, and Canonry configuration systems. <br>
Mitigation: Install it only for Canonry operations, prefer read-only or project-scoped keys where possible, and protect ~/.canonry/config.yaml as a secrets file. <br>
Risk: Write actions, quota-consuming sweeps, schedules, webhooks, WordPress changes, ads actions, and server-log ingestion can affect live projects or expose sensitive operational data. <br>
Mitigation: Require explicit operator approval before each mutation or quota-consuming run, preview supported mutations with dry-run flows, and enable only the integrations needed for the engagement. <br>
Risk: Misreading Canonry signals could produce misleading AEO recommendations. <br>
Mitigation: Keep mention and citation signals separate, avoid fabricating missing sweep data, and report uncertainty when evidence has not been collected. <br>


## Reference(s): <br>
- [Canonry skill page](https://clawhub.ai/arberx/skills/canonry) <br>
- [Canonry website](https://canonry.ai) <br>
- [Canonry GitHub documentation](https://github.com/Canonry/canonry) <br>
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology) <br>
- [AEO Analysis](references/aeo-analysis.md) <br>
- [Canonry CLI](references/canonry-cli.md) <br>
- [Google Business Profile](references/google-business-profile.md) <br>
- [Indexing Workflows](references/indexing.md) <br>
- [Server-side Traffic](references/server-side-traffic.md) <br>
- [WordPress Integration](references/wordpress-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, code and configuration snippets, and JSON-oriented command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance emphasizes operator approval for mutations and quota-consuming sweeps.] <br>

## Skill Version(s): <br>
4.136.1+a5b2a12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
