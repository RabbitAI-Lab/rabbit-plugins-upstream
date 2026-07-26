## Description: <br>
AIFLC PDLC Family provides 11 injectable workflow packages that guide AI coding agents through professional software delivery from idea evaluation through architecture, workspace generation, governance, compliance, and test accountability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mbmd](https://clawhub.ai/user/mbmd) <br>

### License/Terms of Use: <br>
Apache-2.0 with Attribution Addendum <br>


## Use Case: <br>
Developers, engineers, product teams, and delivery leads use this skill to add structured product-development lifecycle guidance to AI coding agents. It helps agents guide projects through initiation, portfolio governance, product ownership, UX design, architecture, workspace generation, compliance, and test planning with human approval gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill can add persistent agent routing or governance files such as AGENTS.md, CLAUDE.md imports, platform rule files, hooks, dashboards, reports, and outboxes. <br>
Mitigation: Use dry-run or an isolated branch first, review generated files and hooks before enabling them, and keep changes under version control. <br>
Risk: Generated reports, compliance logs, or test-mode outboxes may capture sensitive project information if users provide it during workflows. <br>
Mitigation: Avoid putting secrets or sensitive data into prompts, generated reports, test-mode outboxes, or dashboard data; review outputs before sharing or committing them. <br>
Risk: Optional dashboard behavior may depend on a Mermaid CDN path, which can be unsuitable for network-isolated environments. <br>
Mitigation: Vendor Mermaid locally or disable CDN-dependent dashboard paths when network isolation matters. <br>
Risk: Brownfield adoption can conflict with existing project files, conventions, or governance structures. <br>
Mitigation: Back up the workspace, use a test branch, and inspect the package's documented output structure before applying it to a main project. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mbmd/skills/pdlc) <br>
- [README](README.md) <br>
- [Security Policy](SECURITY.md) <br>
- [Licensing FAQ](LICENSING_FAQ.md) <br>
- [Changelog](CHANGELOG.md) <br>
- [Platform Capabilities](PLATFORM_CAPABILITIES.md) <br>
- [Rollback Plan](ROLLBACK_PLAN.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, workspace instruction files, templates, shell or PowerShell commands, and structured state or report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Designed for human approval gates; installation and use may add persistent workspace guidance, platform rule files, hooks, dashboard files, reports, and test-mode outputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
