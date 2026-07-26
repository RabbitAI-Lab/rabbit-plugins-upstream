## Description: <br>
Audits, creates, updates, refactors, and version-bumps agent skills against R-01 to R-26 standardization rules, with permission scanning and structured reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this skill to inspect existing skills, create standard skill skeletons, apply structural fixes, and generate audit reports before publishing or updating a release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically rewrite, move, delete, back up, and version-bump other skill projects. <br>
Mitigation: Run read-only audits first, review generated reports and planned changes, and keep an external backup or version-control commit before update, refactor, or fix flows. <br>
Risk: The cleanup dry-run behavior should not be treated as a guaranteed no-op preview. <br>
Mitigation: Avoid relying on cleanup --dry-run alone; inspect generated reports and planned changes in a controlled workspace before allowing cleanup actions. <br>
Risk: The skill reads and edits target skill source files. <br>
Mitigation: Use it only on intended skill directories and review resulting file changes before publishing or installing the modified skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/skill-standardization) <br>
- [Skill guide](references/guide.md) <br>
- [Audit rules](references/rules.md) <br>
- [Permissions and testing](references/permissions.md) <br>
- [Architecture](references/architecture.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON status data, patched skill files, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May modify target skill files during update, refactor, and fix flows; read-only audit mode is available for inspection-first use.] <br>

## Skill Version(s): <br>
2.102.9 (source: server release, SKILL.md frontmatter, _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
