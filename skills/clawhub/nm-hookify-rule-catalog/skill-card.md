## Description: <br>
Browse hookify rule catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to browse standard Hookify rule categories and install pre-built local Claude hook rules when they want guardrails for Git, Python quality, security, workflow, or performance tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing catalog rules can create or update local Claude hook rule files. <br>
Mitigation: Review the selected rule content and destination under .claude before allowing installation. <br>
Risk: Bulk installation can add multiple rules at once. <br>
Mitigation: Avoid bulk --all installs unless each rule and its effect are understood. <br>
Risk: Custom target paths or overwrites can place rules somewhere unintended. <br>
Mitigation: Confirm overwrite prompts and custom target paths explicitly before proceeding. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-hookify-rule-catalog) <br>
- [Hookify homepage](https://github.com/athola/claude-night-market/tree/master/plugins/hookify) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, rule identifiers, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to create or update local .claude Hookify rule files when installation is explicitly requested.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
