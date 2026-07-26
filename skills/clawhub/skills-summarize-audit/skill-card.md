## Description: <br>
Audits installed skills and plugins for source, version, availability, metadata, conflicts, ecosystem fit, Chinese display text, project profiling, and recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gtbwpkwjnb-alt](https://clawhub.ai/user/gtbwpkwjnb-alt) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to inspect installed skills, plugins, MCP configuration, project context, and display metadata before deciding what to keep, refine, hide, or review further. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect local skills, plugins, project files, MCP configuration, and session history, which may contain sensitive information. <br>
Mitigation: Run it only against explicit directories you intend to audit, review outputs before sharing, and redact session or project data when needed. <br>
Risk: A helper script may run local diagnostic commands beyond the read-only description. <br>
Mitigation: Inspect the script before execution, verify the PATH and local binaries it can call, and disable the live diagnostic probe if it is not needed. <br>
Risk: Lifecycle and action outputs may include commands or configuration changes that would affect local agent setup if executed. <br>
Mitigation: Treat generated actions as proposals only; require explicit confirmation, backups, and review before applying changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gtbwpkwjnb-alt/skills/skills-summarize-audit) <br>
- [README](README.md) <br>
- [Health checklist](references/health-checklist.md) <br>
- [MCP health checklist](references/mcp-health-checklist.md) <br>
- [Recommendation framework](references/recommendation-framework.md) <br>
- [Output contract](references/output-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON reports with optional shell command templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default behavior is read-only, but local scans may include skills, plugins, project files, MCP configuration, and session history within the supplied scope.] <br>

## Skill Version(s): <br>
9.1.0 (source: ClawHub release metadata and VERSION file) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
