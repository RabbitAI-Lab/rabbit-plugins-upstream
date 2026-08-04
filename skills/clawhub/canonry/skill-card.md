## Description: <br>
Set up and operate Canonry AEO projects: inspect mention and citation coverage, diagnose regressions, run technical audits, and act through the Canonry CLI or MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arberx](https://clawhub.ai/user/arberx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External teams, developers, and site operators use this skill to measure AI answer-engine visibility, diagnose mention and citation regressions, run technical AEO audits, and operate Canonry workflows through CLI or MCP tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide operations against websites, analytics sources, WordPress, Google Business Profile, and ads accounts. <br>
Mitigation: Install only for owned or authorized environments, confirm the target account or site before changes, and require explicit approval before mutations, scheduled sweeps, or quota-consuming runs. <br>
Risk: Canonry credentials may grant broad access to project and instance settings. <br>
Mitigation: Prefer read-only or project-scoped keys where possible, keep configuration files private, and do not switch credentials to bypass authorization failures. <br>
Risk: AEO findings can be misleading if mention and citation signals are fabricated, conflated, or measured without permission. <br>
Mitigation: Use existing measurements when available, keep mention and citation separate, and obtain explicit approval before probes or persisted sweeps. <br>


## Reference(s): <br>
- [Canonry website](https://canonry.ai) <br>
- [Canonry documentation](https://github.com/Canonry/canonry) <br>
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology) <br>
- [AEO Analysis](references/aeo-analysis.md) <br>
- [Canonry CLI Reference](references/canonry-cli.md) <br>
- [Indexing Workflows for AEO](references/indexing.md) <br>
- [WordPress Integration](references/wordpress-integration.md) <br>
- [Server-side traffic](references/server-side-traffic.md) <br>
- [Google Business Profile Integration](references/google-business-profile.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Canonry CLI or MCP actions; mutations, scheduled sweeps, and quota-consuming runs require explicit operator approval.] <br>

## Skill Version(s): <br>
4.143.0+54ee5bb (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
