## Description: <br>
Diagnose, fix, and prevent agent skill trigger failures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaszhou22](https://clawhub.ai/user/thomaszhou22) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use Skill Compass to audit SKILL.md files, diagnose why skills do not activate reliably, and generate fixes for routing, frontmatter, token budget, and trigger conflicts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic repair options can modify installed skill descriptions. <br>
Mitigation: Run audit mode first, review suggested rewrites, and keep backups before using --fix or --init. <br>
Risk: Rollback or broad scans may affect the wrong skill directory if the target path is ambiguous. <br>
Mitigation: Pass an explicit --skills-dir and verify the target directory before using repair or rollback workflows. <br>


## Reference(s): <br>
- [Failure Pattern Reference](references/failure-patterns.md) <br>
- [Hierarchical Routing Guide](references/hierarchical-routing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown audit reports with inline shell commands, JSON reports when requested, and suggested skill description edits] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or apply SKILL.md rewrites, create backups, and produce rollback guidance when invoked with repair options.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
