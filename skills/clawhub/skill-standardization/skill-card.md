## Description: <br>
skill-standardization audits, creates, updates, refactors, and version-bumps agent skills against R-01 to R-26 standardization rules, including permission scanning, data-directory compliance checks, progressive disclosure checks, and LLM-assisted issue classification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and skill maintainers use this skill to check agent skill structure, metadata, permissions, documentation quality, and release consistency, then optionally create or repair standardized skill files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated update, refactor, and fix modes can rewrite, move, back up, or delete skill files. <br>
Mitigation: Run these modes only on disposable or version-controlled skill directories and review diffs, backups, and generated reports before relying on the result. <br>
Risk: The skill is intended to inspect other skill directories and may read source or documentation files in the target tree. <br>
Mitigation: Avoid running it on directories that contain secrets or unrelated user files; prefer readonly or audit commands when edits are not required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/skill-standardization) <br>
- [Guide](references/guide.md) <br>
- [Rules](references/rules.md) <br>
- [Permissions](references/permissions.md) <br>
- [Architecture](references/architecture.md) <br>
- [Changelog](references/changelog.md) <br>
- [License](references/LICENSE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, terminal output, JSON metadata, and file edits when fix or refactor modes are used] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some modes can write, move, back up, or delete skill files.] <br>

## Skill Version(s): <br>
2.103.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
