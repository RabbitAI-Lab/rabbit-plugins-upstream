## Description: <br>
Review plugin quality with tiered checks and dependency scoping for PR and pre-release audits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to scope changed plugins, run tiered quality gates, and summarize pass, warning, or fail results before merge or release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad review, quality, validation, testing, and architecture triggers may activate the skill on general audit requests. <br>
Mitigation: Use explicit tier and scope wording, and review the planned checks before allowing the agent to proceed. <br>
Risk: The skill can guide an agent to run repo-local validation, test, lint, typecheck, git diff, and dependency-map commands. <br>
Mitigation: Run it only in compatible repositories where local quality checks are appropriate, and inspect commands before execution. <br>
Risk: Some checks depend on Night Market configuration, scripts, or evaluator skills that may not exist in other repositories. <br>
Mitigation: Confirm required config and scripts are present; when unavailable, report skipped checks rather than treating them as completed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-plugin-review) <br>
- [clawdis homepage: claude-night-market abstract plugin](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown review report with tables, verdicts, scorecards, and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include quality gate exit-code guidance and tier-specific remediation actions.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
