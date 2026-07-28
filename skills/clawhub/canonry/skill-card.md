## Description: <br>
Set up and operate Canonry AEO projects: inspect mention and citation coverage, diagnose regressions, run technical audits, and act through the Canonry CLI or MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arberx](https://clawhub.ai/user/arberx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and SEO/AEO operators use this skill to measure answer-engine mention and citation coverage, diagnose visibility regressions, run technical audits, and operate Canonry CLI workflows for indexing, analytics, WordPress, traffic, Google Business Profile, and ads tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed for connected marketing, analytics, website, and ads properties, so a broadly scoped Canonry key can expose high-impact operational access. <br>
Mitigation: Install it only for intended Canonry operations, prefer read-only or project-scoped keys where possible, and do not work around authorization failures by switching credentials. <br>
Risk: Canonry initialization can create or reveal sensitive API keys and stores configuration under the user's Canonry config directory. <br>
Mitigation: Run initialization privately, never paste keys into chat, avoid printing config files, and protect the Canonry config file from backups or dotfile sync. <br>
Risk: WordPress writes, ads actions, schedules, account switching, and quota-consuming sweeps can change live systems or consume provider quota. <br>
Mitigation: Require explicit operator approval for those actions and use read-only commands or dry-run previews before committing changes. <br>


## Reference(s): <br>
- [Canonry](https://canonry.ai) <br>
- [Canonry GitHub Documentation](https://github.com/Canonry/canonry) <br>
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology) <br>
- [Canonry CLI Reference](references/canonry-cli.md) <br>
- [AEO Analysis](references/aeo-analysis.md) <br>
- [Indexing Workflows for AEO](references/indexing.md) <br>
- [Server-side traffic](references/server-side-traffic.md) <br>
- [Google Business Profile Integration](references/google-business-profile.md) <br>
- [WordPress Integration](references/wordpress-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI output references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a separately installed canonry CLI and operator approval for mutations, schedules, account switching, and quota-consuming sweeps.] <br>

## Skill Version(s): <br>
4.135.0+c7f0290 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
