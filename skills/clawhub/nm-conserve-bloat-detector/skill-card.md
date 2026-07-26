## Description: <br>
Detects codebase bloat via dead code, duplication, complexity, and documentation bloat scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to scan repositories for dead code, duplication, dependency bloat, stale files, growth trends, and documentation bloat before cleanup, release, or refactoring work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad repository scans can include more files than intended, especially when ignore-file handling is incomplete. <br>
Mitigation: Confirm the scan scope and maintain .bloat-ignore exclusions before running repository-wide checks. <br>
Risk: The optional package-registry lookup can disclose package names to an external registry. <br>
Mitigation: Skip or explicitly approve the npm view check when dependency names or network access are sensitive. <br>
Risk: DELETE recommendations can remove useful code or documentation if treated as automatic actions. <br>
Mitigation: Treat DELETE findings as review candidates and require tests, reference checks, dry-run review, and backups before removal. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-bloat-detector) <br>
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and YAML report examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes confidence levels, bloat scores, recommended remediation actions, and review-first cleanup guidance.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
